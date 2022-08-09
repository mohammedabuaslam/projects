from django.shortcuts import render, get_object_or_404
from .models import Directory, Sidelinks
from django.views.generic import (ListView)
from django.db.models import Q
import random

# =========================================================================
# TRANSCRIPTION SERVICES LOCATIONS
# =========================================================================

class transcriptionservicesusa(ListView):
    model = Directory
    template_name = 'directory/transcriptionservicesusa.html'
    context_object_name = "posts"
    paginate_by = 10
    
    def get_queryset(self):
        fetcher = Directory.objects.filter(industry='Transcription service').order_by('-rating')
        return fetcher
    
    def get_context_data(self, **kwargs):
        context = super(transcriptionservicesusa, self).get_context_data(**kwargs)
        context['location'] = "USA"
        context['title'] = 'Transcription Companies in USA - LetsTranscript | $0.80/Min'
        sysreq = Sidelinks.objects.filter(industry='Transcription service').values_list("url", flat=True)
        temp = list(sysreq)
        sendthis = random.sample(temp, 25)
        context['sidelinks'] = sendthis
        return context

class transcriptionservices(ListView):
    model = Directory
    template_name = 'directory/transcriptionservices.html'
    context_object_name = "posts"
    paginate_by = 10
    
    def get_queryset(self):
        fetcher = Directory.objects.filter(state=self.kwargs.get('location'), industry='Transcription service').order_by('-rating')
        return fetcher
    
    def get_context_data(self, **kwargs):
        context = super(transcriptionservices, self).get_context_data(**kwargs)
        context['location'] = self.kwargs.get('location').replace('-', ' ')
        context['title'] = 'Transcription Companies in '+ self.kwargs.get('location').replace('-', ' ') +' - LetsTranscript | $0.80/Min'
        sysreq = Sidelinks.objects.filter(industry='Transcription service').values_list("url", flat=True)
        temp = list(sysreq)
        try:
            sendthis = random.sample(temp, 15)
        except:
            sendthis = random.sample(temp, len(temp))
        context['sidelinks'] = sendthis
        return context

# =========================================================================
# COURT REPORTERS LOCATIONS
# =========================================================================

class courtreporter(ListView):
    model = Directory
    template_name = 'directory/courtreporter.html'
    context_object_name = 'posts'
    paginate_by = 10

    def get_queryset(self):
    	fetcher = Directory.objects.filter(state=self.kwargs.get('location'), industry='Court reporter').order_by('-rating')
    	return fetcher

    def get_context_data(self, **kwargs):
        context = super(courtreporter, self).get_context_data(**kwargs)
        context['location'] = self.kwargs.get('location').replace('-', ' ')
        context['title'] = 'Court Reporters in '+self.kwargs.get('location').replace('-', ' ') + ' - LetsTranscript | $0.80/Min'
        sysreq = Sidelinks.objects.filter(industry='Court reporter').values_list("url", flat=True)
        temp = list(sysreq)
        sendthis = random.sample(temp, 15)
        context['sidelinks'] = sendthis
        return context

class hrconsulting(ListView):
    model = Directory
    template_name = 'directory/hrconsulting.html'
    context_object_name = 'posts'
    paginate_by = 10

    def get_queryset(self):
        fetcher = Directory.objects.filter(state=self.kwargs.get('location'), industry='Human resource consulting').order_by('-rating')
        return fetcher

    def get_context_data(self, **kwargs):
        context = super(hrconsulting, self).get_context_data(**kwargs)
        context['location'] = self.kwargs.get('location').replace('-', ' ')
        context['title'] = 'HR Consultants in '+self.kwargs.get('location').replace('-', ' ') + ' - LetsTranscript | $0.80/Min'
        sysreq = Sidelinks.objects.filter(industry='Human resource consulting').values_list("url", flat=True)
        temp = list(sysreq)
        sendthis = random.sample(temp, 15)
        context['sidelinks'] = sendthis
        return context

class legalservices(ListView):
    model = Directory
    template_name = 'directory/legalservices.html'
    context_object_name = 'posts'
    paginate_by = 10

    def get_queryset(self):
        fetcher = Directory.objects.filter(state=self.kwargs.get('location'), industry='Legal services').order_by('-rating')
        return fetcher

    def get_context_data(self, **kwargs):
        context = super(legalservices, self).get_context_data(**kwargs)
        context['location'] = self.kwargs.get('location').replace('-', ' ')
        context['title'] = 'Legal Services in '+self.kwargs.get('location').replace('-', ' ') + ' - LetsTranscript | $0.80/Min'
        sysreq = Sidelinks.objects.filter(industry='Legal services').values_list("url", flat=True)
        temp = list(sysreq)
        sendthis = random.sample(temp, 15)
        context['sidelinks'] = sendthis
        return context

class marketresearch(ListView):
    model = Directory
    template_name = 'directory/marketresearcher.html'
    context_object_name = 'posts'
    paginate_by = 10

    def get_queryset(self):
        fetcher = Directory.objects.filter(state=self.kwargs.get('location'), industry='Market researcher').order_by('-rating')
        return fetcher

    def get_context_data(self, **kwargs):
        context = super(marketresearch, self).get_context_data(**kwargs)
        context['location'] = self.kwargs.get('location').replace('-', ' ')
        context['title'] = 'Market Research Companies in '+self.kwargs.get('location').replace('-', ' ') + ' - LetsTranscript | $0.80/Min'
        sysreq = Sidelinks.objects.filter(industry='Market researcher').values_list("url", flat=True)
        temp = list(sysreq)
        sendthis = random.sample(temp, 15)
        context['sidelinks'] = sendthis
        return context

