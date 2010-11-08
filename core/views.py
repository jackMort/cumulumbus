from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response

from cumulumbus.core.models import Post
from cumulumbus.service.lastfm.models import LastfmAccount
from cumulumbus.service.lastfm.fetcher import LastfmFetcher

def index( request ):
	account, created = LastfmAccount.objects.get_or_create( service = 'lastfm', username = 'robinhooj' );
	fetcher = LastfmFetcher( account )
	fetcher.run();
	items = Post.objects.all().order_by( '-date_added' )
	print dir( items[0] )
	return render_to_response( "index.html", { "items": items }, context_instance = RequestContext( request ) )

