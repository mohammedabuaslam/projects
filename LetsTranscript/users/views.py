from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import views as auth_views
from django.views import generic
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, get_user_model, login
from django.views.generic import View, ListView
from django.core.mail import EmailMessage
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text
from django.template.loader import render_to_string, get_template
from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponse, JsonResponse
from django.utils.safestring import mark_safe
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.static import serve
from .forms import LoginForm, RegisterForm, UserPasswordResetForm
from .models import Orders
from .tokens import account_activation_token, user_password_reset_token
import secrets, re, json, boto3, os, socket, threading, librosa, paypalrestsdk, time, math
from django.views.decorators.csrf import csrf_exempt
from django.template import RequestContext

paypalrestsdk.configure({
  "mode": "live",
  "client_id": "YOUR CLIENT ID",
  "client_secret": "YOUR CLIENT SECRET" })

def test(request):
    return render(request, 'main/sendleademail.html')

def handler404(request, exception):
    return render(request, 'errors/404.html',{'title':'404'})

def handler403(request, exception):
    return render(request, 'errors/403.html',{'title':'403'})

def handler500(request):
    context = {}
    response = render(request, "errors/500.html", context=context)
    response.status_code = 500
    return response

def sendhumangeneratedemail(clientemail,filename,filedurationinminutes,transcriptiontype,turnaroundtime,verbatimtype,subtitles,humangeneratedlanguage,noofspeakers,comments,ordervalue):
    message = render_to_string('payments/sendhumangeneratedemail.html',{'filename': filename,'filedurationinminutes': filedurationinminutes,'transcriptiontype': transcriptiontype,'turnaroundtime': turnaroundtime,'verbatimtype': verbatimtype,'subtitles': subtitles,'humangeneratedlanguage': humangeneratedlanguage,'noofspeakers': noofspeakers,'comments': comments,'ordervalue': ordervalue,'clientemail':clientemail,})
    mail_subject = 'Order Placed - ' + str(filename)
    email = EmailMessage(mail_subject, message, to=['YOUR EMAIL',clientemail])
    email.content_subtype = "html"
    email.send()

def sendautomatedemail(clientemail,filename,filedurationinminutes,transcriptiontype,subtitles,foreignsubtitles,ordervalue,automatedlanguage):
    message = render_to_string('payments/sendautomatedemail.html',{'clientemail':clientemail,'filename':filename,'filedurationinminutes':filedurationinminutes,'transcriptiontype':transcriptiontype,'subtitles':subtitles,'foreignsubtitles':foreignsubtitles,'ordervalue':ordervalue,})
    mail_subject = 'Order Placed - ' + str(filename)
    email = EmailMessage(mail_subject, message, to=['YOUR EMAIL',clientemail])
    email.content_subtype = "html"
    createorderdict = {
    'filepath' : filename[0:6],
    'mediaformat' : filename[-4:],
    'email' : clientemail,
    'lang' : automatedlanguage,
    'Requires_SRT' : subtitles,
    'Requires_Foreign_Srt' : foreignsubtitles
    }
    sendserver = json.dumps(createorderdict)
    sendserver = sendserver.encode('utf-8')
    host = "YOUR REMOTE SERVER TO HANDLE THE ORDER"
    port = 12345
    serverSocket = socket.socket()
    serverSocket.connect((host, port))
    serverSocket.send(sendserver)
    serverSocket.close
    email.send()

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password =request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
            # elif user is not None and user.email_verified==False:
            #     messages.info(request, mark_safe("Dear user, you have not activated your account. To activate you account, you need to verify your email. To get a verification link <a href='/users/accountactivation'>fill this form</a>"))
            #     return redirect('login')
            else:
                messages.info(request, 'Invalid Credentials')
        return render(request, 'users/login.html',{'title':'Login'})

