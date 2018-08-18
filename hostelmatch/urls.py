from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #url for registering models to admin
    url(r'^admin/', include(admin.site.urls)),
    #urls for the website main addresses:
    #urls for the hostel application
    url(r'^hostelite/', include('hostel.urls', namespace='hostel', app_name='hostel')),
    #url for the account application
    url(r'^hostelite/', include('account.urls', namespace='account', app_name='account')),
    #the django authentication urls
    url(r'^hostelite/', include('django.contrib.auth.urls')),
    #haystack solr search url config
    #url(r'^search/', include('haystack.urls')),
    
]

#for media and picture directory
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

