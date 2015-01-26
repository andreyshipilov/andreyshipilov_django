(function($) {

	// for tracking the current position of the mouse
	var mouse_x = 0,
	mouse_y = 0,
	mouse_tracking = false;

	$.squidy = function(options) {
		var defaults = {
			tail_length: 0,
			animation_interval: 0.04,
			wobble: 2,
			head_img: '',
			tail_img: '',
			tail_spacing_x: 0,
			tail_spacing_y: 2,
			tail_offset_x: 0,
			tail_offset_y: 2,
		}

		opts = $.extend({},
		defaults, options);

		squid = new squidy(opts);

		$.periodic(function() {
			squid.animate();
			return true;
		},
		{
			frequency: opts.animation_interval
		});

		if (!mouse_tracking) {
			start_mouse_tracking();
		}
	}

	function start_mouse_tracking() {
		$().mousemove(function(e) {
			mouse_x = e.pageX;
			mouse_y = e.pageY;
		});
	}

	function create_layer(img_src, x, y, zindex, opacity) {
		$('body').append('<img class="segment-' + zindex + '" />');
		img = $('img.segment-' + zindex);
		img.attr({
			src: img_src
		}).css({
			opacity: opacity,
			position: 'absolute',
			top: x,
			left: y,
			zIndex: zindex
		});
		return img;
	}

	function squidy(opts, head_img, tail_img) {
		var opacity = 100;
		this.followers = new Array();
		this.followers[0] = create_layer(opts.head_img, -200, 200, opts.tail_length, opacity);

		var op = opacity - 20;
		for (i = 1; i < opts.tail_length; i++) {
			op -= 5;
			this.followers[i] = create_layer(opts.tail_img, -200, 200, opts.tail_length - i, op / 100);
		}

		this.targetX = 200;
		this.targetY = 200;
		this.x = -100;
		this.y = -100;
		this.dx = 0;
		this.dy = 0;

		this.animate = function() {
			var m, offset;
			for (i = this.followers.length - 1; i > 0; i--) {
				// get the position of the next layer
				offset = this.followers[i - 1].offset();
				// allows us to set an offset on the tail
				// this is useful if the tail graphic is smaller than the head
				offset.left += (i != 1) ? opts.tail_spacing_x: opts.tail_offset_x;
				offset.top -= (i != 1) ? opts.tail_spacing_y: opts.tail_offset_y;
				this.followers[i].css(offset);
			}
			m = this.followers[0];
			offset = m.offset();
			var X = (this.targetX - offset.left);
			var Y = (this.targetY - offset.top);
			var len = Math.sqrt(X * X + Y * Y) || 2;
			var dx = 20 * (X / len);
			var dy = 20 * (Y / len);
			var ddx = (dx - this.dx) / 10;
			var ddy = (dy - this.dy) / 10;
			this.dx += ddx;
			this.dy += ddy;
			offset.left += this.dx;
			offset.top += this.dy;

			m.css(offset);
			this.targetX = mouse_x - (m.width() / 2) + Math.floor(Math.random() * opts.wobble) + 50;
			this.targetY = mouse_y - (m.height() - 5) + Math.floor(Math.random() * opts.wobble) + 50;
		}
	}

})(jQuery);

jQuery.periodic = function(callback, options) {
	callback = callback || (function() {
		return false;
	});

	options = jQuery.extend({},
	{
		frequency: 10,
		allowParallelExecution: false
	},
	options);

	var currentlyExecuting = false;
	var timer;

	var controller = {
		stop: function() {
			if (timer) {
				window.clearInterval(timer);
				timer = null;
			}
		},
		currentlyExecuting: false,
		currentlyExecutingAsync: false
	};

	timer = window.setInterval(function() {
		if (options.allowParallelExecution || !(controller.currentlyExecuting || controller.currentlyExecutingAsync)) {
			try {
				controller.currentlyExecuting = true;
				if (! (callback(controller))) {
					controller.stop();
				}
			} finally {
				controller.currentlyExecuting = false;
			}
		}
	},
	options.frequency * 1000);
};