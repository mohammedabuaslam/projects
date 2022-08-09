from django.db import models
from django.urls import reverse
from django.utils import timezone

class Sitemaps(models.Model):
    sitemapurl = models.CharField(max_length=300)
    priority = models.CharField(max_length=6, default=1.00)
    changefrequency = models.CharField(max_length=20,default='daily')
    date_posted = models.DateTimeField(default=timezone.now,null=True)

    def get_absolute_url(self):
        return self.sitemapurl

class Firms(models.Model):
    companyname = models.CharField(max_length=100,default='')
    website = models.CharField(max_length=100,default='')
    rating = models.CharField(max_length=100,default='')
    phone = models.CharField(max_length=20,default='')
    service = models.CharField(max_length=100,default='')
    address = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=100, default='')
    category = models.CharField(max_length=100,default='')
    
    def __str__(self):
        return self.companyname