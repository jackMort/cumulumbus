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
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

from cumulumbus.core.servicehook_pool import servicehook_pool

class UserProfile( models.Model ):
	user = models.ForeignKey( User, unique = True, related_name = 'profile' )
	services = models.ManyToManyField( 'ServiceAccount', blank = True, null = True )

class ServiceAccount( models.Model ):
	service = models.CharField( _( "service" ), max_length = 100, choices = servicehook_pool.get_servicehooks() )
	last_import = models.DateTimeField( _( "last import" ), null=True, blank=True )

class Post( models.Model ):
	account = models.ForeignKey( ServiceAccount, verbose_name = _( "service account" ) )
	# ...
	date_added = models.DateTimeField( _( "date added" ) )
	readed = models.BooleanField( _( "is readed" ) )
	locked = models.BooleanField( _( "is locked" ) )

