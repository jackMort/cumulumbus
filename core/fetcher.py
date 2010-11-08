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

from datetime import datetime

from cumulumbus.core.utils import to_timestamp

class BaseFetcher( object ):
	def __init__( self, serviceAccount ):
		self.serviceAccount = serviceAccount

	def run( self ):
		self.fetch( to_timestamp( self.serviceAccount.last_import ) )
		self.serviceAccount.last_import = datetime.now()
		self.serviceAccount.save()

	def fetch( self, since=None ):
		pass
