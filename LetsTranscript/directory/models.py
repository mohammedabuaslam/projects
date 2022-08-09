from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField


class Directory(models.Model):
    companyname = models.CharField(max_length=150, null=True, blank=True)
    letsranking = models.CharField(max_length=4,null=True,blank=True,default=9999)
    rating = models.CharField(max_length=150, null=True, blank=True)
    reviewcount = models.CharField(max_length=150, null=True, blank=True)
    industry = models.CharField(max_length=150, null=True, blank=True)
    address = models.CharField(max_length=250, null=True, blank=True)
    city = models.CharField(max_length=150, null=True, blank=True)
    state = models.CharField(max_length=150, null=True, blank=True)
    country = models.CharField(max_length=150, null=True, blank=True)
    experience = models.CharField(max_length=150, null=True, blank=True)
    website = models.CharField(max_length=150, null=True, blank=True)
    reltype = models.CharField(max_length=30,null=True,blank=True)
    phone = models.CharField(max_length=150, null=True, blank=True)
    uniqueid = models.CharField(max_length=30,null=True,blank=True)
    metatitle = models.CharField(max_length=60,null=True,blank=True)
    metadescription = models.CharField(max_length=160,null=True,blank=True)
    metakeywords = models.CharField(max_length=160,null=True,blank=True)
    pagedescription = RichTextField(blank=True, null=True)
    logourl = models.CharField(blank=True, null=True, max_length=200)
    displayfields = ['companyname','rating','reviewcount','industry','address','city','state','country','experience','website','phone']
    filterfields = ['companyname','rating','reviewcount','industry','address','city','state','country','experience','website','phone']

    def __str__(self):
        return self.companyname

class Sidelinks(models.Model):
    industry = models.CharField(max_length=150, null=True, blank=True)
    url = models.CharField(max_length=250, null=True, blank=True)

    displayfields = ['industry','url']
    filterfields = ['industry','url']

    def __str__(self):
        return self.url