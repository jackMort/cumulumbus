# -*- coding: utf-8 -*-

# Copyright (C) 2010  {lech.twarog@gmail.com}
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from django.conf import settings
from django.utils.html import strip_tags

import feedparser

from cumulumbus.core.utils import from_timetuple, to_timestamp, from_timestamp
from cumulumbus.core.fetcher import BaseFetcher
from cumulumbus.service.rss.models import RSSAccount, RSSEntry

class RSSFetcher( BaseFetcher ):
	def __init__( self, serviceAccount ):
		assert isinstance( serviceAccount, RSSAccount )
		super( RSSFetcher, self ).__init__( serviceAccount )
	
	def fetch( self, since=None ):
		rss = feedparser.parse( self.serviceAccount.url )
		print "-- %s [%s]. %d items" % ( self.serviceAccount.url, since if since else "ALL_TIME", len( rss['entries'] ) )
		for entry in rss['entries']:
			timestamp = to_timestamp( entry['updated_parsed'] ) + 3600 # TODO
			if timestamp > since:
				print "  `-- %s [%s]" % ( entry.title, from_timestamp( timestamp ) )
				
				if entry['summary_detail']['type'] == 'text/html':
					body = strip_tags( entry['summary_detail']['value'] )
					# TODO rest of types
				else:
					body = entry['summary_detail']['value']

				image_url = None
				if entry.has_key( 'enclosures' ):
					for enclosure in entry['enclosures']:
						if "image/" in enclosure['type']:
							image_url = enclosure['href']

				entry, created = RSSEntry.objects.get_or_create(
					account = self.serviceAccount,
					date_added = from_timestamp( timestamp ),
					title = entry['title'],
					url = entry['link'],
					image_url = image_url,
					body = body
				)
