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
from cumulumbus.service.lastfm.models import *

class LastfmFetcher( BaseFetcher ):
	def __init__( self, serviceAccount ):
		assert isinstance( serviceAccount, LastfmAccount )
		super( LastfmFetcher, self ).__init__( serviceAccount )
	
	def fetch( self, since=None ):
		network = pylast.get_lastfm_network( api_key = settings.LASTFM_API_KEY, api_secret = settings.LASTFM_API_SECRET )
		lasftmUser = network.get_user( self.serviceAccount.username )
		friends = lasftmUser.get_friends()

		friends.append( lasftmUser )
		for friend in friends:
			try:
				friend_mbid = friend.get_id()
				friend_name = friend.get_name()
				try:
					friend_user = LastfmUser.objects.get( mbid = friend_mbid )
				except LastfmUser.DoesNotExist:
					friend_user = LastfmUser(
						mbid = friend_mbid,
						url = "http://last.fm/user/%s" % friend_name,
						image_url = friend.get_image(),
						username = friend_name
					)
					friend_user.save()

				recent_tracks = friend.get_recent_tracks( since=since, limit=5 )
				print "-- %s [%s]. %d items" % ( friend, since if since else "ALL_TIME", len( recent_tracks ) )
				for recent in recent_tracks:
					print "  `-- %s [%s]" % ( recent.track, from_timestamp( recent.timestamp ) )
					
					track_artist = recent.track.get_artist()
					artist_mbid = track_artist.get_mbid()
					if artist_mbid is None:
						artist_mbid = track_artist.name
					
					try:
						artist = LastfmArtist.objects.get( mbid = artist_mbid )
					except LastfmArtist.DoesNotExist:
						artist = LastfmArtist(
							mbid = artist_mbid,
							url = track_artist.get_url(),
							image_url = track_artist.get_cover_image(),
							name = track_artist.get_name()
						)
						artist.save()

					track = recent.track
					track_mbid = track.get_id()
					track_album = track.get_album()

					try:
						track = LastfmTrack.objects.get( mbid = track_mbid )
					except LastfmTrack.DoesNotExist:
						track = LastfmTrack(
							mbid = track_mbid,
							url = track.get_url(),
							image_url = track_album.get_cover_image() if track_album else track_artist.get_cover_image(),
							artist = artist,
							title = track.get_title(),
							duration = track.get_duration(),
							streamable = track.is_streamable()
						)
						track.save()
					
					LastfmFriendListen.objects.get_or_create(
						account = self.serviceAccount,
						date_added = from_timestamp( recent.timestamp ),
						friend = friend_user,
						track = track
					)

			except pylast.WSError:
				pass
