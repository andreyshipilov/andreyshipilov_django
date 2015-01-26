$(function(){
	$.preloadImages('../m/project/history-icons/c.png', '../m/project/history-icons/l.png', '../m/project/history-icons/o.png', '../m/project/history-icons/r.png', '../m/project/history-icons/s.png');
	$('#about-switch li').click(function(){
		$('#about-switch li').attr('class', null);
		$(this).addClass($(this).attr('id') + '-in');
		var _ = $(this), o = $('.history-element-chosen');

		$('#history-icon' + o.attr('rel')).css({
			opacity: 0
		});
		$('#about-stuff > div').not($('#' + $(this).attr('id') + '-content')).hide(200, function(){
			$('#' + _.attr('id') + '-content').appendTo($('#about-stuff')).show();
		});
		setTimeout(function(){
			$('#history-icon' + o.attr('rel')).css({
				top: o.position().top - 25,
				opacity: 0
			}).animate({
				top: '+=5',
				opacity: 1
			});
		}, 200);
	});

	$('.history-year').click(function(e){
		e.preventDefault();
		$(this).blur();
		if(!$(this).hasClass('year-in')){
			var y = $(this).text(), id = $(this).attr('rel');
			$('#history-stuff .history-year').removeClass('year-in');
			$(this).addClass('year-in');
			$('#history-container .history-container').not('#history-container' + id).prependTo($('#history-container')).hide(200);
			$('#history-container' + id).show();
			$('#history-stuff .history-content').not('#history-content' + y).hide();
			$('#history-container .history-icon').fadeOut();
			$('#history-content' + y).animate({width: 'show'}, function(){
				var offset = $('#history-element' + id).offset();
				$('#history-icon' + id).show().css({
					top: offset.top - 25,
					left: offset.left + 2,
					opacity: 1
				}).animate({
					top: '+=5',
					opacity: 1
				}, 100);
			});
			$('#history-stuff .history-element').removeClass('history-element-chosen');
			$('#history-element' + id).addClass('history-element-chosen');
		}
	});

	$('.history-element').click(function(){
		var offset = $(this).offset(), id = $(this).attr('rel');
		$('#history-stuff .history-element').removeClass('history-element-chosen');
		$(this).blur().addClass('history-element-chosen');
		$('#history-container .history-container').not('#history-container' + id).prependTo($('#history-container')).hide(200);
		$('#history-container' + id).show();
		$('#history-container .history-icon').not('#history-icon' + id).animate({
			top: '-=5',
			opacity: 0
		}, 200, function(){
			$(this).hide();
		});
		$('#history-icon' + id).show();
		return false;
	}).hover(function(){
		if(!$(this).hasClass('history-element-chosen')){
			var offset = $(this).offset(), id = $(this).attr('rel');
			$('#history-icon' + id).css({
				top: offset.top - 25,
				left: offset.left + 2,
				opacity: 0
			}).show().animate({
				top: '+=5',
				opacity: 1
			}, 100);
		}
	}, function(){
		if(!$(this).hasClass('history-element-chosen')){
			var id = $(this).attr('rel');
			$('#history-icon' + id).animate({
				top: '-=5',
				opacity: 0
			}, 100, function(){
				$(this).hide();
			});
		}
	});

	$(window).resize(function(){
		var o = $('.history-element-chosen');
		$('#history-icon' + o.attr('rel')).css({
			left: o.position().left + 2,
		});
	});

	setTimeout(function(){
		var id = $('#history-stuff .year-in').attr('rel');
		var offset = $('#history-element' + id).offset();
		$('#history-icon' + id).show().delay(500).css({
			top: offset.top - 20,
			left: offset.left + 2,
		});
	}, 500);
});