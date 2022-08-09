from django.db import models
from django.utils import timezone
from django.urls import reverse
from ckeditor.fields import RichTextField
from main.models import Sitemaps
# from django.db.models import Q

bloguploads = 'blog/img/blogimages/'
NICHE_CHOICES = (
    ('transcription','Transcription'),
    ('podcasting','Podcasting'),
    ('captions-&-subtitles','Captions & Subtitles'),
    ('seo','SEO'),
    ('marketresearch','Market Research'),
)

def makurl(changeit):
    tempo = changeit.lower().replace(' ','-')
    sitema = Sitemaps()
    creatingsitemap = '/blog/'+str(tempo)
    sitema.sitemapurl = creatingsitemap
    if Sitemaps.objects.filter(sitemapurl=creatingsitemap).exists():
        pass
    else:
        sitema.save()
    return tempo



class blog(models.Model):
    metatitle = models.CharField(max_length=100)
    metadescription = models.CharField(max_length=160)
    metakeywords = models.CharField(max_length=160)
    niche = models.CharField(max_length=60, choices=NICHE_CHOICES, default='Uncategorized')
    image = models.ImageField(upload_to= bloguploads, null=False, blank=False)
    coverimage = models.ImageField(upload_to= bloguploads, null=True, blank=True)
    title = models.CharField(max_length=100)
    shortdescription = models.CharField(max_length=200, default='')
    url = models.CharField(max_length=100, null=True, blank=True, editable=False)
    content = RichTextField(blank=False, null=False)
    covercontent = RichTextField(blank=True, null=True)
    sitemap_url = models.CharField(max_length=350, editable=False)
    date_posted = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'blogs'
    

    def save(self, *args, **kwargs):
        self.url = makurl(self.title)
        super(blog, self).save(*args, **kwargs)

    def __str__(self):
        return self.title