class mediaagencies(ListView):
    model = Directory
    template_name = 'directory/mediacompany.html'
    context_object_name = 'posts'
    paginate_by = 10

    def get_queryset(self):
        fetcher = Directory.objects.filter(state=self.kwargs.get('location'), industry='Media company').order_by('-rating')
        return fetcher

    def get_context_data(self, **kwargs):
        context = super(mediaagencies, self).get_context_data(**kwargs)
        context['location'] = self.kwargs.get('location').replace('-', ' ')
        context['title'] = 'Media Agencies in '+self.kwargs.get('location').replace('-', ' ') + ' - LetsTranscript | $0.80/Min'
        sysreq = Sidelinks.objects.filter(industry='Media company').values_list("url", flat=True)
        temp = list(sysreq)
        sendthis = random.sample(temp, 15)
        context['sidelinks'] = sendthis
        return context

class medicalbillingcompanies(ListView):
    model = Directory
    template_name = 'directory/medicalbillingcompanies.html'
    context_object_name = 'posts'
    paginate_by = 10

    def get_queryset(self):
        fetcher = Directory.objects.filter(state=self.kwargs.get('location'), industry='Medical billing service').order_by('-rating')
        return fetcher

    def get_context_data(self, **kwargs):
        context = super(medicalbillingcompanies, self).get_context_data(**kwargs)
        context['location'] = self.kwargs.get('location').replace('-', ' ')
        context['title'] = 'Medical Billing Companies in '+self.kwargs.get('location').replace('-', ' ') + ' - LetsTranscript | $0.80/Min'
        sysreq = Sidelinks.objects.filter(industry='Medical billing service').values_list("url", flat=True)
        temp = list(sysreq)
        sendthis = random.sample(temp, 15)
        context['sidelinks'] = sendthis
        return context

class medicaltranscriptionservices(ListView):
    model = Directory
    template_name = 'directory/medicaltranscriptionservices.html'
    context_object_name = 'posts'
    paginate_by = 10

    def get_queryset(self):
        fetcher = Directory.objects.filter(state=self.kwargs.get('location'), industry='Medical transcription service').order_by('-rating')
        return fetcher

    def get_context_data(self, **kwargs):
        context = super(medicaltranscriptionservices, self).get_context_data(**kwargs)
        context['location'] = self.kwargs.get('location').replace('-', ' ')
        context['title'] = 'Medical Transcription Services in '+self.kwargs.get('location').replace('-', ' ') + ' - LetsTranscript | $0.80/Min'
        sysreq = Sidelinks.objects.filter(industry='Medical transcription service').values_list("url", flat=True)
        temp = list(sysreq)
        sendthis = random.sample(temp, 15)
        context['sidelinks'] = sendthis
        return context

class privateinvestigators(ListView):
    model = Directory
    template_name = 'directory/privateinvestigators.html'
    context_object_name = 'posts'
    paginate_by = 10

    def get_queryset(self):
        fetcher = Directory.objects.filter(state=self.kwargs.get('location'), industry='Private investigator').order_by('-rating')
        return fetcher

    def get_context_data(self, **kwargs):
        context = super(privateinvestigators, self).get_context_data(**kwargs)
        context['location'] = self.kwargs.get('location').replace('-', ' ')
        context['title'] = 'Private Investigators in '+self.kwargs.get('location').replace('-', ' ') + ' - LetsTranscript | $0.80/Min'
        sysreq = Sidelinks.objects.filter(industry='Private investigator').values_list("url", flat=True)
        temp = list(sysreq)
        sendthis = random.sample(temp, 15)
        context['sidelinks'] = sendthis
        return context

class recordingstudios(ListView):
    model = Directory
    template_name = 'directory/recordingstudios.html'
    context_object_name = 'posts'
    paginate_by = 10

    def get_queryset(self):
        fetcher = Directory.objects.filter(state=self.kwargs.get('location'), industry='Recording studio').order_by('-rating')
        return fetcher

    def get_context_data(self, **kwargs):
        context = super(recordingstudios, self).get_context_data(**kwargs)
        context['location'] = self.kwargs.get('location').replace('-', ' ')
        context['title'] = 'Recording Studios in '+self.kwargs.get('location').replace('-', ' ') + ' - LetsTranscript | $0.80/Min'
        sysreq = Sidelinks.objects.filter(industry='Recording studio').values_list("url", flat=True)
        temp = list(sysreq)
        sendthis = random.sample(temp, 4)
        context['sidelinks'] = sendthis
        return context

class translationcompanies(ListView):
    model = Directory
    template_name = 'directory/translationcompanies.html'
    context_object_name = 'posts'
    paginate_by = 10

    def get_queryset(self):
        fetcher = Directory.objects.filter(state=self.kwargs.get('location'), industry='Translator').order_by('-rating')
        return fetcher

    def get_context_data(self, **kwargs):
        context = super(translationcompanies, self).get_context_data(**kwargs)
        context['location'] = self.kwargs.get('location').replace('-', ' ')
        context['title'] = 'Translation Companies in '+self.kwargs.get('location').replace('-', ' ') + ' - LetsTranscript | $0.80/Min'
        sysreq = Sidelinks.objects.filter(industry='Translator').values_list("url", flat=True)
        temp = list(sysreq)
        sendthis = random.sample(temp, 15)
        context['sidelinks'] = sendthis
        return context

class videoproductioncompanies(ListView):
    model = Directory
    template_name = 'directory/videoproductioncompanies.html'
    context_object_name = 'posts'
    paginate_by = 10

    def get_queryset(self):
        fetcher = Directory.objects.filter(state=self.kwargs.get('location'), industry='Video production service').order_by('-rating')
        return fetcher

    def get_context_data(self, **kwargs):
        context = super(videoproductioncompanies, self).get_context_data(**kwargs)
        context['location'] = self.kwargs.get('location').replace('-', ' ')
        context['title'] = 'Video Production Companies in '+self.kwargs.get('location').replace('-', ' ') + ' - LetsTranscript | $0.80/Min'
        sysreq = Sidelinks.objects.filter(industry='Transcription service').values_list("url", flat=True)
        temp = list(sysreq)
        sendthis = random.sample(temp, 15)
        context['sidelinks'] = sendthis
        return context

