from django.conf.urls import url
from . import views

urlpatterns = [
    #url patterns for the registration applicarion, consisting of url, a mapped view and a url name
    # registration app urls
    
    # registration urls: user registration/profile urls
    url(r'^dashboard/$', views.dashboard, name='dashboard'),
    
    # registration urls: login/logout urls
    url(r'^login/$','django.contrib.auth.views.login', name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout',{'template_name':'registration/logged_out.html',}, name='logout'),
    url(r'^logout-then-login/$', 'django.contrib.auth.views.logout_then_login', name='logout_then_login'),

    # registration urls: password urls (change password urls)
    url(r'^password-change/$', 'django.contrib.auth.views.password_change', name='password_change'),
    url(r'^password-change/done/$', 'django.contrib.auth.views.password_change_done', name='password_change_done'),
    
    # registration urls: password urls (reset password urls)
    url(r'^password-reset/$', 'django.contrib.auth.views.password_reset', name='password_reset'),
    url(r'^password-reset/done/$', 'django.contrib.auth.views.password_reset_done', name='password_reset_done'),
    url(r'^password-reset/confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$', 'django.contrib.auth.views.password_reset_confirm', name='password_reset_confirm'),
    url(r'^password-reset/complete/$', 'django.contrib.auth.views.password_reset_complete', name='password_reset_complete'),
    

    ]
