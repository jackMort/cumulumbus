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

import logging

from threading import Thread, Lock
from datetime import datetime

from cumulumbus.core.utils import to_timestamp
from cumulumbus.core.models import post_imported

class BaseFetcher( Thread ):
	def __init__( self, serviceAccount ):
		Thread.__init__( self )
		self.serviceAccount = serviceAccount
		self._logger = logging.getLogger( 'cumulumbus.fetcher.%s' % serviceAccount.service )

	def run( self ):
		lock = Lock()
		lock.acquire()
		# store date to catch elements added 
		# while import is in proggress
		next_import = datetime.now()

		last_import = to_timestamp( self.serviceAccount.last_import ) -1000 \
				if self.serviceAccount.last_import else None
		self.fetch( last_import )
		self.serviceAccount.last_import = next_import
		self.serviceAccount.save()
		lock.release()

	def fetch( self, since=None ):
		pass

	def fetched( self, post ):
		post_imported.send( sender=self, post=post )

	@property
	def logger( self ):
		return self._logger