class marketresearch(ListView):
    model = Directory
    template_name = 'directory/marketresearcher.html'
    context_object_name = 'posts'
    paginate_by = 10

    def get_queryset(self):
        fetcher = Directory.objects.filter(state=self.kwargs.get('location'), industry='Market researcher').order_by('-rating')
        return fetcher

    def get_context_data(self, **kwargs):
        context = super(marketresearch, self).get_context_data(**kwargs)
        context['location'] = self.kwargs.get('location').replace('-', ' ')
        context['title'] = 'Market research in '+self.kwargs.get('location').replace('-', ' ') + ' - LetsTranscript | $0.80/Min'
        sysreq = Sidelinks.objects.filter(industry='Video production service').values_list("url", flat=True)
        temp = list(sysreq)
        sendthis = random.sample(temp, 15)
        context['sidelinks'] = sendthis
        return context

class mediaagencies(ListView):
    model = Directory
    template_name = 'directory/mediacompany.html'
    context_object_name = 'posts'
    paginate_by = 10

    def get_queryset(self):
        fetcher = Directory.objects.filter(state=self.kwargs.get('location'), industry='Media company').order_by('-rating')
        return fetcher

    def get_context_data(self, **kwargs):
        context = super(mediaagencies, self).get_context_data(**kwargs)
        context['location'] = self.kwargs.get('location').replace('-', ' ')
        context['title'] = 'Media Agencies in '+self.kwargs.get('location').replace('-', ' ') + ' - LetsTranscript | $0.80/Min'
        sysreq = Sidelinks.objects.filter(industry='Media company').values_list("url", flat=True)
        temp = list(sysreq)
        sendthis = random.sample(temp, 15)
        context['sidelinks'] = sendthis
        return context

# class transcriptionservicesalabama(ListView):
#     model = Directory
#     template_name = 'directory/transcription/transcriptionservicesalabama.html'
#     context_object_name = "posts"
#     paginate_by = 10
    
#     def get_queryset(self):
#         fetcher = Directory.objects.filter(state="alabama", industry='Transcription service').order_by('-rating')
#         return fetcher
    
#     def get_context_data(self, **kwargs):
#         context = super(transcriptionservicesalabama, self).get_context_data(**kwargs)
#         context['location'] = "alabama"
#         context['title'] = 'Transcription Companies in Alabama - LetsTranscript | $0.80/Min'
#         return context

# class transcriptionservicesalaska(ListView):
#     model = Directory
#     template_name = 'directory/transcription/transcriptionservicesalaska.html'
#     context_object_name = "posts"
#     paginate_by = 10
    
#     def get_queryset(self):
#         fetcher = Directory.objects.filter(state="alaska", industry='Transcription service').order_by('-rating')
#         return fetcher
    
#     def get_context_data(self, **kwargs):
#         context = super(transcriptionservicesalaska, self).get_context_data(**kwargs)
#         context['location'] = "alaska"
#         context['title'] = 'Transcription Companies in Alaska - LetsTranscript | $0.80/Min'
#         return context

# class transcriptionservicesarizona(ListView):
#     model = Directory
#     template_name = 'directory/transcription/transcriptionservicesarizona.html'
#     context_object_name = "posts"
#     paginate_by = 10
    
#     def get_queryset(self):
#         fetcher = Directory.objects.filter(state="arizona", industry='Transcription service').order_by('-rating')
#         return fetcher
    
#     def get_context_data(self, **kwargs):
#         context = super(transcriptionservicesarizona, self).get_context_data(**kwargs)
#         context['location'] = "arizona"
#         context['title'] = 'Transcription Companies in Arizona - LetsTranscript | $0.80/Min'
#         return context

# class transcriptionservicesarkansas(ListView):
#     model = Directory
#     template_name = 'directory/transcription/transcriptionservicesarkansas.html'
#     context_object_name = "posts"
#     paginate_by = 10
    
#     def get_queryset(self):
#         fetcher = Directory.objects.filter(state="arkansas", industry='Transcription service').order_by('-rating')
#         return fetcher
    
#     def get_context_data(self, **kwargs):
#         context = super(transcriptionservicesarkansas, self).get_context_data(**kwargs)
#         context['location'] = "arkansas"
#         context['title'] = 'Transcription Companies in Arkansas - LetsTranscript | $0.80/Min'
#         return context

# class transcriptionservicescalifornia(ListView):
#     model = Directory
#     template_name = 'directory/transcription/transcriptionservicescalifornia.html'
#     context_object_name = "posts"
#     paginate_by = 10
    
#     def get_queryset(self):
#         fetcher = Directory.objects.filter(state="california", industry='Transcription service').order_by('-rating')
#         return fetcher
    
#     def get_context_data(self, **kwargs):
#         context = super(transcriptionservicescalifornia, self).get_context_data(**kwargs)
#         context['location'] = "california"
#         context['title'] = 'Transcription Companies in California - LetsTranscript | $0.80/Min'
#         return context

# class transcriptionservicescolorado(ListView):
#     model = Directory
#     template_name = 'directory/transcription/transcriptionservicescolorado.html'
#     context_object_name = "posts"
#     paginate_by = 10
    
#     def get_queryset(self):
#         fetcher = Directory.objects.filter(state="colorado", industry='Transcription service').order_by('-rating')
#         return fetcher
    
#     def get_context_data(self, **kwargs):
#         context = super(transcriptionservicescolorado, self).get_context_data(**kwargs)
#         context['location'] = "colorado"
#         context['title'] = 'Transcription Companies in Colorado - LetsTranscript | $0.80/Min'
#         return context

