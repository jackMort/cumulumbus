from django.conf.urls.defaults import *
from django.contrib import admin
admin.autodiscover()

from cumulumbus.core.views import index

urlpatterns = patterns('',
	( r'^$', index ),
	( r'^admin/', include( admin.site.urls ) ),
)