def RegisterView(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            # site = get_current_site(request)
            username = form.cleaned_data.get('username')
            country = form.cleaned_data.get('country')
            phone = form.cleaned_data.get('phone')
            user = form.save(commit=False)
            user.email_verified = False
            user.username = username.lower()
            user.phone = phone
            try:
                user.save()
            except Exception as e:
                print(e)
                messages.info(request, 'This username is taken, please choose a different username')
                return redirect('register')
            # message = render_to_string('users/account_activation.html', {
            #     'user':user, 'domain':'letstranscript.com',
            #     'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            #     'token': account_activation_token.make_token(user),
            # })
            # mail_subject = 'Please confirm your LetsTranscript account.'
            # to_email = form.cleaned_data.get('email')
            # email = EmailMessage(mail_subject, message, to=[to_email])
            # email.content_subtype = "html"
            # email.send()
            messages.success(request, 'Your account was created successfully. Please login to proceed.')
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'users/register.html', {'form': form, 'title':'Register'})   

def user_password_reset(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method == 'POST':
        form = UserPasswordResetForm(request.POST)
        if form.is_valid():
            # site = get_current_site(request)
            email = form.cleaned_data.get('email')
            if User.objects.filter(email=email).exists():
                user = User.objects.filter(email=email)
                message = render_to_string('users/password_reset_mail.html', {
                    'user':user, 'domain':'letstranscript.com',
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'token': user_password_reset_token.make_token(user),
                })
                mail_subject = 'Password Reset Request.'
                email = EmailMessage(mail_subject, message, to=[email])
                email.content_subtype = "html"
                email.send()

                messages.success(request, 'An email has been sent with password reset instructions. Please check your email to reset your password. If you did not recieve the email, please check your spam folder.')
                return redirect('user_password_reset')
            else:
                messages.warning(request, mark_safe('We could not find an account associated with this email. Please check if the email entered by you is correct. You can <a href="/users/register">register your account here</a>'))
    else:
        form = UserPasswordResetForm()
    return render(request, 'users/request_password_reset.html', {'form': form,'title':'Password Reset'})


@login_required
@csrf_exempt
def upload(request):
    if request.method == 'POST':
        originalfilename = request.FILES["file"]
        name,ext = originalfilename.name.rsplit('.',1)
        try:
            _,ext = ext.split('.')
        except:
            pass
        token = secrets.token_hex(3)
        uniquefilename = str(token)+'____'+str(name+'.'+ext)
        folder = settings.MEDIA_ROOT+'/useruploads' 
        fs = FileSystemStorage(location=folder)
        fs.save(token+'.'+ext, originalfilename)
        try:
            seconds = int(librosa.get_duration(filename=folder+'/'+token+'.'+ext))
        except:
            seconds = 0
            return JsonResponse(status=404)
        return JsonResponse({"message": f"{uniquefilename} uploaded successfully", "totalduration":seconds, "uniquefilename":uniquefilename}, status=200)
    else:
        return render(request, 'users/upload.html',{'title':'Upload'})

@login_required
@csrf_exempt
def orderplaced(request):
    if request.method == 'POST':
        updatedData = json.loads(request.body.decode('UTF-8'))
        User = get_user_model()
        user = User.objects.get(username=request.user.username)
        order = Orders()
        order.uniqueordertracker = updatedData['filename'][0:6]
        order.ordername = updatedData['filename']
        order.totalminutecount = updatedData['filedurationinminutes']
        order.orderstatus = 'processing'
        order.paymentstatus = 'paid'
        order.ordervalue = updatedData['ordervalue']
        if updatedData['transcriptiontype'] == 0.8:
            transcriptiontype = 'Human-Generated'
        else:
            transcriptiontype = 'Automated'
        if updatedData['turnaroundtime'] == 0:
            turnaroundtime = '3 Days'
        else:
            turnaroundtime = '1 Day'
        if updatedData['verbatimtype'] == 0:
            verbatimtype = 'Clean Verbatim'
        else:
            verbatimtype = 'Full Verbatim'
        if updatedData['subtitles'] == 0:
            subtitles = 'No'
        else:
            subtitles = 'Yes'
        if updatedData['foreignsubtitles'] == 0:
            foreignsubtitles = 'No'
        else:
            foreignsubtitles = 'Yes'
        order.transcriptiontype = transcriptiontype
        order.turnaroundtime = turnaroundtime
        order.verbatimtype = verbatimtype
        order.subtitles = subtitles
        order.foreignsubtitles = foreignsubtitles
        order.noofspeakers = updatedData['noofspeakers']
        order.comments = updatedData['comments']
        order.humangeneratedlanguage = updatedData['humangeneratedlanguage']
        order.automatedlanguage = updatedData['automatedlanguage']
        order.foriegnsubtitlelanguage = updatedData['foreignlanguage']
        order.author = request.user
        user.credits = round(float(user.credits) - float(updatedData['ordervalue']),2)
        s3 = boto3.resource('s3', aws_access_key_id='YOUR ACCESS KEY ID', aws_secret_access_key='YOUR ACCESS SECRET KEY')
        absolutefilepath = settings.MEDIA_ROOT+'/useruploads/'+str(updatedData['filename'][0:6]+updatedData['filename'][-4:])
        s3.Bucket('YOUR BUCKET NAME').upload_file(absolutefilepath, updatedData['filename'][0:6]+updatedData['filename'][-4:])
        order.save()
        user.save()
        if transcriptiontype == 'Human-Generated':
            sendhumangeneratedemail(user.email,updatedData['filename'],updatedData['filedurationinminutes'],transcriptiontype,turnaroundtime,verbatimtype,subtitles,updatedData['humangeneratedlanguage'],updatedData['noofspeakers'],updatedData['comments'],updatedData['ordervalue'])
        if transcriptiontype == 'Automated':
            sendautomatedemail(user.email,updatedData['filename'],updatedData['filedurationinminutes'],transcriptiontype,subtitles,foreignsubtitles,updatedData['ordervalue'],updatedData['automatedlanguage'])
        os.remove(settings.MEDIA_ROOT+'/useruploads/'+str(updatedData['filename'][0:6]+updatedData['filename'][-4:]))
        return redirect('dashboard')
    else:
        return render(request, 'users/orderplaced.html',{'title':'Order Placed'})

@login_required
@csrf_exempt
def submitorderforprocessing(request):
    if request.method == 'POST':
        updatedData=json.loads(request.body.decode('UTF-8'))
        User = get_user_model()
        user = User.objects.get(username=request.user.username)
        order = Orders()
        order.uniqueordertracker = updatedData['filename'][0:6]
        order.ordername = updatedData['filename']
        order.totalminutecount = updatedData['filedurationinminutes']
        order.orderstatus = 'processing'
        order.paymentstatus = 'pending'
        order.ordervalue = updatedData['ordervalue']
        if updatedData['transcriptiontype'] == 0.8:
            transcriptiontype = 'Human-Generated'
        else:
            transcriptiontype = 'Automated'
        if updatedData['turnaroundtime'] == 0:
            turnaroundtime = '3 Days'
        else:
            turnaroundtime = '1 Day'
        if updatedData['verbatimtype'] == 0:
            verbatimtype = 'Clean Verbatim'
        else:
            verbatimtype = 'Full Verbatim'
        if updatedData['subtitles'] == 0:
            subtitles = 'No'
        else:
            subtitles = 'Yes'
        if updatedData['foreignsubtitles'] == 0:
            foreignsubtitles = 'No'
        else:
            foreignsubtitles = 'Yes'
        order.transcriptiontype = transcriptiontype
        order.turnaroundtime = turnaroundtime
        order.verbatimtype = verbatimtype
        order.subtitles = subtitles
        order.foreignsubtitles = foreignsubtitles
        order.noofspeakers = updatedData['noofspeakers']
        order.comments = updatedData['comments']
        order.humangeneratedlanguage = updatedData['humangeneratedlanguage']
        order.automatedlanguage = updatedData['automatedlanguage']
        order.foriegnsubtitlelanguage = updatedData['foreignlanguage']
        order.author = request.user
        amountpayable = float(updatedData['ordervalue']) - float(user.credits)
        order.save()
        return JsonResponse({'uniqueid':updatedData['filename'][0:6],'ordervalue':round(amountpayable, 2)})
    else:
        return redirect('upload')

@login_required
@csrf_exempt
def initiatepaymentprocess(request,encypdata,uniqueid):
    encypdata=encypdata
    uniqueid=uniqueid
    context = {}
    context['amountpayable'] = encypdata.replace('b8204657188fae32a6c884d4f9dfabbdcc1ba843','').replace('627bc999f7d73398fd9a93fd67dbb15e0ad691377b','')
    return render(request, 'payments/paymentprocessing.html',context)

@login_required
@csrf_exempt
def insufficientfunds(request, uniqueid, amountpayable):
    if request.method == 'POST':
        print(amountpayable)
        payment = paypalrestsdk.Payment({
            "intent": "sale",
            "payer": {
                "payment_method": "paypal"},
            "redirect_urls": {
                "return_url": "/users/upload",
                "cancel_url": "/"},
            "transactions": [{
                "item_list": {
                    "items": [{
                        "name": "YOUR COMPANY NAME",
                        "sku": "ABCD",
                        "price": amountpayable,
                        "currency": "USD",
                        "quantity": 1}]},
                "amount": {
                    "total": amountpayable,
                    "currency": "USD"},
                "description": "You are paying to YOUR COMPANY."}]})

        if payment.create():
            a='as'
        else:
            print(payment.error)
        return JsonResponse({'paymentID' : payment.id,'uniqueid':uniqueid,'ordervalue':amountpayable})
    else:
        return redirect('upload')

@login_required
@csrf_exempt
def executepayment(request, uniqueid, amountpayable):
    if request.method == 'POST':
        success = 'failed'
        User = get_user_model()
        user = User.objects.get(username=request.user.username)
        payment = paypalrestsdk.Payment.find(request.POST['paymentID'])
        if payment.execute({'payer_id' : request.POST['payerID']}):
            success = 'completed'
        else:
            success = 'failed'
        return JsonResponse({'success' : success,'uniqueid':uniqueid})
    else:
        return redirect('upload')

@login_required
@csrf_exempt
def placeorderafterpayment(request, uniqueid):
    if request.method == 'POST':
        currentorder = Orders.objects.get(uniqueordertracker=uniqueid)
        currentorder.paymentstatus = 'paid'
        User = get_user_model()
        user = User.objects.get(username=request.user.username)
        user.credits = 0
        currentorder.save()
        user.save()
        s3 = boto3.resource('s3', aws_access_key_id='YOUR ACCESS KEY ID', aws_secret_access_key='YOUR ACCESS SECRET KEY')
        absolutefilepath = settings.MEDIA_ROOT+'/useruploads/'+str(currentorder.ordername[0:6]+currentorder.ordername[-4:])
        s3.Bucket('YOUR BUCKET NAME').upload_file(absolutefilepath, currentorder.ordername[0:6]+currentorder.ordername[-4:])
        if currentorder.transcriptiontype == 'Human-Generated':
            sendhumangeneratedemail(user.email,currentorder.ordername,currentorder.totalminutecount,currentorder.transcriptiontype,currentorder.turnaroundtime,currentorder.verbatimtype,currentorder.subtitles,currentorder.humangeneratedlanguage,currentorder.noofspeakers,currentorder.comments,currentorder.ordervalue)
        if currentorder.transcriptiontype == 'Automated':
            sendautomatedemail(user.email,currentorder.ordername,currentorder.totalminutecount,currentorder.transcriptiontype,currentorder.subtitles,currentorder.foreignsubtitles,currentorder.ordervalue,currentorder.automatedlanguage)
        os.remove(settings.MEDIA_ROOT+'/useruploads/'+str(currentorder.ordername[0:6]+currentorder.ordername[-4:]))
        return JsonResponse({'success' : 'success'})
    else:
        return redirect('upload')


def clearstorage(request):
    current_time = time.time()
    thisdir = settings.MEDIA_ROOT+'/useruploads'
    for r, d, f in os.walk(thisdir):
        for file in f:
            path123 = os.path.join(r, file)
            creation_time = os.path.getctime(path123)
            if (current_time - creation_time) // (24 * 3600) >= 3:
                os.unlink(path123)
    messages.success(request, 'All files older than 3 days were removed successfully.')
    return render(request, 'users/clearstorage.html',{'title':'Clear Storage'})

class dashboard(LoginRequiredMixin, ListView):
    model = Orders
    template_name = 'users/dashboard.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 20

    def get_queryset(self):
        User = get_user_model()
        user = User.objects.get(username=self.request.user)
        return Orders.objects.filter(author=user).order_by('-date_posted')

    def get_context_data(self, **kwargs):
        context = super(dashboard, self).get_context_data(**kwargs)
        context['title'] = str(self.request.user).capitalize() +"'s" +' Dashboard'
        messages.success(self.request, 'Welcomeback '+str(self.request.user).capitalize())
        return context

class adminorders(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Orders
    template_name = 'users/adminorders.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 50
    def test_func(self):
        return self.request.user.is_superuser

def downloadorder(request):
    if request.method == 'POST':
        downloadfilename = request.POST['download']
        uniquefilename = downloadfilename[0:6]+str('.zip')
        file_and_path = settings.MEDIA_ROOT+'/deliveredorderstemp/'+downloadfilename+str('.zip')
        s3 = boto3.client('s3', aws_access_key_id='YOUR ACCESS KEY ID', aws_secret_access_key='YOUR ACCESS SECRET KEY')
        s3.download_file('YOUR BUCKET', 'YOUR BUCKET/'+uniquefilename, file_and_path)
        with open(file_and_path, 'wb') as f:
            userorderdownload = f.read()
        os.remove(file_and_path)
        response = HttpResponse(userorderdownload, content_type='multipart/mixed')
        response['Content-Disposition'] = "%sfilename=%s" % ('attachment;', downloadfilename[0:-4]+str('.zip'))
        return response
    else:
        return redirect('dashboard')

def downloadautomatedorder(request):
    if request.method == 'POST':
        downloadfilename = request.POST['download']
        uniquefilename = downloadfilename[0:6]+str('.zip')
        file_and_path = settings.MEDIA_ROOT+'/deliveredorderstemp/'+downloadfilename+str('.zip')
        s3 = boto3.client('s3', aws_access_key_id='YOUR ACCESS KEY ID', aws_secret_access_key='YOUR ACCESS SECRET KEY')
        s3.download_file('YOUR BUCKET', 'YOUR BUCKET/'+uniquefilename, file_and_path)
        with open(file_and_path, 'wb') as f:
            userorderdownload = f.read()
        os.remove(file_and_path)
        response = HttpResponse(userorderdownload, content_type='multipart/mixed')
        response['Content-Disposition'] = "%sfilename=%s" % ('attachment;', downloadfilename[0:-4]+str('.zip'))
        return response
    else:
        return redirect('dashboard')

@csrf_exempt
def submitorder(request):
    if request.method == 'POST':
        originalfilename = request.FILES["file"]
        folder = settings.MEDIA_ROOT+'/submitorderstemp'
        fs = FileSystemStorage(location=folder)
        fs.save(originalfilename.name,originalfilename)
        s3 = boto3.resource('s3', aws_access_key_id='YOUR ACCESS KEY ID', aws_secret_access_key='YOUR ACCESS SECRET KEY')
        absolutefilepath = settings.MEDIA_ROOT+'/submitorderstemp/'+str(originalfilename.name)
        s3.Bucket('YOUR BUCKET NAME').upload_file(absolutefilepath, 'YOUR BUCKET NAME/'+originalfilename.name)
        orders = Orders.objects.get(uniqueordertracker=originalfilename.name[0:6])
        orders.orderstatus = 'completed'
        orders.save()
        os.remove(settings.MEDIA_ROOT+'/submitorderstemp/'+str(originalfilename))
        return JsonResponse({"message": f"Your order {originalfilename} was submitted successfully"}, status=200)
    else:
        return render(request, 'users/submitorder.html')

@login_required
def addcreditstowallet(request):
    return render(request, 'payments/addcredits.html',{'title':'Add Credits'})

@login_required
@csrf_exempt
def addcreditstowalletprocessing(request,amount):
    if request.method == 'POST':
        
        payment = paypalrestsdk.Payment({
            "intent": "sale",
            "payer": {
                "payment_method": "paypal"},
            "redirect_urls": {
                "return_url": "",
                "cancel_url": ""},
            "transactions": [{
                "item_list": {
                    "items": [{
                        "name": "",
                        "sku": "",
                        "price": amount,
                        "currency": "USD",
                        "quantity": 1}]},
                "amount": {
                    "total": amount,
                    "currency": "USD"},
                "description": "You are paying to ."}]})

        if payment.create():
            a='as'
        else:
            print(payment.error)

        return JsonResponse({'paymentID' : payment.id,'Amount':amount})
    else:
        return render(request, 'payments/addcredits.html')

@login_required
@csrf_exempt
def addcreditstowalletexecute(request,amount):
    if request.method == 'POST':
        success = False
        User = get_user_model()
        user = User.objects.get(username=request.user.username)
        payment = paypalrestsdk.Payment.find(request.POST['paymentID'])
        if payment.execute({'payer_id' : request.POST['payerID']}):            
            finalusercredits = math.floor((float(user.credits)+float(amount))*100)/100
            user.credits = finalusercredits
            user.save()
            success = True
        else:
            success = False
        return JsonResponse({'success' : success})
    else:
        return render(request, 'payments/addcredits.html')

@login_required
def walletpaymentprocessing(request):
    return render(request, 'payments/walletpaymentprocessing.html')

@login_required
def downloadaudio(request):
    if request.method == 'POST':
        filename = request.POST.get('filename')
        s3 = boto3.client('s3', aws_access_key_id='YOUR ACCESS KEY ID', aws_secret_access_key='YOUR ACCESS SECRET KEY')
        file_and_path = settings.MEDIA_ROOT+'/deliveredorderstemp/'+filename
        s3.download_file('letstranscriptfileuploads', filename, file_and_path)
        with open(file_and_path, 'rb') as f:
            userorderdownload = f.read()
        os.remove(file_and_path)
        response = HttpResponse(userorderdownload, content_type='multipart/mixed')
        response['Content-Disposition'] = "%sfilename=%s" % ('attachment;', filename)
        return response
    else:
        return render(request, 'users/downloadaudio.html')

# def accountactivation(request):
#     if request.method == 'POST':
#         to_email = request.POST.get('email')
#         try:
#             User = get_user_model()
#             user = User.objects.get(email=to_email)
#         except(TypeError, ValueError, OverflowError, User.DoesNotExist):
#             user = None
#         if user is not None:
#             # site = get_current_site(request)
#             message = render_to_string('users/account_activation.html', {
#                     'user':user, 'domain':'letstranscript.com',
#                     'uid': urlsafe_base64_encode(force_bytes(user.pk)),
#                     'token': account_activation_token.make_token(user),
#                 })
#             mail_subject = 'Please confirm your LetsTranscript account.'
#             email = EmailMessage(mail_subject, message, to=[to_email])
#             email.content_subtype = "html"
#             email.send()
#             messages.success(request, 'Thankyou for requesting email confirmation. If this user exists, a confirmation email will be sent with activation instructions.')
#             return render(request, 'users/requestaccountactivation.html')
#         else:
#             messages.success(request, 'Thankyou for requesting email confirmation. If this user exists, a confirmation email will be sent with activation instructions.')
#             return render(request, 'users/requestaccountactivation.html')
#     else:
#         return render(request, 'users/requestaccountactivation.html',{'title':'Request account activation'})

# def activate(request, uidb64, token):
#     try:
#         User = get_user_model()
#         uid = force_text(urlsafe_base64_decode(uidb64))
#         user = User.objects.get(pk=uid)
#     except(TypeError, ValueError, OverflowError, User.DoesNotExist):
#         user = None
#     if user is not None and account_activation_token.check_token(user, token):
#         user.is_active = True
#         user.email_verified = True
#         user.save()
#         messages.success(request, 'Thank you for your email confirmation. You will now be able to login!')
#         return redirect('login')
#     else:
#         return HttpResponse('Activation link is invalid!')