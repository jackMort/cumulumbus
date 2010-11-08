import os

from django.conf.urls.defaults import *
from django.contrib import admin

from cumulumbus.core.views import index

admin.autodiscover()

urlpatterns = patterns('',

	( r'^media/(.*)$', 'django.views.static.serve', { 'document_root' : os.path.join( os.path.dirname( __file__ ), 'media' ) } ),
	( r'^$', index ),
	( r'^admin/', include( admin.site.urls ) ),
)