# class transcriptionservicesconnecticut(ListView):
#     model = Directory
#     template_name = 'directory/transcription/transcriptionservicesconnecticut.html'
#     context_object_name = "posts"
#     paginate_by = 10
    
#     def get_queryset(self):
#         fetcher = Directory.objects.filter(state="connecticut", industry='Transcription service').order_by('-rating')
#         return fetcher
    
#     def get_context_data(self, **kwargs):
#         context = super(transcriptionservicesconnecticut, self).get_context_data(**kwargs)
#         context['location'] = "connecticut"
#         context['title'] = 'Transcription Companies in Connecticut - LetsTranscript | $0.80/Min'
#         return context

# class transcriptionservicesdelaware(ListView):
#     model = Directory
#     template_name = 'directory/transcription/transcriptionservicesdelaware.html'
#     context_object_name = "posts"
#     paginate_by = 10
    
#     def get_queryset(self):
#         fetcher = Directory.objects.filter(state="delaware", industry='Transcription service').order_by('-rating')
#         return fetcher
    
#     def get_context_data(self, **kwargs):
#         context = super(transcriptionservicesdelaware, self).get_context_data(**kwargs)
#         context['location'] = "delaware"
#         context['title'] = 'Transcription Companies in Delaware - LetsTranscript | $0.80/Min'
#         return context

# class transcriptionservicesflorida(ListView):
#     model = Directory
#     template_name = 'directory/transcription/transcriptionservicesflorida.html'
#     context_object_name = "posts"
#     paginate_by = 10
    
#     def get_queryset(self):
#         fetcher = Directory.objects.filter(state="florida", industry='Transcription service').order_by('-rating')
#         return fetcher
    
#     def get_context_data(self, **kwargs):
#         context = super(transcriptionservicesflorida, self).get_context_data(**kwargs)
#         context['location'] = "florida"
#         context['title'] = 'Transcription Companies in Florida - LetsTranscript | $0.80/Min'
#         return context

# class transcriptionservicesgeorgia(ListView):
#     model = Directory
#     template_name = 'directory/transcription/transcriptionservicesgeorgia.html'
#     context_object_name = "posts"
#     paginate_by = 10
    
#     def get_queryset(self):
#         fetcher = Directory.objects.filter(state="georgia", industry='Transcription service').order_by('-rating')
#         return fetcher
    
#     def get_context_data(self, **kwargs):
#         context = super(transcriptionservicesgeorgia, self).get_context_data(**kwargs)
#         context['location'] = "georgia"
#         context['title'] = 'Transcription Companies in Georgia - LetsTranscript | $0.80/Min'
#         return context

# class transcriptionserviceshawaii(ListView):
#     model = Directory
#     template_name = 'directory/transcription/transcriptionserviceshawaii.html'
#     context_object_name = "posts"
#     paginate_by = 10
    
#     def get_queryset(self):
#         fetcher = Directory.objects.filter(state="hawaii", industry='Transcription service').order_by('-rating')
#         return fetcher
    
#     def get_context_data(self, **kwargs):
#         context = super(transcriptionserviceshawaii, self).get_context_data(**kwargs)
#         context['location'] = "hawaii"
#         context['title'] = 'Transcription Companies in Hawaii - LetsTranscript | $0.80/Min'
#         return context

# class transcriptionservicesidaho(ListView):
#     model = Directory
#     template_name = 'directory/transcription/transcriptionservicesidaho.html'
#     context_object_name = "posts"
#     paginate_by = 10
    
#     def get_queryset(self):
#         fetcher = Directory.objects.filter(state="idaho", industry='Transcription service').order_by('-rating')
#         return fetcher
    
#     def get_context_data(self, **kwargs):
#         context = super(transcriptionservicesidaho, self).get_context_data(**kwargs)
#         context['location'] = "idaho"
#         context['title'] = 'Transcription Companies in Idaho - LetsTranscript | $0.80/Min'
#         return context

# class transcriptionservicesillinois(ListView):
#     model = Directory
#     template_name = 'directory/transcription/transcriptionservicesillinois.html'
#     context_object_name = "posts"
#     paginate_by = 10
    
#     def get_queryset(self):
#         fetcher = Directory.objects.filter(state="illinois", industry='Transcription service').order_by('-rating')
#         return fetcher
    
#     def get_context_data(self, **kwargs):
#         context = super(transcriptionservicesillinois, self).get_context_data(**kwargs)
#         context['location'] = "illinois"
#         context['title'] = 'Transcription Companies in Illinois - LetsTranscript | $0.80/Min'
#         return context

# class transcriptionservicesindiana(ListView):
#     model = Directory
#     template_name = 'directory/transcription/transcriptionservicesindiana.html'
#     context_object_name = "posts"
#     paginate_by = 10
    
#     def get_queryset(self):
#         fetcher = Directory.objects.filter(state="indiana", industry='Transcription service').order_by('-rating')
#         return fetcher
    
#     def get_context_data(self, **kwargs):
#         context = super(transcriptionservicesindiana, self).get_context_data(**kwargs)
#         context['location'] = "indiana"
#         context['title'] = 'Transcription Companies in Indiana - LetsTranscript | $0.80/Min'
#         return context

# class transcriptionservicesiowa(ListView):
#     model = Directory
#     template_name = 'directory/transcription/transcriptionservicesiowa.html'
#     context_object_name = "posts"
#     paginate_by = 10
    
#     def get_queryset(self):
#         fetcher = Directory.objects.filter(state="iowa", industry='Transcription service').order_by('-rating')
#         return fetcher
    
