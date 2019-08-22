from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse
#from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set or Users must have an email address.')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, username="", **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    """User model."""

    username = None
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email_confirmed = models.BooleanField(default=False)
    # other fields...

    def __str__(self):
        return str(self.id) + ' - ' + str(self.user_id) + ' - ' + str(self.email_confirmed)

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()


class NewLeads(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=True)
    custName = models.CharField(max_length=250,blank=True)
    mobile = models.CharField(max_length=25,blank=True)
    alternate_mobile = models.CharField(max_length=25,blank=True)
    email = models.CharField(max_length=250,blank=True)
    address = models.TextField(max_length=500,blank=True)
    area = models.CharField(max_length=250,blank=True)
    city = models.CharField(max_length=250,blank=True)
    zipcode = models.CharField(max_length=250,blank=True)
    state = models.CharField(max_length=250,blank=True)
    plan = models.CharField(max_length=100,blank=True)
    leadStatus = models.CharField(max_length=25,default='New')
    leadType = models.CharField(max_length=250,blank=True)
    pointOfContact = models.CharField(max_length=250,blank=True)
    enquiryDate = models.DateTimeField(auto_now=True)
    leadSource = models.CharField(max_length=250,blank=True)
    currentStatus = models.CharField(max_length=100,blank=True)
    latestUpdate = models.TextField(max_length=500,blank=True)
    utm_source = models.CharField(max_length=250,blank=True)
    utm_campaign = models.CharField(max_length=250,blank=True)


class ColdLeads(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=True)
    lead = models.ForeignKey(NewLeads,on_delete=models.CASCADE)
    custName = models.CharField(max_length=250,blank=True)
    mobile = models.CharField(max_length=25,blank=True)
    alternate_mobile = models.CharField(max_length=25,blank=True)
    email = models.CharField(max_length=250,blank=True)
    address = models.TextField(max_length=500,blank=True)
    area = models.CharField(max_length=250,blank=True)
    city = models.CharField(max_length=250,blank=True)
    zipcode = models.CharField(max_length=250,blank=True)
    state = models.CharField(max_length=250,blank=True)
    plan = models.CharField(max_length=100,blank=True)
    leadStatus = models.CharField(max_length=25,default='Cold')
    leadType = models.CharField(max_length=250,blank=True)
    pointOfContact = models.CharField(max_length=250,blank=True)
    enquiryDate = models.DateTimeField(blank=True)
    coldDate = models.DateTimeField(auto_now=True)
    leadSource = models.CharField(max_length=250,blank=True)
    currentStatus = models.CharField(max_length=100,blank=True)
    latestUpdate = models.TextField(max_length=500,blank=True)

class ConvertedLeads(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=True)
    lead = models.ForeignKey(NewLeads,on_delete=models.CASCADE)
    custName = models.CharField(max_length=250,blank=True)
    mobile = models.CharField(max_length=25,blank=True)
    alternate_mobile = models.CharField(max_length=25,blank=True)
    email = models.CharField(max_length=250,blank=True)
    address = models.TextField(max_length=500,blank=True)
    area = models.CharField(max_length=250,blank=True)
    city = models.CharField(max_length=250,blank=True)
    zipcode = models.CharField(max_length=250,blank=True)
    state = models.CharField(max_length=250,blank=True)
    plan = models.CharField(max_length=100,blank=True)
    leadStatus = models.CharField(max_length=25,default='Converted')
    pointOfContact = models.CharField(max_length=250,blank=True)
    convertedDate = models.DateTimeField(auto_now=True)
    leadSource = models.CharField(max_length=250,blank=True)
    currentStatus = models.CharField(max_length=100,default='Active')
    latestUpdate = models.TextField(max_length=500,blank=True)


class InstalledLeads(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=True)
    lead = models.ForeignKey(NewLeads,on_delete=models.CASCADE)
    custName = models.CharField(max_length=250, blank=True)
    mobile = models.CharField(max_length=25, blank=True)
    alternate_mobile = models.CharField(max_length=25, blank=True)
    email = models.CharField(max_length=250, blank=True)
    address = models.TextField(max_length=500, blank=True)
    area = models.CharField(max_length=250, blank=True)
    city = models.CharField(max_length=250, blank=True)
    zipcode = models.CharField(max_length=250, blank=True)
    state = models.CharField(max_length=250, blank=True)
    plan = models.CharField(max_length=100, blank=True)
    leadStatus = models.CharField(max_length=25, default='Installed')
    pointOfContact = models.CharField(max_length=250, blank=True)
    installationDate = models.DateTimeField(auto_now=True)
    leadSource = models.CharField(max_length=250, blank=True)
    currentStatus = models.CharField(max_length=100, blank=True)
    purifierId = models.CharField(max_length=15,blank=True)
    technician = models.CharField(max_length=250,blank=True)
    latestUpdate = models.TextField(max_length=500, blank=True)

class ScheduledLeads(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=True)
    lead = models.ForeignKey(NewLeads,on_delete=models.CASCADE)
    custName = models.CharField(max_length=250, blank=True)
    mobile = models.CharField(max_length=25, blank=True)
    alternate_mobile = models.CharField(max_length=25, blank=True)
    email = models.CharField(max_length=250, blank=True)
    address = models.TextField(max_length=500, blank=True)
    area = models.CharField(max_length=250, blank=True)
    city = models.CharField(max_length=250, blank=True)
    zipcode = models.CharField(max_length=250, blank=True)
    state = models.CharField(max_length=250, blank=True)
    plan = models.CharField(max_length=100, blank=True)
    leadStatus = models.CharField(max_length=25, default='Scheduled')
    pointOfContact = models.CharField(max_length=250, blank=True)
    scheduledDate = models.DateTimeField(auto_now=True)
    leadSource = models.CharField(max_length=250, blank=True)
    currentStatus = models.CharField(max_length=100, blank=True)
    purifierId = models.CharField(max_length=15, blank=True)
    latestUpdate = models.TextField(max_length=500, blank=True)

class LeadNotes(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=True)
    lead = models.ForeignKey(NewLeads,on_delete=models.CASCADE)
    leadNotes = models.CharField(max_length=1500,blank=True)
    dateTime = models.DateTimeField(auto_now=True,blank=True)

class ReferralTbl(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=True)
    name = models.CharField(max_length=250)
    mobile = models.CharField(max_length=25)
    leadSource = models.CharField(max_length=250)
    purifierId = models.CharField(max_length=15)
    enquiryDate = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=15)
    note = models.TextField(max_length=500)

class ReferralNotes(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=True)
    reflead = models.ForeignKey(ReferralTbl,on_delete=models.CASCADE)
    notes = models.CharField(max_length=250)
    timestamp = models.DateTimeField(auto_now=True)



