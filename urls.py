import os

from django.conf.urls.defaults import *
from django.contrib import admin

from cumulumbus.core.views import index, mark_as_readed, get_by_id

admin.autodiscover()

urlpatterns = patterns('',

	( r'^media/(.*)$', 'django.views.static.serve', { 'document_root' : os.path.join( os.path.dirname( __file__ ), 'media' ) } ),
	( r'^$', index ),
	( r'^post/(?P<id>\d+)$', get_by_id ),
	( r'^admin/', include( admin.site.urls ) ),
	( r'readed/(?P<id>\d+)', mark_as_readed ),
)
