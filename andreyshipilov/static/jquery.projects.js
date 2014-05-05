$(function(){
	// Projects list resize.
	var maxCellSize = 220;
	var projects = $('#projects');

	$(window).resize(function(){
		var cellWidth = 100 / Math.floor(projects.width() / maxCellSize);
		$('#latest-project').css({
			'width': cellWidth * 2 + '%',
			'height': 310
		});
		$('.project', projects).not('#latest-project').width(cellWidth + '%');
	});
	$(window).resize();

	// Projects filter.
	var projectTypes = $('#project-types a');

	projectTypes.click(function(){
		$(this).hasClass('selected') ? 	$(this).removeClass('selected').blur() : $(this).addClass('selected').blur();

		var selectedSelector = '';
		projectTypes.filter('.selected').each(function(){
			selectedSelector +='[rel*="' + $(this).attr('rel') + '"]';
		})
		if (selectedSelector == ''){
			$('.project', projects).animate({opacity: 1})
			$('.project .screenshot-count').show();
		} else {
			$(selectedSelector, projects).animate({opacity: 1});
			$('.project', projects).not(selectedSelector).animate({opacity: 0.2});
			$('.screenshot-count', $('.project', projects).not(selectedSelector)).hide();
		}
		return false;
	});

	$('#projects-container').css({
		opacity: 1,
		visibility: 'visible'
	});

	// Move screenshot count.
	$('.project .screenshot-count').css({
		'opacity': 0
	});
	$('.project').hover(function(){
		$('.screenshot-count', this).stop().animate({
			'right': 0,
			'opacity': 1
		}, 'fast')
	}, function(){
		$('.screenshot-count', this).stop().animate({
			'right': -150,
			'opacity': 0
		}, 'fast')
	});
});
