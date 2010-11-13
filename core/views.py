from datetime import datetime

from django.utils import simplejson
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404

from cumulumbus.core.models import Post

def index( request ):
	items = Post.objects.filter( readed = False ).order_by( 'date_added' )[:50]
	
	return render_to_response( "index.html", { "items": items }, context_instance = RequestContext( request ) )

def get_by_id( request, id ):
	post = get_object_or_404( Post, id = id )
	return render_to_response( "post.html", { "post": post }, context_instance = RequestContext( request ) )

def mark_all_as_readed( request ):
	Post.objects.filter( readed = False ).update( readed = True )

	return HttpResponse( 'ok' )

def mark_as_readed( request, id ):
	post = get_object_or_404( Post, id = id )

	if request.is_ajax():
		post.readed = True
		post.save()

	unreaded = Post.objects.filter( readed = False ).count()	


	return HttpResponse( simplejson.dumps( { "success": True, "unreaded": unreaded  } ) )
