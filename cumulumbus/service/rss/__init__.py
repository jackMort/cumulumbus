from cumulumbus.core.service import Service

class RSSService( Service ):
	name = "rss"

	def get_fetchers( self ):
		from cumulumbus.service.rss.fetcher import RSSFetcher
		return [ RSSFetcher ]
