from django.db import models
from django.utils import timezone
from django.conf import settings
from django.core.urlresolvers import reverse


class VacanthostelManager(models.Manager):
    def get_queryset(self):
        return super(VacanthostelManager, self).get_queryset().filter(vacant=True)


class Hostel(models.Model):
    #landlord = models.ForeignKey(Landlord, related_name='landlords' )
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique_for_date='created' )
    address = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    image1 = models.ImageField(upload_to='hostel/%Y/%m/%d')
    image2 = models.ImageField(upload_to='hostel/%Y/%m/%d')
    image3 = models.ImageField(upload_to='hostel/%Y/%m/%d')
    image4 = models.ImageField(upload_to='hostel/%Y/%m/%d', blank=True)
    image5 = models.ImageField(upload_to='hostel/%Y/%m/%d', blank=True)
    description = models.CharField(max_length=200, blank=True)
    vacant = models.BooleanField(default=True)
    price = models.CharField(max_length=200)
    created = models.DateField(db_index=True, default=timezone.now)
    #users_like = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='houses_liked', blank=True)
    objects = models.Manager() #the default manager
    vacanthostel = VacanthostelManager() #our customized manager
    #tags = TaggableManager() #the tag manager
    
    class Meta:
        ordering = ('-created',)
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('hostel:hostel_detail',
                       args=[self.created.year, self.created.strftime('%m'), self.created.strftime('%d'),
                             self.slug, self.location])

