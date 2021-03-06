#!/usr/bin/python

import json
import urllib
import urllib2

from django.conf import settings

class HookboxHelper:
	def __init__( self, url, secret ):
		self.url = url
		self.secret = secret

	def publish( self, channel, payload ):
		values = { 
			"secret" : "cumul4",
			"channel_name" : "posts",
			"payload" : json.dumps( payload )
		}

		return self._request( "%s/rest/publish" % self.url, values ).read() == '[true, {}]'

	def _request( self, url, values ):
		data = urllib.urlencode( values )
		req = urllib2.Request( url, data )

		return urllib2.urlopen( req )


hookbox_helper = HookboxHelper( settings.HOOKBOX_URL, settings.HOOKBOX_SECRET )
