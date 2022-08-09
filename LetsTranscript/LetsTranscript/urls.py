from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = 'LetsTranscript Administration'
handler404 = 'users.views.handler404'
handler403 = 'users.views.handler403'
handler500 = 'users.views.handler500'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    path('users/', include('users.urls')),
    path('directory/', include('directory.urls')),
    path('', include('main.urls')),
    path('accounts/', include('allauth.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)