#     def get_context_data(self, **kwargs):
#         context = super(transcriptionservicesiowa, self).get_context_data(**kwargs)
#         context['location'] = "iowa"
#         context['title'] = 'Transcription Companies in Iowa - LetsTranscript | $0.80/Min'
#         return context

# class transcriptionserviceskansas(ListView):
#     model = Directory
#     template_name = 'directory/transcription/transcriptionserviceskansas.html'
#     context_object_name = "posts"
#     paginate_by = 10
    
#     def get_queryset(self):
#         fetcher = Directory.objects.filter(state="kansas", industry='Transcription service').order_by('-rating')
#         return fetcher
    
#     def get_context_data(self, **kwargs):
#         context = super(transcriptionserviceskansas, self).get_context_data(**kwargs)
#         context['location'] = "kansas"
#         context['title'] = 'Transcription Companies in Kansas - LetsTranscript | $0.80/Min'
#         return context

# class transcriptionserviceskentucky(ListView):
#     model = Directory
#     template_name = 'directory/transcription/transcriptionserviceskentucky.html'
#     context_object_name = "posts"
#     paginate_by = 10
    
#     def get_queryset(self):
#         fetcher = Directory.objects.filter(state="kentucky", industry='Transcription service').order_by('-rating')
#         return fetcher
    
#     def get_context_data(self, **kwargs):
#         context = super(transcriptionserviceskentucky, self).get_context_data(**kwargs)
#         context['location'] = "kentucky"
#         context['title'] = 'Transcription Companies in Kentucky - LetsTranscript | $0.80/Min'
#         return context

# class transcriptionserviceslouisiana(ListView):
#     model = Directory
#     template_name = 'directory/transcription/transcriptionserviceslouisiana.html'
#     context_object_name = "posts"
#     paginate_by = 10
    
#     def get_queryset(self):
#         fetcher = Directory.objects.filter(state="louisiana", industry='Transcription service').order_by('-rating')
#         return fetcher
    
#     def get_context_data(self, **kwargs):
#         context = super(transcriptionserviceslouisiana, self).get_context_data(**kwargs)
#         context['location'] = "louisiana"
#         context['title'] = 'Transcription Companies in Louisiana - LetsTranscript | $0.80/Min'
#         return context

# class transcriptionservicesmaine(ListView):
#     model = Directory
#     template_name = 'directory/transcription/transcriptionservicesmaine.html'
#     context_object_name = "posts"
#     paginate_by = 10
    
#     def get_queryset(self):
#         fetcher = Directory.objects.filter(state="maine", industry='Transcription service').order_by('-rating')
#         return fetcher
    
#     def get_context_data(self, **kwargs):
#         context = super(transcriptionservicesmaine, self).get_context_data(**kwargs)
#         context['location'] = "maine"
#         context['title'] = 'Transcription Companies in Maine - LetsTranscript | $0.80/Min'
#         return context

# class transcriptionservicesmaryland(ListView):
#     model = Directory
#     template_name = 'directory/transcription/transcriptionservicesmaryland.html'
#     context_object_name = "posts"
#     paginate_by = 10
    
#     def get_queryset(self):
#         fetcher = Directory.objects.filter(state="maryland", industry='Transcription service').order_by('-rating')
#         return fetcher
    
#     def get_context_data(self, **kwargs):
#         context = super(transcriptionservicesmaryland, self).get_context_data(**kwargs)
#         context['location'] = "maryland"
#         context['title'] = 'Transcription Companies in Maryland - LetsTranscript | $0.80/Min'
#         return context

# class transcriptionservicesmassachusetts(ListView):
#     model = Directory
#     template_name = 'directory/transcription/transcriptionservicesmassachusetts.html'
#     context_object_name = "posts"
#     paginate_by = 10
    
#     def get_queryset(self):
#         fetcher = Directory.objects.filter(state="massachusetts", industry='Transcription service').order_by('-rating')
#         return fetcher
    
#     def get_context_data(self, **kwargs):
#         context = super(transcriptionservicesmassachusetts, self).get_context_data(**kwargs)
#         context['location'] = "massachusetts"
#         context['title'] = 'Transcription Companies in Massachusetts - LetsTranscript | $0.80/Min'
#         return context

# class transcriptionservicesmichigan(ListView):
#     model = Directory
#     template_name = 'directory/transcription/transcriptionservicesmichigan.html'
#     context_object_name = "posts"
#     paginate_by = 10
    
#     def get_queryset(self):
#         fetcher = Directory.objects.filter(state="michigan", industry='Transcription service').order_by('-rating')
#         return fetcher
    
#     def get_context_data(self, **kwargs):
#         context = super(transcriptionservicesmichigan, self).get_context_data(**kwargs)
#         context['location'] = "michigan"
#         context['title'] = 'Transcription Companies in Michigan - LetsTranscript | $0.80/Min'
#         return context

# class transcriptionservicesminnesota(ListView):
#     model = Directory
#     template_name = 'directory/transcription/transcriptionservicesminnesota.html'
#     context_object_name = "posts"
#     paginate_by = 10
    
#     def get_queryset(self):
#         fetcher = Directory.objects.filter(state="minnesota", industry='Transcription service').order_by('-rating')
#         return fetcher
    
#     def get_context_data(self, **kwargs):
#         context = super(transcriptionservicesminnesota, self).get_context_data(**kwargs)
#         context['location'] = "minnesota"
#         context['title'] = 'Transcription Companies in Minnesota - LetsTranscript | $0.80/Min'
#         return context

# class transcriptionservicesmississippi(ListView):
#     model = Directory
#     template_name = 'directory/transcription/transcriptionservicesmississippi.html'
#     context_object_name = "posts"
#     paginate_by = 10
    
#     def get_queryset(self):
#         fetcher = Directory.objects.filter(state="mississippi", industry='Transcription service').order_by('-rating')
#         return fetcher
    
