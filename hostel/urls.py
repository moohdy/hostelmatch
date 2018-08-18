from django.conf.urls import url
from . import views


urlpatterns = [
    #url for the homepage 
    url(r'^$', views.homepage, name='homepage'),
    #url for the about page
    url(r'^about-hostelite/$', views.about_hostelite, name='about_hostelite'),
    url(r'^vacant-hostels/$', views.hostel_list, name='vacant_hostels'),
    #url(r'^like/$', views.house_like, name='like'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<title>[-\w]+)/(?P<location>[-\w]+)/$',views.hostel_detail, name='hostel_detail'),
    #home urls: retrieve houses by tag search
    #url(r'^tag/(?P<tag_slug>[-\w]+)/$', views.homes_list, name='homes_list_by_tag'),
    
]