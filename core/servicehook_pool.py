from django.conf import settings
from cumulumbus.core.service import Service

class ServicehookPool( object ):
	def __init__( self ):
		self.services = {}
		self.block_register = False
		self.discovered = False
		
	def discover_services(self):
		if self.discovered:
			return
		
		if settings.SERVICES:
			for app in settings.SERVICES:
				self.block_register = True
				path = ".".join( app.split( "." )[:-1] )
				class_name = app.split( "." )[-1]
				module = __import__( path, {}, {}, [class_name] )
				self.block_register = False
				cls = getattr( module, class_name )
				self.register( cls )
		
		self.discovered = True
		
	def clear( self ):
		self.services = {}
		self.discovered = False

	def register( self, service ):
		if self.block_register:
			return
		
		assert issubclass( service, Service )
		if not service.__name__ in self.services.keys():
			self.services[service.__name__] = service
		
	def get_servicehooks( self ):
		self.discover_services()
		hooks = []
		for service_name in self.services.keys():
			service = self.services[service_name]
			hooks.append( ( service_name, service.name ) )
		return hooks
	
	def get_servicehook( self, service_name ):
		return self.services[service_name]

servicehook_pool = ServicehookPool()
