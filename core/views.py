from django.http import HttpResponse

from cumulumbus.service.lastfm.models import LastfmAccount
from cumulumbus.service.lastfm.fetcher import LastfmFetcher

def index( request ):
	account, created = LastfmAccount.objects.get_or_create( service = 'lastfm', username = 'robinhooj' );
	fetcher = LastfmFetcher( account )
	fetcher.fetch();

	return HttpResponse( 'OK' )

