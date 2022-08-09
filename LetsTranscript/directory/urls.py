from django.urls import path
from . import views as dir_views
from django.urls import path


urlpatterns = [
	path('usa/transcription-services/<str:location>/', dir_views.transcriptionservices.as_view(), name='transcriptionservices'),
	path('usa/transcription-services/', dir_views.transcriptionservicesusa.as_view(), name='transcriptionservicesusa'),

	path('usa/court-reporter/<str:location>/', dir_views.courtreporter.as_view(), name='courtreporter'),
	path('usa/hr-consulting/<str:location>/', dir_views.hrconsulting.as_view(), name='hrconsulting'),
	path('usa/legal-services/<str:location>/', dir_views.legalservices.as_view(), name='legalservices'),
	path('usa/medical-billing-companies/<str:location>/', dir_views.medicalbillingcompanies.as_view(), name='medicalbillingcompanies'),
	path('usa/medical-transcription-services/<str:location>/', dir_views.medicaltranscriptionservices.as_view(), name='medicaltranscriptionservices'),
	path('usa/private-investigators/<str:location>/', dir_views.privateinvestigators.as_view(), name='privateinvestigators'),
	path('usa/recording-studios/<str:location>/', dir_views.recordingstudios.as_view(), name='recordingstudios'),



	path('usa/translation-companies/<str:location>/', dir_views.translationcompanies.as_view(), name='translationcompanies'), # pending



	path('usa/video-production-companies/<str:location>/', dir_views.videoproductioncompanies.as_view(), name='videoproductioncompanies'),
	path('usa/market-research/<str:location>/', dir_views.marketresearch.as_view(), name='marketresearch'),
	path('usa/media-agencies/<str:location>/', dir_views.mediaagencies.as_view(), name='mediaagencies'),
]


	# path('usa/transcription-services/alabama/', dir_views.transcriptionservicesalabama.as_view(), name='transcriptionservicesalabama'),
	# path('usa/transcription-services/alaska/', dir_views.transcriptionservicesalaska.as_view(), name='transcriptionservicesalaska'),
	# path('usa/transcription-services/arizona/', dir_views.transcriptionservicesarizona.as_view(), name='transcriptionservicesarizona'),
	# path('usa/transcription-services/arkansas/', dir_views.transcriptionservicesarkansas.as_view(), name='transcriptionservicesarkansas'),
	# path('usa/transcription-services/california/', dir_views.transcriptionservicescalifornia.as_view(), name='transcriptionservicescalifornia'),
	# path('usa/transcription-services/colorado/', dir_views.transcriptionservicescolorado.as_view(), name='transcriptionservicescolorado'),
	# path('usa/transcription-services/connecticut/', dir_views.transcriptionservicesconnecticut.as_view(), name='transcriptionservicesconnecticut'),
	# path('usa/transcription-services/delaware/', dir_views.transcriptionservicesdelaware.as_view(), name='transcriptionservicesdelaware'),
	# path('usa/transcription-services/florida/', dir_views.transcriptionservicesflorida.as_view(), name='transcriptionservicesflorida'),
	# path('usa/transcription-services/georgia/', dir_views.transcriptionservicesgeorgia.as_view(), name='transcriptionservicesgeorgia'),
	# path('usa/transcription-services/hawaii/', dir_views.transcriptionserviceshawaii.as_view(), name='transcriptionserviceshawaii'),
	# path('usa/transcription-services/idaho/', dir_views.transcriptionservicesidaho.as_view(), name='transcriptionservicesidaho'),
	# path('usa/transcription-services/illinois/', dir_views.transcriptionservicesillinois.as_view(), name='transcriptionservicesillinois'),
	# path('usa/transcription-services/indiana/', dir_views.transcriptionservicesindiana.as_view(), name='transcriptionservicesindiana'),
	# path('usa/transcription-services/iowa/', dir_views.transcriptionservicesiowa.as_view(), name='transcriptionservicesiowa'),
	# path('usa/transcription-services/kansas/', dir_views.transcriptionserviceskansas.as_view(), name='transcriptionserviceskansas'),
	# path('usa/transcription-services/kentucky/', dir_views.transcriptionserviceskentucky.as_view(), name='transcriptionserviceskentucky'),
	# path('usa/transcription-services/louisiana/', dir_views.transcriptionserviceslouisiana.as_view(), name='transcriptionserviceslouisiana'),
	# path('usa/transcription-services/maine/', dir_views.transcriptionservicesmaine.as_view(), name='transcriptionservicesmaine'),
	# path('usa/transcription-services/maryland/', dir_views.transcriptionservicesmaryland.as_view(), name='transcriptionservicesmaryland'),
	# path('usa/transcription-services/massachusetts/', dir_views.transcriptionservicesmassachusetts.as_view(), name='transcriptionservicesmassachusetts'),
	# path('usa/transcription-services/michigan/', dir_views.transcriptionservicesmichigan.as_view(), name='transcriptionservicesmichigan'),
	# path('usa/transcription-services/minnesota/', dir_views.transcriptionservicesminnesota.as_view(), name='transcriptionservicesminnesota'),
	# path('usa/transcription-services/mississippi/', dir_views.transcriptionservicesmississippi.as_view(), name='transcriptionservicesmississippi'),
	# path('usa/transcription-services/missouri/', dir_views.transcriptionservicesmissouri.as_view(), name='transcriptionservicesmissouri'),
	# path('usa/transcription-services/montana/', dir_views.transcriptionservicesmontana.as_view(), name='transcriptionservicesmontana'),
	# path('usa/transcription-services/nebraska/', dir_views.transcriptionservicesnebraska.as_view(), name='transcriptionservicesnebraska'),
	# path('usa/transcription-services/nevada/', dir_views.transcriptionservicesnevada.as_view(), name='transcriptionservicesnevada'),
	# path('usa/transcription-services/new-hampshire/', dir_views.transcriptionservicesnewhampshire.as_view(), name='transcriptionservicesnewhampshire'),
	# path('usa/transcription-services/new-jersey/', dir_views.transcriptionservicesnewjersey.as_view(), name='transcriptionservicesnewjersey'),
	# path('usa/transcription-services/new-mexico/', dir_views.transcriptionservicesnewmexico.as_view(), name='transcriptionservicesnewmexico'),
	# path('usa/transcription-services/<str:location>/', dir_views.transcriptionservicesnewyork.as_view(), name='transcriptionservicesnewyork'),
	# path('usa/transcription-services/north-carolina/', dir_views.transcriptionservicesnorthcarolina.as_view(), name='transcriptionservicesnorthcarolina'),
	# path('usa/transcription-services/north-dakota/', dir_views.transcriptionservicesnorthdakota.as_view(), name='transcriptionservicesnorthdakota'),
	# path('usa/transcription-services/ohio/', dir_views.transcriptionservicesohio.as_view(), name='transcriptionservicesohio'),
	# path('usa/transcription-services/oklahoma/', dir_views.transcriptionservicesoklahoma.as_view(), name='transcriptionservicesoklahoma'),
	# path('usa/transcription-services/oregon/', dir_views.transcriptionservicesoregon.as_view(), name='transcriptionservicesoregon'),
	# path('usa/transcription-services/pennsylvania/', dir_views.transcriptionservicespennsylvania.as_view(), name='transcriptionservicespennsylvania'),
	# path('usa/transcription-services/rhode-island/', dir_views.transcriptionservicesrhodeisland.as_view(), name='transcriptionservicesrhodeisland'),
	# path('usa/transcription-services/south-carolina/', dir_views.transcriptionservicessouthcarolina.as_view(), name='transcriptionservicessouthcarolina'),
	# path('usa/transcription-services/south-dakota/', dir_views.transcriptionservicessouthdakota.as_view(), name='transcriptionservicessouthdakota'),
	# path('usa/transcription-services/tennessee/', dir_views.transcriptionservicestennessee.as_view(), name='transcriptionservicestennessee'),
	# path('usa/transcription-services/texas/', dir_views.transcriptionservicestexas.as_view(), name='transcriptionservicestexas'),
	# path('usa/transcription-services/utah/', dir_views.transcriptionservicesutah.as_view(), name='transcriptionservicesutah'),
	# path('usa/transcription-services/vermont/', dir_views.transcriptionservicesvermont.as_view(), name='transcriptionservicesvermont'),
	# path('usa/transcription-services/virginia/', dir_views.transcriptionservicesvirginia.as_view(), name='transcriptionservicesvirginia'),
	# path('usa/transcription-services/washington/', dir_views.transcriptionserviceswashington.as_view(), name='transcriptionserviceswashington'),
	# path('usa/transcription-services/west-virginia/', dir_views.transcriptionserviceswestvirginia.as_view(), name='transcriptionserviceswestvirginia'),
	# path('usa/transcription-services/wisconsin/', dir_views.transcriptionserviceswisconsin.as_view(), name='transcriptionserviceswisconsin'),
	# path('usa/transcription-services/wyoming/', dir_views.transcriptionserviceswyoming.as_view(), name='transcriptionserviceswyoming'),