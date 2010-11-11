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

class TwitterAccount( ServiceAccount ):
	username = models.CharField( _( "username" ), max_length = 100 )

	class Meta:
		verbose_name = _( "Twitter account" )
		verbose_name_plural = _( "Twitter accounts" )

class TwitterUser( models.Model ):
	screen_name = models.CharField( _( "screen name" ), max_length = 100 )
	name = models.CharField( _( "name" ), max_length = 200 )

	class Meta:
		verbose_name = _( "Twitter user" )
		verbose_name_plural = _( "Twitter users" )

	def get_absolute_url( self ):
		return "http://twitter.com/%s" % self.screen_name

class TwitterPost( Post ):
	user = models.ForeignKey( TwitterUser, verbose_name = _( "user" ) )
	body = models.TextField( _( "body" ), blank = True, null = True )

	class Meta:
		verbose_name = _( "Twitter post" )
		verbose_name_plural = _( "Twitter posts" )


