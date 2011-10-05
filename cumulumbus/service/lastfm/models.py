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

from django.db import models
from django.utils.translation import ugettext_lazy as _

from cumulumbus.core.models import ServiceAccount, Post

class LastfmElement( models.Model ):
	mbid = models.CharField( _( "mbid" ), max_length = 255 )
	url = models.URLField( _( "url" ) )
	image_url = models.CharField( _( "image url" ), max_length = 255, blank = True, null = True )

	class Meta:
		abstract = True

class LastfmAccount( ServiceAccount ):
	username = models.CharField( _( "username" ), max_length = 100 )

class LastfmUser( LastfmElement ):
	username = models.CharField( _( "username" ), max_length = 100 )

class LastfmArtist( LastfmElement ):
	name = models.CharField( _( "name" ), max_length = 255 )

class LastfmTrack( LastfmElement ):
	title = models.CharField( _( "track" ), max_length = 255 )
	artist = models.ForeignKey( LastfmArtist, verbose_name = _( "artist" ) )
	duration = models.CharField( _( "duration" ), max_length = 50 )
	streamable = models.BooleanField( _( "streamable" ) )

class LastfmFriendListen( Post ):
	friend = models.ForeignKey( LastfmUser, verbose_name = _( "friend" ) )
	track = models.ForeignKey( LastfmTrack, verbose_name = _( "track" ) )

