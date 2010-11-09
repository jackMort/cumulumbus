from datetime import datetime

from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404

from cumulumbus.core.models import Post
from cumulumbus.service.lastfm.models import LastfmAccount
from cumulumbus.service.lastfm.fetcher import LastfmFetcher
from cumulumbus.service.rss.models import RSSAccount
from cumulumbus.service.rss.fetcher import RSSFetcher

def index( request ):
	account, created = LastfmAccount.objects.get_or_create( service = 'LastfmService', username = 'robinhooj' );
	if created:
		account.last_import = datetime.now()
		account.save()
	
	fetcher = LastfmFetcher( account )
	fetcher.run();
	
	account, created = RSSAccount.objects.get_or_create( service = 'RSSService', url = 'http://feeds.feedburner.com/ajaxian' );
	if created:
		account.last_import = datetime.now()
		account.save()

	fetcher = RSSFetcher( account )
	fetcher.run()

	account, created = RSSAccount.objects.get_or_create( service = 'RSSService', url = 'http://legia.com/www/view_rss.php' );
	if created:
		account.last_import = datetime.now()
		account.save()

	fetcher = RSSFetcher( account )
	fetcher.run()
	
	account, created = RSSAccount.objects.get_or_create( service = 'RSSService', url = 'http://feeds.feedburner.com/ps3site-pl' );
	if created:
		account.last_import = datetime.now()
		account.save()

	fetcher = RSSFetcher( account )
	fetcher.run()

	account, created = RSSAccount.objects.get_or_create( service = 'RSSService', url = 'http://www.rmf24.pl/feed' );
	if created:
		account.last_import = datetime.now()
		account.save()

	fetcher = RSSFetcher( account )
	fetcher.run()

	account, created = RSSAccount.objects.get_or_create( service = 'RSSService', url = 'http://filmaster.pl/planeta/rss' );
	if created:
		account.last_import = datetime.now()
		account.save()

	fetcher = RSSFetcher( account )
	fetcher.run()

	items = Post.objects.filter( readed = False ).order_by( '-date_added' )[:50]
	
	return render_to_response( "index.html", { "items": items }, context_instance = RequestContext( request ) )

def mark_as_readed( request, id ):
	post = get_object_or_404( Post, id = id )
	
	if request.is_ajax():
		post.readed = True
		post.save()
	
	return HttpResponse( 'OK' )
