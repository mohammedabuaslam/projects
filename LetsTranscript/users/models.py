from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.contrib.auth.models import User
from django.utils import timezone

PREMIUM_CHOICES = (
    ('basic','Basic'),
    ('standard','Standard'),
    ('premium','Premium'),
    ('enterprise','Enterprise'),
)

ORDER_STATUSES = (
    ('processing','processing'),
    ('completed','completed'),

)
PAYMENT_STATUSES = (
    ('pending','pending'),
    ('paid','paid'),

)

class MyValidator(UnicodeUsernameValidator):
    regex = r'^[\w.@+\- ]+$'

class User(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)
    phone = models.CharField(max_length=15, blank=True)
    country = models.CharField(max_length=50, blank=True)
    first_name = None
    last_name = None
    username_validator = MyValidator()
    username = models.CharField(_('username'),max_length=50,unique=True,help_text=_('Username must be 50 characters or fewer. Letters, digits and @/./+/-/_ only.'),validators=[username_validator],error_messages={'unique': _("A user with that username already exists."),},)
    email_verified = models.BooleanField(default=False)
    is_postpaid = models.BooleanField(default=False)
    credits = models.CharField(max_length=12, blank=True, default=0)
    referredby = models.CharField(max_length=100, blank=True)

class Orders(models.Model):
    uniqueordertracker = models.CharField(max_length=100, default='uniqueordertracker')
    ordername = models.CharField(max_length=200)
    totalminutecount = models.CharField(max_length=10)
    orderstatus = models.CharField(max_length=16, default="processing", choices=ORDER_STATUSES)
    paymentstatus = models.CharField(max_length=20, default="pending payment", choices=PAYMENT_STATUSES)
    ordervalue = models.CharField(max_length=12)
    transcriptiontype = models.CharField(max_length=30,default='Human-Generated')
    turnaroundtime = models.CharField(max_length=10,default='3 Days')
    verbatimtype = models.CharField(max_length=15,default='Clean Verbatim')
    subtitles = models.CharField(max_length=6,default='No')
    foreignsubtitles = models.CharField(max_length=6,default='No')
    noofspeakers = models.CharField(max_length=3,default='2')
    comments = models.TextField(blank=True, null=True)
    humangeneratedlanguage = models.CharField(max_length=8,default='en-us')
    automatedlanguage = models.CharField(max_length=8,default='en-us')
    foriegnsubtitlelanguage = models.CharField(max_length=8,default='en-us')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)
    displayfields = ['ordername', 'uniqueordertracker','totalminutecount', 'author', 'orderstatus','paymentstatus','date_posted']
    filterfields = ['uniqueordertracker','orderstatus','paymentstatus','author','date_posted']

    def __str__(self):
        return self.ordername