#     def get_context_data(self, **kwargs):
#         context = super(transcriptionservicesmississippi, self).get_context_data(**kwargs)
#         context['location'] = "mississippi"
#         context['title'] = 'Transcription Companies in Mississippi - LetsTranscript | $0.80/Min'
#         return context

# class transcriptionservicesmissouri(ListView):
#     model = Directory
#     template_name = 'directory/transcription/transcriptionservicesmissouri.html'
#     context_object_name = "posts"
#     paginate_by = 10
    
#     def get_queryset(self):
#         fetcher = Directory.objects.filter(state="missouri", industry='Transcription service').order_by('-rating')
#         return fetcher
    
#     def get_context_data(self, **kwargs):
#         context = super(transcriptionservicesmissouri, self).get_context_data(**kwargs)
#         context['location'] = "missouri"
#         context['title'] = 'Transcription Companies in Missouri - LetsTranscript | $0.80/Min'
#         return context

# class transcriptionservicesmontana(ListView):
#     model = Directory
#     template_name = 'directory/transcription/transcriptionservicesmontana.html'
#     context_object_name = "posts"
#     paginate_by = 10
    
#     def get_queryset(self):
#         fetcher = Directory.objects.filter(state="montana", industry='Transcription service').order_by('-rating')
#         return fetcher
    
#     def get_context_data(self, **kwargs):
#         context = super(transcriptionservicesmontana, self).get_context_data(**kwargs)
#         context['location'] = "montana"
#         context['title'] = 'Transcription Companies in Montana - LetsTranscript | $0.80/Min'
#         return context

# class transcriptionservicesnebraska(ListView):
#     model = Directory
#     template_name = 'directory/transcription/transcriptionservicesnebraska.html'
#     context_object_name = "posts"
#     paginate_by = 10
    
#     def get_queryset(self):
#         fetcher = Directory.objects.filter(state="nebraska", industry='Transcription service').order_by('-rating')
#         return fetcher
    
#     def get_context_data(self, **kwargs):
#         context = super(transcriptionservicesnebraska, self).get_context_data(**kwargs)
#         context['location'] = "nebraska"
#         context['title'] = 'Transcription Companies in Nebraska - LetsTranscript | $0.80/Min'
#         return context

# class transcriptionservicesnevada(ListView):
#     model = Directory
#     template_name = 'directory/transcription/transcriptionservicesnevada.html'
#     context_object_name = "posts"
#     paginate_by = 10
    
#     def get_queryset(self):
#         fetcher = Directory.objects.filter(state="nevada", industry='Transcription service').order_by('-rating')
#         return fetcher
    
#     def get_context_data(self, **kwargs):
#         context = super(transcriptionservicesnevada, self).get_context_data(**kwargs)
#         context['location'] = "nevada"
#         context['title'] = 'Transcription Companies in Nevada - LetsTranscript | $0.80/Min'
#         return context

# class transcriptionservicesnewhampshire(ListView):
#     model = Directory
#     template_name = 'directory/transcription/transcriptionservicesnewhampshire.html'
#     context_object_name = "posts"
#     paginate_by = 10
    
#     def get_queryset(self):
#         fetcher = Directory.objects.filter(state="new-hampshire", industry='Transcription service').order_by('-rating')
#         return fetcher
    
#     def get_context_data(self, **kwargs):
#         context = super(transcriptionservicesnewhampshire, self).get_context_data(**kwargs)
#         context['location'] = "new hampshire"
#         context['title'] = 'Transcription Companies in New Hampshire - LetsTranscript | $0.80/Min'
#         return context

# class transcriptionservicesnewjersey(ListView):
#     model = Directory
#     template_name = 'directory/transcription/transcriptionservicesnewjersey.html'
#     context_object_name = "posts"
#     paginate_by = 10
    
#     def get_queryset(self):
#         fetcher = Directory.objects.filter(state="new-jersey", industry='Transcription service').order_by('-rating')
#         return fetcher
    
#     def get_context_data(self, **kwargs):
#         context = super(transcriptionservicesnewjersey, self).get_context_data(**kwargs)
#         context['location'] = "new jersey"
#         context['title'] = 'Transcription Companies in New Jersey - LetsTranscript | $0.80/Min'
#         return context

# class transcriptionservicesnewmexico(ListView):
#     model = Directory
#     template_name = 'directory/transcription/transcriptionservicesnewmexico.html'
#     context_object_name = "posts"
#     paginate_by = 10
    
#     def get_queryset(self):
#         fetcher = Directory.objects.filter(state="new-mexico", industry='Transcription service').order_by('-rating')
#         return fetcher
    
#     def get_context_data(self, **kwargs):
#         context = super(transcriptionservicesnewmexico, self).get_context_data(**kwargs)
#         context['location'] = "new mexico"
#         context['title'] = 'Transcription Companies in New Mexico - LetsTranscript | $0.80/Min'
#         return context

# class transcriptionservicesnewyork(ListView):
#     model = Directory
#     template_name = 'directory/transcription/transcriptionservicesnewyork.html'
#     context_object_name = "posts"
#     paginate_by = 10
    
#     def get_queryset(self):
#         fetcher = Directory.objects.filter(state="new-york", industry='Transcription service').order_by('-rating')
#         return fetcher
    
#     def get_context_data(self, **kwargs):
#         context = super(transcriptionservicesnewyork, self).get_context_data(**kwargs)
#         context['location'] = "new york"
#         context['title'] = 'Transcription Companies in New York - LetsTranscript | $0.80/Min'
#         context['testing']
#         return context

# class transcriptionservicesnorthcarolina(ListView):
#     model = Directory
#     template_name = 'directory/transcription/transcriptionservicesnorthcarolina.html'
#     context_object_name = "posts"
#     paginate_by = 10
    
