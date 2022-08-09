from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_GET
from django.http import HttpResponse
from .models import Sitemaps, Firms
from LetsTranscript import settings
from django.contrib import messages
import requests, json
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.views.generic import (ListView)

def contactus(request):
	if request.method == 'POST':
		clientkey = request.POST['g-recaptcha-response']
		secretkey = 'YOUR SECRET KEY'
		captchadata = {
		'secret':secretkey,
		'response':clientkey
		}
		r = requests.post('https://www.google.com/recaptcha/api/siteverify',data=captchadata)
		response = json.loads(r.text)
		if response['success'] == True:
			name = request.POST.get('name')
			email = request.POST.get('email')
			phone = request.POST.get('phone')
			country = request.POST.get('country')
			companyname = request.POST.get('companyname')
			subject = request.POST.get('subject')
			messagecontent = request.POST.get('message')

			message = render_to_string('main/sendleademail.html',{'name': name,'email': email,'phone': phone,'country': country,'companyname': companyname,'subject': subject,'messagecontent': messagecontent})
			mail_subject = 'LetsTranscript Lead from - ' + str(email)
			email = EmailMessage(mail_subject, message, to=['YOUR EMAIL'])
			email.content_subtype = "html"
			email.send()

			messages.success(request, 'We have recieved your request and one of our associate will get in touch with you within 24 Hours.')
		if response['success'] == False:
			messages.warning(request,'Please verify the captcha before you submit the form.')
		return render(request, 'main/contactus.html')
	else:
		return render(request, 'main/contactus.html')

def Homepage(request):
	return render(request, 'main/index.html',{'title':'Transcription Services - Speech to Text | Video Captions'})

class companysites(ListView):
    model = Firms
    template_name = 'companies/companies.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 20

    def get_queryset(self):
        res = get_object_or_404(Firms, location=self.kwargs.get('uniqueid'))
        return Firms.objects.filter(location=self.kwargs.get('uniqueid'))

def costestimator(request):
	return render(request, 'main/cost-estimator.html',{'title':'Transcription Services Cost - Price | Rates ($0.80/ Minute)'})

def templates(request):
	return render(request, 'main/templates.html')

def humangeneratedtranscription(request):
	return render(request, 'main/humangeneratedtranscription.html',{'title':'Accurate Transcription Services - Proofread | Delivered ($0.80)'})

def services(request):
	return render(request, 'main/services.html',{'title':'Services - LetsTranscript'})

def automatedtranscription(request):
	return render(request, 'main/automatedtranscription.html',{'title':'Automated Transcription Software - Video | Subtitles | Captions'})

def captionsandsubtitles(request):
	return render(request, 'main/captionsandsubtitles.html',{'title':'Video Editing - Subtitles | Closed-caption | SRT File ($0.80)'})

def foreignsubtitles(request):
	return render(request, 'main/foreignsubtitles.html',{'title':'Foreign Subtitles - Global Audience - Translate'})

def about(request):
	return render(request, 'main/about.html',{'title':'About Us - LetsTranscript'})

def transcriptionsamples(request):
	return render(request, 'main/transcriptionsamples.html',{'title':'Transcription Samples'})

def faqs(request):
	return render(request, 'main/faqs.html',{'title':'Frequently Asked Questions - Transcription - LetsTranscript'})

def calltranscription(request):
	return render(request, 'main/calltranscription.html',{'title':'Call Transcription Services - LetsTranscript'})

def legaltranscription(request):
	return render(request, 'main/legaltranscription.html',{'title':'Legal Transcription Services - Attorney | Paralegal | Court'})

def academictranscription(request):
	return render(request, 'main/academictranscription.html',{'title':'Academic Transcription Services - LetsTranscript ($0.80/min)'})

def financialtranscription(request):
	return render(request, 'main/financialtranscription.html',{'title':'Financial Transcription'})

def interviewtranscription(request):
	return render(request, 'main/interviewtranscription.html',{'title':'Interview Transcription Services - LetsTranscript'})

def investigationtranscription(request):
	return render(request, 'main/investigationtranscription.html',{'title':'Private Investigator - Investigation Transcription Services'})

def mediatranscription(request):
	return render(request, 'main/mediatranscription.html',{'title':'Media Transcription Services - LetsTranscript ($0.80/Minute)'})

def depositiontranscription(request):
	return render(request, 'main/depositiontranscription.html',{'title':'Deposition Transcription Services - Court Reporter | Legal'})

def AudioVideoTranscriptionServicesConvertMp3Mp4toText(request):
	return render(request, 'main/AudioVideoTranscriptionServicesConvertMp3Mp4toText.html',{'title':'Audio/Video Transcription Services - Convert Mp3, Mp4 to Text'})

def termsofservice(request):
	return render(request, 'main/termsofservice.html',{'title':'Terms & Conditions'})

def privacypolicy(request):
	return render(request, 'main/privacypolicy.html',{'title':'Privacy Policy'})

def cancellations(request):
	return render(request, 'main/cancellations.html',{'title':'Cancellation Policy'})

def shippingpolicy(request):
	return render(request, 'main/shippingpolicy.html',{'title':'Shipping Policy'})

def medicaltranscription(request):
	return render(request, 'main/medicaltranscription.html',{'title':'Medical Transcription Services - Physician | Billing ($0.80/min)'})

def podcasttranscription(request):
	return render(request, 'main/podcasttranscription.html',{'title':'Podcast Transcription Services - $0.1/Minute'})

def documenttranslation(request):
	return render(request, 'main/documenttranslation.html',{'title':'Document Translation'})

def qualitativeresearch(request):
	return render(request, 'main/qualitativeresearch.html',{'title':'Qualitative Research'})

def dissertationtranscription(request):
	return render(request, 'main/dissertationtranscription.html',{'title':'Dissertation Transcription - Interview, Research, PhD'})

def wistiavideos(request):
	return render(request, 'main/wistiavideos.html',{'title':'Wistia - Video Subtitle | Captioning - Video Marketing'})

def vimeovideos(request):
	return render(request, 'main/vimeovideos.html',{'title':'Vimeo - Video Subtitle | Captioning - Video Marketing'})

def ooyalavideos(request):
	return render(request, 'main/ooyalavideos.html',{'title':'Ooyala - Video Subtitle | Captioning - Video Marketing'})

class sitemap(ListView):
    model = Sitemaps
    template_name = 'main/sitemap.html'
    context_object_name = "posts"
    ordering = ['-date_posted']
    paginate_by = 50000

@require_GET
def robots(request):
	lines = [
		"Sitemap: https://www.letstranscript.com/sitemap.xml",
		"User-Agent: *",
		"Allow: /",
	]
	return HttpResponse("\n".join(lines), content_type='text/plain')