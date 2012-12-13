$(function(){
	// Flickr restyling.
	var height = 100;

	$('.flickr_badge_image img').each(function(index){
		if($(this).height() < 90) {
			$(this).parents('.flickr_badge_image').remove();
		} else {
			height = $(this).height() < height ? $(this).height() : height;
		}
	});

	$('.flickr_badge_image a').each(function(index){
		$(this).css({
			'margin-top': -($(this).height() - height) * .5
		});
	}).hover(function(){
		var that = this;

		$('img', that).stop().animate({opacity: 0.2}, 100, function(){
			$('div', that).fadeIn(100);
		});
	}, function(){
		var that = this;

		$('img', that).stop().animate({opacity: 1}, 100, function(){
			$('div', that).fadeOut(100);
		});
	});

	// add hover div with title
	$('.flickr_badge_image a').each(function(){
		var that = $(this);
		var marginTop = parseInt(that.css('marginTop').replace('px', ''));
		var titleHover = $('<div class="flickr_badge_title_hover"></div>').css('margin-top', -marginTop).append($('img', that).attr('title'));

		that.append(titleHover);
	});

	// set whole wrapper height
	$('#flickr_badge_uber_wrapper').css({
		'height': height
	});

	// Twitter table resize.
	var maxCellSize = 220;
	var root = $('#tweets-table');
	var maxCells = Math.floor(root.width() / maxCellSize);

	$('td', root).slice(0, maxCells - 1).addClass('v').removeClass('h');
	$('td[class*="v"]', root).css({'width': 100 / ($('td[class*="v"]', root).length) + '%'});

	$(window).resize(function(){
		var maxCells = Math.floor(root.width() / maxCellSize);

		if ($('td:first', root).width() >= maxCellSize && $('td[class*="v"]', root).length < maxCells){
			$('td', root).slice(0, maxCells - 1).addClass('v').removeClass('h');
			var width = 100 / ($('td[class*="v"]', root).length) + '%';
			$('td[class*="v"]', root).css({'width': width});
		} else if ($('td:first', root).width() <= maxCellSize && $('td[class*="v"]', root).length > maxCells){
			$('td', root).slice(maxCells - 1, $('td', root).length - 1).addClass('h').removeClass('v');
			$('td[class*="v"]', root).css({'width': 100 / $('td[class*="v"]', root).length + '%'});
		}
	});
	$(window).resize();
});
