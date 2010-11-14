/**
 * Copyright (C) 2010  lech.twarog@gmail.com
 * 
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 * 
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 * 
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 */


Ext.namespace(
	'Cumulumbus.core'
);

Cumulumbus.core = function() {
	return {
		MAX_PERPAGE: 10,
		init: function() {
			new Ext.Viewport({
				layout: 'fit',
				items: {
					border: false,
					autoScroll: true,
					contentEl: 'posts_content',
				}
			});

			this.masonry();
			
			this.keyMap = new Ext.KeyMap( document, [
				{ key: 'h', fn: this.moveSelection.createDelegate( this, [ 'r' ] )  }, // left
				{ key: 'l', fn: this.moveSelection.createDelegate( this, [ 'l' ] )  }, // right
			])
			
			this.bindActions( '#posts_content .post' )

			this.makeConnection()
		},
		masonry: function() {
			this.wall = jQuery( '#posts_content' )

			var masonry_options = {
				columnWidth: 50,
				itemSelector: '.post', 
				animate: true,
				saveOptions: false,
				animateOptions: {
					duration: 1000,
					queue: false
				}
			};
			
			this.wall.masonry( masonry_options )
			
			jQuery( '.post:hidden' ).fadeIn()
		},
		bindActions: function( el ) {
			var self = this
			jQuery( '.post-close', el )
				.click( function() {
					var post = $( this ).closest( '.post' )
					self.closePost( post )
				})
		},
		closePost: function( el ) {
			var id = el.attr( 'id' )
			var self = this
			// ..
			jQuery.getJSON( '/readed/' + id, function( data ) {
				if ( data.success ) {
					el.fadeOut( function() {
						el.remove();
						self.updateUnreadedCount( data.unreaded )
						// fetch new parts
						self.getParts()
					})
					// ..
				}
			})
		},
		updateUnreadedCount: function( count ) {
			this.titles = [
				"CUMULUMBUS --- " + count
			]
			if( count > 0 && !this.animate_title ) {
				this.animate_title = true
				this.animateTitle()
			} else if ( count == 0 && this.animate_title ) {
				this.animate_title = false
				this.animateTitle()
			}
		},
		animateTitle: function() {
			var self = this
			if( self.animate_title ) {
				this.title_interval = setInterval( function() {
					var id = self.title_id < self.titles.length - 1  ? self.title_id + 1 : 0
						document.title = self.titles[ id ]
					self.title_id = id
				}, 1000 )
			} else {
				if( self.title_interval )
					self.title_interval.clearInterval()
			}
		},
		makeConnection: function() {
			var self = this

			var conn = hookbox.connect( "http://jackmort.hosted.hookbox.org" );
			// TODO: messaging ...
			// conn.onOpen = function() { alert("connection established!"); };
			conn.onError = function(err) { alert("connection failed: " + err.msg); };
			conn.onClose = function() { self.makeConnection() };

			var subscription = null;
			conn.onSubscribed = function( channelName, _subscription ) {
				subscription = _subscription;                
				subscription.onPublish = function( frame ) {
					id = frame['payload']['id']
					jQuery.get( '/post/' + id, function( data ) {
						var item = $( data )
						item.css( 'position', 'absolute' );
						self.bindActions( item )
						self.wall.append( item )

						self.masonry()
					})
				};  
			};
			conn.subscribe( "posts" )
		},
		getParts: function() {
			var self = this;
			var parts = $( '.post', this.wall )
			if( parts.length < this.MAX_PERPAGE ) {
				var id = parts.length > 0 ? parts.last().attr( 'id' ) : 0
				var count = this.MAX_PERPAGE - parts.length
				jQuery.get( '/posts/fetch/' + id + '/'+ count, function( data ) {
						if( data.length > 10 /* FIXME */ ) {
							var items = $( data )
							items.css( 'position', 'absolute' );
							self.bindActions( items )
							self.wall.append( items )
						}
						self.masonry()
					})
			}
		},
		moveSelection: function( direction ) {
			// TODO: move selection to next/prev element
		}
	}
}();

Ext.onReady( Cumulumbus.core.init, Cumulumbus.core )