#     def get_queryset(self):
#         fetcher = Directory.objects.filter(state="north-carolina", industry='Transcription service').order_by('-rating')
#         return fetcher
    
#     def get_context_data(self, **kwargs):
#         context = super(transcriptionservicesnorthcarolina, self).get_context_data(**kwargs)
#         context['location'] = "north carolina"
#         context['title'] = 'Transcription Companies in North Carolina - LetsTranscript | $0.80/Min'
#         return context

# class transcriptionservicesnorthdakota(ListView):
#     model = Directory
#     template_name = 'directory/transcription/transcriptionservicesnorthdakota.html'
#     context_object_name = "posts"
#     paginate_by = 10
    
#     def get_queryset(self):
#         fetcher = Directory.objects.filter(state="north-dakota", industry='Transcription service').order_by('-rating')
#         return fetcher
    
#     def get_context_data(self, **kwargs):
#         context = super(transcriptionservicesnorthdakota, self).get_context_data(**kwargs)
#         context['location'] = "north dakota"
#         context['title'] = 'Transcription Companies in North Dakota - LetsTranscript | $0.80/Min'
#         return context

# class transcriptionservicesohio(ListView):
#     model = Directory
#     template_name = 'directory/transcription/transcriptionservicesohio.html'
#     context_object_name = "posts"
#     paginate_by = 10
    
#     def get_queryset(self):
#         fetcher = Directory.objects.filter(state="ohio", industry='Transcription service').order_by('-rating')
#         return fetcher
    
#     def get_context_data(self, **kwargs):
#         context = super(transcriptionservicesohio, self).get_context_data(**kwargs)
#         context['location'] = "ohio"
#         context['title'] = 'Transcription Companies in Ohio - LetsTranscript | $0.80/Min'
#         return context

# class transcriptionservicesoklahoma(ListView):
#     model = Directory
#     template_name = 'directory/transcription/transcriptionservicesoklahoma.html'
#     context_object_name = "posts"
#     paginate_by = 10
    
#     def get_queryset(self):
#         fetcher = Directory.objects.filter(state="oklahoma", industry='Transcription service').order_by('-rating')
#         return fetcher
    
#     def get_context_data(self, **kwargs):
#         context = super(transcriptionservicesoklahoma, self).get_context_data(**kwargs)
#         context['location'] = "oklahoma"
#         context['title'] = 'Transcription Companies in Oklahoma - LetsTranscript | $0.80/Min'
#         return context

# class transcriptionservicesoregon(ListView):
#     model = Directory
#     template_name = 'directory/transcription/transcriptionservicesoregon.html'
#     context_object_name = "posts"
#     paginate_by = 10
    
#     def get_queryset(self):
#         fetcher = Directory.objects.filter(state="oregon", industry='Transcription service').order_by('-rating')
#         return fetcher
    
#     def get_context_data(self, **kwargs):
#         context = super(transcriptionservicesoregon, self).get_context_data(**kwargs)
#         context['location'] = "oregon"
#         context['title'] = 'Transcription Companies in Oregon - LetsTranscript | $0.80/Min'
#         return context

# class transcriptionservicespennsylvania(ListView):
#     model = Directory
#     template_name = 'directory/transcription/transcriptionservicespennsylvania.html'
#     context_object_name = "posts"
#     paginate_by = 10
    
#     def get_queryset(self):
#         fetcher = Directory.objects.filter(state="pennsylvania", industry='Transcription service').order_by('-rating')
#         return fetcher
    
#     def get_context_data(self, **kwargs):
#         context = super(transcriptionservicespennsylvania, self).get_context_data(**kwargs)
#         context['location'] = "pennsylvania"
#         context['title'] = 'Transcription Companies in Pennsylvania - LetsTranscript | $0.80/Min'
#         return context

# class transcriptionservicesrhodeisland(ListView):
#     model = Directory
#     template_name = 'directory/transcription/transcriptionservicesrhodeisland.html'
#     context_object_name = "posts"
#     paginate_by = 10
    
#     def get_queryset(self):
#         fetcher = Directory.objects.filter(state="rhode-island", industry='Transcription service').order_by('-rating')
#         return fetcher
    
#     def get_context_data(self, **kwargs):
#         context = super(transcriptionservicesrhodeisland, self).get_context_data(**kwargs)
#         context['location'] = "Rhode Island"
#         context['title'] = 'Transcription Companies in Rhode Island - LetsTranscript | $0.80/Min'
#         return context

# class transcriptionservicessouthcarolina(ListView):
#     model = Directory
#     template_name = 'directory/transcription/transcriptionservicessouthcarolina.html'
#     context_object_name = "posts"
#     paginate_by = 10
    
#     def get_queryset(self):
#         fetcher = Directory.objects.filter(state="south-carolina", industry='Transcription service').order_by('-rating')
#         return fetcher
    
#     def get_context_data(self, **kwargs):
#         context = super(transcriptionservicessouthcarolina, self).get_context_data(**kwargs)
#         context['location'] = "south carolina"
#         context['title'] = 'Transcription Companies in South Carolina - LetsTranscript | $0.80/Min'
#         return context

# class transcriptionservicessouthdakota(ListView):
#     model = Directory
#     template_name = 'directory/transcription/transcriptionservicessouthdakota.html'
#     context_object_name = "posts"
#     paginate_by = 10
    
#     def get_queryset(self):
#         fetcher = Directory.objects.filter(state="south-dakota", industry='Transcription service').order_by('-rating')
#         return fetcher
    
#     def get_context_data(self, **kwargs):
#         context = super(transcriptionservicessouthdakota, self).get_context_data(**kwargs)
#         context['location'] = "south dakota"
#         context['title'] = 'Transcription Companies in South Dakota - LetsTranscript | $0.80/Min'
#         return context

