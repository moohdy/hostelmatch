from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from django.utils import timezone
from django.core.urlresolvers import reverse
from django.utils.text import slugify
from django.conf import settings

from phone_field import PhoneField


class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')
    
        if not password:
            raise ValueError('Users must have a password')
    
        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, password):
        """
        Creates and saves a staff user with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    first_name = models.CharField(max_length=30, blank =True)
    last_name = models.CharField(max_length=30, blank =True)
    profile_picture = models.ImageField(upload_to='users/%Y/%m/%d', null =True, blank=True)
    phone_number = PhoneField(blank=True, help_text='Contact phone number')
    #phone_number = models.CharField(max_length=13, unique=True, blank =True)
    address = models.CharField(max_length=250, blank =True)
    date_of_birth = models.DateField(null=True, blank=True)
    reg_date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False) # a admin user; non super-user
    admin = models.BooleanField(default=False) # a superuser
    # notice the absence of a "Password field", that's built in.

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [] # Email & Password are required by default.

    objects = UserManager()

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __str__(self):              # __unicode__ on Python 2
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.staff

    @property
    def is_admin(self):
        "Is the user a admin member?"
        return self.admin

    @property
    def is_active(self):
        "Is the user active?"
        return self.active
    
class Landlord(models.Model):
    '''
    the lanlord model for landlord users
    '''
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='landlords',on_delete=models.CASCADE)
    property_name = models.CharField(max_length=200)
    slug = models.SlugField(unique_for_date='reg_date', blank=True )
    reg_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return '{}'.format(self.property_name)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.property_name)
            #self.user = request.user
            super(Landlord, self).save(*args, **kwargs)
'''
    def get_absolute_url(self):
        return reverse('account:reg_landlord', args=[self.property_name])
'''

class Roomie(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='Roommate', on_delete=models.CASCADE)
    address = models.CharField(max_length=250)
    duration = models.CharField(max_length=250)
    agreement = models.CharField(max_length=1000)
    photo1 = models.ImageField(upload_to='roomies/%Y/%m/%d')
    photo2 = models.ImageField(upload_to='roomies/%Y/%m/%d')
    photo3 = models.ImageField(upload_to='roomies/%Y/%m/%d')
    photo4 = models.ImageField(upload_to='roomies/%Y/%m/%d', null =True, blank=True)
    photo5 = models.ImageField(upload_to='roomies/%Y/%m/%d', null =True, blank=True)
    payment = models.CharField(max_length=250)
    slug = models.SlugField(unique_for_date='reg_date', blank=True )
    reg_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{} {}'.format(self.user.first_name, self.user.last_name )
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.address)
            #self.user = request.user
            super(Roomie, self).save(*args, **kwargs)
    '''
    def get_absolute_url(self):
        return reverse('account:reg_landlord', args=[self.property_name])
    '''