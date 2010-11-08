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

import pylast

from cumulumbus.core.utils import from_timestamp, to_timestamp
from cumulumbus.core.fetcher import BaseFetcher
from cumulumbus.service.lastfm.models import LastfmAccount, LastfmFriendListen

class LastfmFetcher( BaseFetcher ):
	def __init__( self, serviceAccount ):
		assert isinstance( serviceAccount, LastfmAccount )
		super( LastfmFetcher, self ).__init__( serviceAccount )
	
	def fetch( self, since=None ):
		network = pylast.get_lastfm_network( api_key = settings.LASTFM_API_KEY, api_secret = settings.LASTFM_API_SECRET )
		lasftmUser = network.get_user( self.serviceAccount.username )
		friends = lasftmUser.get_friends()
		for friend in friends:
			try:
				recent_tracks = friend.get_recent_tracks( since=since )
				print "-- %s [%d]. %d items" % ( friend, since, len( recent_tracks ) )
				for recent in recent_tracks:
					print "  `-- %s [%s]" % ( recent.track, from_timestamp( recent.timestamp ) )
					LastfmFriendListen.objects.create(
						account = self.serviceAccount,
						date_added = from_timestamp( recent.timestamp ),
						friend = str( friend ), # TODO: class LastfmUser
						track = recent.track # TODO: class LastfmTrack
					)
			except pylast.WSError:
				pass
