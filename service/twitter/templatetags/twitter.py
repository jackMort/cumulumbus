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

import re

from django.template import Library
from django.utils.safestring import mark_safe

register = Library()

@register.filter
def tweet( value ):
		value = re.sub(r'((mailto\:|(news|(ht|f)tp(s?))\://){1}\S+)', '<a href="\g<0>" rel="external">\g<0></a>', value)
		#value = re.sub(r'http://(yfrog|twitpic).com/(?P<id>\w+/?)', '', value)
		value = re.sub(r'#(?P<tag>\w+)', '<a href="http://search.twitter.com/search?tag=\g<tag>" rel="external">#\g<tag></a>', value)
		value = re.sub(r'@(?P<username>\w+)', '@<a href="http://twitter.com/\g<username>/" rel="external">\g<username></a>', value)
	
		return mark_safe(value)
