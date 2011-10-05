from cumulumbus.core.models import post_imported
from cumulumbus.hookbox.utils import hookbox_helper


def notify_post_imported( sender, **kwargs ):
	#TODO user channel
	post = kwargs['post']
	try:
		hookbox_helper.publish( "posts", { 'id': post.id } )
	except:
		pass

post_imported.connect( notify_post_imported )
