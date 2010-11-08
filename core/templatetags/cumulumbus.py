# -*- coding: utf-8 -*-

# Copyright (C) 2010  {lech.twarog@gmail.com}
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from django import template
from django.contrib.contenttypes.models import ContentType

from core.models import Post

register = template.Library()

# TODO move to better place
class PostModels( object ):
	def __init__( self ):
		self.cache = {}
		self.cached = False

	def clear_cache( self ):
		self.cache = {}
		self.cached = False

	def get_types( self ):
		if not self.cached:
			for ct in ContentType.objects.all():
				model = ct.model_class()
				if model is not None\
					and ct.app_label != 'core'\
					and ct.model != 'post'\
						and issubclass( model, Post ):
					self.cache[ct.model] = ct
			self.cached = True
		return self.cache

post_models = PostModels()

@register.inclusion_tag( 'display_single_post.html', takes_context = True )
def render_post( context, post ):
	types = post_models.get_types()
	
	for key, ct in types.items():
		try:
			object = getattr( post, key )
			return { 
				'template': '%s/display_%s.html' % ( ct.app_label, ct.model ),
				'post': post,
				'object': object 
			}
		except:
			pass
