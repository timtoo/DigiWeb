from django.conf.urls.defaults import *
from django.http import HttpResponsePermanentRedirect
from django.contrib.auth.views import login

urlpatterns = patterns('dreamvault.views',
    url('^$', 'default', name="home"),
)

#urlpatterns += patterns('',
#    ('^login', 'django.contrib.auth.views.login'),
#)

