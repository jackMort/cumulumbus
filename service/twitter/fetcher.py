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

import twitter

from django.conf import settings

from cumulumbus.core.utils import to_timestamp, from_timestamp
from cumulumbus.core.fetcher import BaseFetcher
from cumulumbus.service.twitter.models import TwitterAccount, TwitterUser, TwitterPost

class TwitterFetcher( BaseFetcher ):
	def __init__( self, serviceAccount ):
		if not isinstance( serviceAccount, TwitterAccount ):
			serviceAccount = serviceAccount.twitteraccount
		super( TwitterFetcher, self ).__init__( serviceAccount )
	
	def fetch( self, since=None ):
		client = twitter.Api()
		posts = client.GetUserTimeline( self.serviceAccount.username )

		self.logger.info( "-- %s [%s]. %d items" % ( self.serviceAccount.username, since if since else "ALL_TIME", len( posts ) ) )
		for post in posts:
			user = post.GetUser()
			id = post.GetId()
			body = post.GetText()
			
			timestamp = post.GetCreatedAtInSeconds() + user.utc_offset
			if timestamp > since:
				self.logger.info("  `-- %s [%s]" % ( body, from_timestamp( timestamp ) ) )

				user, created = TwitterUser.objects.get_or_create(
					screen_name = user.screen_name,
					name = user.name
				)

				post, created = TwitterPost.objects.get_or_create(
					account = self.serviceAccount,
					date_added = from_timestamp( timestamp ),
					body = body,
					user = user
				)

				if created:
					self.fetched( post )
