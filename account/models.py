from django.db import models
from django.conf import settings


class Profile(models.Model):
    '''
    the profile model used for creating the database and also used as model for a the profileform
    '''
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='users/%Y/%m/%d', blank=True)
    contact = models.PositiveIntegerField(blank=True, null=True, unique=True)
    date_of_birth = models.DateField(blank=True, null=True)
    location = models.CharField( max_length=250, blank=True, null=True)
    reg_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('reg_date',)

    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)

    def get_absolute_url(self):
        return reverse('registration:profile', args=[self.user.username])

    
