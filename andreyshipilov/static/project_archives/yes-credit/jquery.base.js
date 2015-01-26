// Preload images
(function(a){var b=[];a.extend({preload:function(f,g){var e=a.extend({init:function(){},loaded:function(){},loaded_all:function(){}},g),d=f.length,c=0;e.init(0,d);for(var h in f)b.push(a("<img />").attr("src",f[h]).load(function(){c++;e.loaded(this,c,d);c==d&&e.loaded_all(c,d)}))}})})(jQuery);

$.preload([
	   'm/index-mac.png',
	   'm/index-left-boy.png',
	   'm/index-right-boy.png',
	   'm/index-billboard.png',
	   'm/index-cloud.png',
	   'm/index-car.png',
	   'm/index-girl.png',
	   'm/index-button.png',
	   'm/index-curtain.png',
], {
	loaded_all: function(loaded, total){
		//$('#home').css({'overflow-x': 'hidden'});
		// Index animation
		$('#index-billboard').css({'margin-left': '+=1500'}).show().animate({'margin-left': '-=1500'}, 400);
		$('#index-mac').css({'right': '-=1500'}).show().delay(150).animate({'right': '+=1500'}, 400);
		$('#index-right-boy').css({'right': '-=1500'}).show().delay(300).animate({'right': '+=1500'}, 400);
		$('#index-left-boy').css({'left': '-=1500'}).show().delay(450).animate({'left': '+=1500'}, 400);
		$('#index-girl').css({'margin-left': '-=1000'}).show().delay(600).animate({'margin-left': '+=1000'}, 400);
		$('#index-car').css({'margin-left': '-=1500'}).show().delay(750).animate({'margin-left': '+=1500'}, 400);
		$('#index-cloud').css({'top': '-=1000'}).show().delay(1000).animate({'top': '+=1000'}, 400);
		$('#index-button').css({'bottom': '+=1000'}).show().delay(1150).animate({'bottom': '-=1000'}, 400, function(){
			//$('body').css({'overflow': 'visible'});
		});
	}
});

$(function(){
	var hasFlash = true;
	// Index flash
	flashembed("flash-content", {
		'src': "./yescredit-flash.swf",
		'version': [9],
		'wmode': 'transparent',
		//'width': '640',
		//'height': '470',
		onFail: function(){
			hasFlash = false
			$('#index-button').click(function(){
				window.open('m/video/YESCredit.mov') // Path to MOV file
			});
		}
	});

	// About right block adjust
	setTimeout(function(){
		var mainBlock = $('#about2'), rightBlock = $('#about2-right');
		rightBlock.animate({'height': mainBlock.height() - 3});
	}, 500);

	if (hasFlash){
		$('#index-button').click(function(e){
			//$('body').css({'overflow': 'hidden'});
			e.preventDefault();
			$('#index-mac').animate({'right': '-=1500'});
			$('#index-right-boy').animate({'right': '-=1500'});
			$('#index-left-boy').animate({'left': '-=1500'});
			$('#index-girl').animate({'margin-left': '-=1000'});
			$('#index-car').animate({'margin-left': '-=1500'});
			$('#index-cloud').animate({'top': '-=1000'});
			$('#index-button').animate({'bottom': '+=1000'}, 500, function(){
				$('#curtain-left').animate({'width': '50%'});
				$('#curtain-right').animate({'width': '50%'}, function(){
					$('#video-close').hide();
					$('#video').fadeIn(function(){
						$('#video-close').fadeIn();
					});
				});
			});
		});
	}

	// Function for flash
	closeVideo = function(){
			$('#video').fadeOut(function(){
				$('#curtain-left').animate({'width': '0%'});
				$('#curtain-right').animate({'width': '0%'}, function(){
					$('#index-mac').animate({'right': '+=1500'}, 400);
					$('#index-right-boy').animate({'right': '+=1500'}, 400);
					$('#index-left-boy').animate({'left': '+=1500'}, 400);
					$('#index-girl').animate({'margin-left': '+=1000'}, 400);
					$('#index-car').animate({'margin-left': '+=1500'}, 400);
					$('#index-cloud').animate({'top': '+=1000'}, 400);
					$('#index-button').animate({'bottom': '-=1000'}, 400, function(){
						//$('body').css({'overflow': 'visible'});
					});
				});
			});
	};	
	$('#video').click(function(e){
		e.preventDefault();
		closeVideo();
	});

	$(document).keyup(function(e) {
		if ($('#video').is(':visible')){
			if (e.keyCode == 27){
				closeVideo();
			}
		}
	});

	// Pencils
	/*
	$('#penciled1').hover(function(){
		$('.pencil', this).stop().animate({
			'opacity': 1,
			'left': '100%'
		}, 500, 'linear');
		$('.overlay', this).animate({
			'right': -605
		}, 500);
	}, function(){
		$('.pencil', this).stop().animate({
			'left': '0%',
			'opacity': 0
		}, 500, 'linear');
		$('.overlay', this).animate({
			'right': 0
		}, 500);
	});
	*/

	$('.penciled').hover(function(){
		$('.overlay', this).stop().animate({
			'right': -605
		}, 500);
	}, function(){
		$('.overlay', this).stop().animate({
			'right': 0
		}, 500);
	});
});