from django.contrib.sitemaps import Sitemap
from .models import Sitemaps as ss
from django.urls import reverse

class sendsitemap(Sitemap):
    changefreq = "monthly"
    protocol = 'https'

    def items(self):
        return ss.objects.all()

    def priority(self, obj):
        return obj.priority