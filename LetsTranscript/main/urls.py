from django.urls import path
from . import views as main_views
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from django.contrib.sitemaps.views import sitemap
from .sitemaps import sendsitemap
from django.conf import settings

sitemaps = {
    'posts': sendsitemap
}

urlpatterns = [
 path('', main_views.Homepage, name='homepage'),
 path('cost-estimator/', main_views.costestimator, name='cost-estimator'),
 path('transcription-services/', main_views.humangeneratedtranscription, name='humangeneratedtranscription'),
 path('services/', main_views.services, name='services'),
 path('dissertation-transcription/', main_views.dissertationtranscription, name='dissertationtranscription'),
 path('automated-transcription-services/', main_views.automatedtranscription, name='automatedtranscription'),
 path('captions/', main_views.captionsandsubtitles, name='captionsandsubtitles'),
 path('about/', main_views.about, name='about'),
 path('frequently-asked-questions/', main_views.faqs, name='frequently-asked-questions'),
 path('contact/', main_views.contactus, name='contact-us'),
 path('legal-transcription/', main_views.legaltranscription, name='legaltranscription'),
 path('academic-transcription/', main_views.academictranscription, name='academictranscription'),
 path('medical-transcription/', main_views.medicaltranscription, name='medicaltranscription'),
 path('investigation-transcription/', main_views.investigationtranscription, name='investigationtranscription'),
 path('media-transcription/', main_views.mediatranscription, name='mediatranscription'),
 path('deposition-transcription/', main_views.depositiontranscription, name='depositiontranscription'),
 path('audio-video-transcription-services-convert-mp3-mp4-to-text/', main_views.AudioVideoTranscriptionServicesConvertMp3Mp4toText, name='AudioVideoTranscriptionServicesConvertMp3Mp4toText'),
 path('terms-of-service/', main_views.termsofservice, name='termsofservice'),
 path('privacy-policy/', main_views.privacypolicy, name='privacypolicy'),
 path('cancellations/', main_views.cancellations, name='cancellations'),
 path('shipping-policy/', main_views.shippingpolicy, name='shippingpolicy'),
 path('robots.txt/', main_views.robots, name='robots'),
 path('sitemap.xml/', sitemap, {'sitemaps' : sitemaps }, name='sitemap'),
 path('companies/p/<city>/', main_views.companysites.as_view(), name='companysites'),
 path('sitemap/', main_views.sitemap.as_view(), name='sitemap'),
 path('templates/', main_views.templates, name='templates'),
 path('captioning-subtitling-wistia-videos/', main_views.wistiavideos, name='wistiavideos'),
 path('vimeo-video-subtitle-captioning-video-marketing/', main_views.vimeovideos, name='vimeovideos'),
 path('ooyala-video-subtitle-captioning-video-marketing/', main_views.ooyalavideos, name='ooyalavideos'),
]
