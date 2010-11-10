from datetime import datetime

from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404

from cumulumbus.core.models import Post

def index( request ):
	items = Post.objects.filter( readed = False ).order_by( '-date_added' )[:50]
	
	return render_to_response( "index.html", { "items": items }, context_instance = RequestContext( request ) )

def test_stomp( request ):
	import stomp
	import json

	conn = stomp.Connection( host_and_ports = [ ('127.0.0.1', 13131314) ] ) 
	conn.start()
	conn.connect()
	conn.subscribe( destination='/posts', ack='auto' )
	
	post = Post.objects.all()[0]
	msg = json.dumps( { 'post': { 'id': post.id }  } )

	conn.send( msg, destination='/posts' )
	return HttpResponse( 'OK' )

def mark_as_readed( request, id ):
	post = get_object_or_404( Post, id = id )
	
	if request.is_ajax():
		post.readed = True
		post.save()
	
	return HttpResponse( 'OK' )
