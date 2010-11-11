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
		init: function() {
			new Ext.Viewport({
				layout: 'fit',
				items: {
					border: false,
					contentEl: 'posts_content'
				}
			});

			this.masonry();
			
			this.keyMap = new Ext.KeyMap( document, [
				{ key: 'k', fn: function() { console.log( "UP" )}  }, // up
				{ key: 'j', fn: function() { console.log( "DOWN" )} }, // down
				{ key: 'h', fn: function() { console.log( "LEFT" )}  }, // left
				{ key: 'l', fn: function() { console.log( "RIGHT" )}  }, // right
			])
			
			this.bindActions( '#posts_content .post' )
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
			jQuery.get( '/readed/' + id, function( data ) {
				// TODO: json, and messaging
				if ( data == 'OK' ) {
					el.fadeOut( function() {
						el.remove();
						self.masonry();
					})
					// ..
				}
			})
		}
	}
}();

Ext.onReady( Cumulumbus.core.init, Cumulumbus.core )
/*
		jQuery( window ).load( function() {
			$wall = jQuery( '.posts' )
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
			var delete_post = function() {
				var self = $( this ), id = self.attr( 'id' )
				jQuery.get( '/readed/' + id, function( data ) {
					// TODO: json, and messaging
					if ( data == 'OK' ) {
						self.remove()
						$wall.masonry( masonry_options )
					} else {
						alert( 'ERROR: while processing ...' )
					}
				})
			};

			$wall.masonry( masonry_options )
			
			var make_connection = function() {
				var conn = hookbox.connect('http://jackmort.hosted.hookbox.org');
				// TODO: messaging ...
				// conn.onOpen = function() { alert("connection established!"); };
				conn.onError = function(err) { alert("connection failed: " + err.msg); };
				conn.onClose = function() { make_connection() };

				var subscription = null;
				conn.onSubscribed = function(channelName, _subscription) {
					subscription = _subscription;                
					subscription.onPublish = function( frame ) {
						id = frame['payload']['id']
						jQuery.get( '/post/' + id, function( data ) {
							$item = $( data )
							$wall.append( $item )
							$item.click( delete_post )
							$wall.masonry( { appendedContent: $item } )
						})
					};  
				};
				conn.subscribe( "posts" );
			}

			make_connection();

			// mark as readed
			jQuery( '.post' ).click( delete_post )
		})
*/