# class transcriptionservicestennessee(ListView):
#     model = Directory
#     template_name = 'directory/transcription/transcriptionservicestennessee.html'
#     context_object_name = "posts"
#     paginate_by = 10
    
#     def get_queryset(self):
#         fetcher = Directory.objects.filter(state="tennessee", industry='Transcription service').order_by('-rating')
#         return fetcher
    
#     def get_context_data(self, **kwargs):
#         context = super(transcriptionservicestennessee, self).get_context_data(**kwargs)
#         context['location'] = "tennessee"
#         context['title'] = 'Transcription Companies in Tennessee - LetsTranscript | $0.80/Min'
#         return context

# class transcriptionservicestexas(ListView):
#     model = Directory
#     template_name = 'directory/transcription/transcriptionservicestexas.html'
#     context_object_name = "posts"
#     paginate_by = 10
    
#     def get_queryset(self):
#         fetcher = Directory.objects.filter(state="texas", industry='Transcription service').order_by('-rating')
#         return fetcher
    
#     def get_context_data(self, **kwargs):
#         context = super(transcriptionservicestexas, self).get_context_data(**kwargs)
#         context['location'] = "texas"
#         context['title'] = 'Transcription Companies in Texas - LetsTranscript | $0.80/Min'
#         return context

# class transcriptionservicesutah(ListView):
#     model = Directory
#     template_name = 'directory/transcription/transcriptionservicesutah.html'
#     context_object_name = "posts"
#     paginate_by = 10
    
#     def get_queryset(self):
#         fetcher = Directory.objects.filter(state="utah", industry='Transcription service').order_by('-rating')
#         return fetcher
    
#     def get_context_data(self, **kwargs):
#         context = super(transcriptionservicesutah, self).get_context_data(**kwargs)
#         context['location'] = "utah"
#         context['title'] = 'Transcription Companies in Utah - LetsTranscript | $0.80/Min'
#         return context

# class transcriptionservicesvermont(ListView):
#     model = Directory
#     template_name = 'directory/transcription/transcriptionservicesvermont.html'
#     context_object_name = "posts"
#     paginate_by = 10
    
#     def get_queryset(self):
#         fetcher = Directory.objects.filter(state="vermont", industry='Transcription service').order_by('-rating')
#         return fetcher
    
#     def get_context_data(self, **kwargs):
#         context = super(transcriptionservicesvermont, self).get_context_data(**kwargs)
#         context['location'] = "vermont"
#         context['title'] = 'Transcription Companies in Vermont - LetsTranscript | $0.80/Min'
#         return context

# class transcriptionservicesvirginia(ListView):
#     model = Directory
#     template_name = 'directory/transcription/transcriptionservicesvirginia.html'
#     context_object_name = "posts"
#     paginate_by = 10
    
#     def get_queryset(self):
#         fetcher = Directory.objects.filter(state="virginia", industry='Transcription service').order_by('-rating')
#         return fetcher
    
#     def get_context_data(self, **kwargs):
#         context = super(transcriptionservicesvirginia, self).get_context_data(**kwargs)
#         context['location'] = "virginia"
#         context['title'] = 'Transcription Companies in Virginia - LetsTranscript | $0.80/Min'
#         return context

# class transcriptionserviceswashington(ListView):
#     model = Directory
#     template_name = 'directory/transcription/transcriptionserviceswashington.html'
#     context_object_name = "posts"
#     paginate_by = 10
    
#     def get_queryset(self):
#         fetcher = Directory.objects.filter(state="washington", industry='Transcription service').order_by('-rating')
#         return fetcher
    
#     def get_context_data(self, **kwargs):
#         context = super(transcriptionserviceswashington, self).get_context_data(**kwargs)
#         context['location'] = "washington"
#         context['title'] = 'Transcription Companies in Washington - LetsTranscript | $0.80/Min'
#         return context

# class transcriptionserviceswestvirginia(ListView):
#     model = Directory
#     template_name = 'directory/transcription/transcriptionserviceswestvirginia.html'
#     context_object_name = "posts"
#     paginate_by = 10
    
#     def get_queryset(self):
#         fetcher = Directory.objects.filter(state="west-virginia", industry='Transcription service').order_by('-rating')
#         return fetcher
    
#     def get_context_data(self, **kwargs):
#         context = super(transcriptionserviceswestvirginia, self).get_context_data(**kwargs)
#         context['location'] = "west virginia"
#         context['title'] = 'Transcription Companies in West Virginia - LetsTranscript | $0.80/Min'
#         return context

# class transcriptionserviceswisconsin(ListView):
#     model = Directory
#     template_name = 'directory/transcription/transcriptionserviceswisconsin.html'
#     context_object_name = "posts"
#     paginate_by = 10
    
#     def get_queryset(self):
#         fetcher = Directory.objects.filter(state="wisconsin", industry='Transcription service').order_by('-rating')
#         return fetcher
    
#     def get_context_data(self, **kwargs):
#         context = super(transcriptionserviceswisconsin, self).get_context_data(**kwargs)
#         context['location'] = "wisconsin"
#         context['title'] = 'Transcription Companies in Wisconsin - LetsTranscript | $0.80/Min'
#         return context

# class transcriptionserviceswyoming(ListView):
#     model = Directory
#     template_name = 'directory/transcription/transcriptionserviceswyoming.html'
#     context_object_name = "posts"
#     paginate_by = 10
    
#     def get_queryset(self):
#         fetcher = Directory.objects.filter(state="wyoming", industry='Transcription service').order_by('-rating')
#         return fetcher
    
#     def get_context_data(self, **kwargs):
#         context = super(transcriptionserviceswyoming, self).get_context_data(**kwargs)
#         context['location'] = "wyoming"
#         context['title'] = 'Transcription Companies in Wyoming - LetsTranscript | $0.80/Min'
#         return context

















# =========================================================================

