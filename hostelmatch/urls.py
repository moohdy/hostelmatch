from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    #url site main address
    url(r'^hostelite/', include('hostel.urls', namespace='hostel', app_name='hostel')),
    #the site main address url
    #url(r'^hostelmatch/', include('registration.urls', namespace='registration', app_name='registration')),
    #the django authentication urls
    #url('^', include('django.contrib.auth.urls')),
    #haystack solr search url config
    #url(r'^search/', include('haystack.urls')),
    
]

#for media and picture directory
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

