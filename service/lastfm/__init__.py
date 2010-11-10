from cumulumbus.core.service import Service

class LastfmService( Service ):
	name = "lastfm"
	
	def get_fetchers( self ):
		from cumulumbus.service.lastfm.fetcher import LastfmFetcher
		return [ LastfmFetcher ]
