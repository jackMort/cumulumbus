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
			this.initialiseHistory();
			this.wall = jQuery( '#posts_content' )

			new Ext.Viewport({
				layout: 'fit',
				items: {
					border: false,
					autoScroll: true,
					contentEl: 'posts_content',
				}
			});

			//this.masonry();
			
			this.keyMap = new Ext.KeyMap( document, [
				{ key: 'h', fn: this.keyAction.createDelegate( this, [ 'l' ] )  }, // left
				{ key: 'l', fn: this.keyAction.createDelegate( this, [ 'r' ] )  }, // right
				{ key: 'c', fn: this.keyAction.createDelegate( this, [ 'c' ] )  }, // close
			])
			
			//this.bindActions( '#posts_content .post' )
			this.getParts();

			this.makeConnection()
		},
		masonry: function() {

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
			
			this.wall.masonry( masonry_options );

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
						self.makeSelection( el.next() )
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
		keyAction: function( direction ) {
			var first = jQuery( ".post", this.wall ).first()
			var last = jQuery( ".post", this.wall ).last()

			switch( direction ) {
				case "r": 
					if( !this.selected || this.selected == last ) this.makeSelection( first )
					else this.makeSelection( this.selected.next() )
					break;
				case "l": 
					if( !this.selected || this.selected == first ) this.makeSelection( last );
					else this.makeSelection( this.selected.prev() )
					break;
				case "c": 
					if( this.selected ) this.closePost( this.selected );
					break;
			}
		},
		makeSelection: function( post ) {
			jQuery( ".post.selected", this.wall ).removeClass( 'selected' )
			// ..
			this.selected = post;
			this.selected.addClass( 'selected' );
		},
		/**
		 * Creates the necessary DOM elements required for Ext.History to manage state
		 * Sets up a listener on Ext.History's change event to fire this.handleHistoryChange
		 */
		initialiseHistory: function() {
			this.historyForm = Ext.getBody().createChild({
				tag: 'form', action: '#', cls: 'x-hidden', id: 'history-form',
				children: [
					{ tag: 'div', children: [
						{ tag:  'input', id:   Ext.History.fieldId, type: 'hidden' },
						{ tag:  'iframe', id:   Ext.History.iframeId }
					]}
				]
			});

			//initialize History management
			Ext.History.init( 
				this.handleHistoryChange.createDelegate( this, [document.location.hash.replace("#", "")] ) 
			);
			Ext.History.on('change', this.handleHistoryChange, this);
		},
		handleHistoryChange: function( token ) {
			if( !token ) return;

			switch( token ) {
				case "archive": this.archive(); break;
				default: window.location = window.location.href.split('#')[0]
			}
		},
		archive: function() {

		}
	}
}();

Ext.onReady( Cumulumbus.core.init, Cumulumbus.core )
