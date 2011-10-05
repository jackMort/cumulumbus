from django.contrib import admin

from cumulumbus.core.models import Post, ServiceAccount

admin.site.register( Post )
admin.site.register( ServiceAccount )
