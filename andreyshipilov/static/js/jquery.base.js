// Fonts.
WebFontConfig = {
    google: {
        families: ['PT+Sans::cyrillic-ext,latin']
    }
};
(function () {
    var wf = document.createElement('script');
    wf.src = ('https:' == document.location.protocol ? 'https' : 'http') +
        '://ajax.googleapis.com/ajax/libs/webfont/1/webfont.js';
    wf.type = 'text/javascript';
    wf.async = 'true';
    var s = document.getElementsByTagName('script')[0];
    s.parentNode.insertBefore(wf, s);
})();

// DOM Ready.
$(function () {
    // Projects list resize.
    var maxCellSize = 220,
        cellWidth,
        selectedSelector,
        $projects = $('#projects'),
        $latest = $('.latest', $projects),
        $projectTypes = $('#project-types').find('a');

    $(window).resize(function () {
        cellWidth = 100 / Math.floor($projects.width() / maxCellSize);
        $latest.css({
            'width': cellWidth * 2 + '%'
        });
        $('.project', $projects).not($latest).width(cellWidth + '%');
    }).resize();

    // Projects filter.
    $projectTypes.click(function (e) {
        e.preventDefault();

        $(this).hasClass('selected') ? $(this).removeClass('selected').blur() : $(this).addClass('selected').blur();
        selectedSelector = '';
        $projectTypes.filter('.selected').each(function () {
            selectedSelector += '[rel*="' + $(this).attr('rel') + '"]';
        });

        if (selectedSelector === '') {
            $('.project', $projects).removeClass('selected');
        } else {
            $(selectedSelector, $projects).removeClass('selected');
            $('.project', $projects).not(selectedSelector).each(function (i, e) {
                window.setTimeout(function () {
                    $(e).addClass('selected');
                }, i * 5)
            });
        }
    });


    // Flickr restyling.
    /*
     var flickrHeight = 100;

     $('.flickr_badge_image').find('img').each(function (index) {
     if ($(this).height() < 90) {
     $(this).parents('.flickr_badge_image').remove();
     } else {
     flickrHeight = $(this).height() < flickrHeight ? $(this).height() : flickrHeight;
     }
     });

     $('.flickr_badge_image').find('a').each(function (index) {
     $(this).css({
     'margin-top': -($(this).height() - flickrHeight) * .5
     });
     }).hover(function () {
     var that = this;

     $('img', that).stop().animate({opacity: 0.2}, 100, function () {
     $('div', that).fadeIn(100);
     });
     }, function () {
     var that = this;

     $('img', that).stop().animate({opacity: 1}, 100, function () {
     $('div', that).fadeOut(100);
     });
     });

     // add hover div with title
     $('.flickr_badge_image').find('a').each(function () {
     var that = $(this);
     var marginTop = parseInt(that.css('marginTop').replace('px', ''));
     var titleHover = $('<div class="flickr_badge_title_hover"></div>').css('margin-top', -marginTop).append($('img', that).attr('title'));

     that.append(titleHover);
     });

     // set whole wrapper height
     $('#flickr_badge_uber_wrapper').css({
     'height': flickrHeight
     });
     */

    // Twitter table resize.
    var $twitterTable = $('#twitter').find('.table'),
        maxCells = Math.floor($twitterTable.width() / maxCellSize);

    $('td', $twitterTable).slice(0, maxCells - 1).addClass('v').removeClass('h');
    $('td[class*="v"]', $twitterTable).css({'width': 100 / ($('td[class*="v"]', $twitterTable).length) + '%'});

    $(window).resize(function () {
        var maxCells = Math.floor($twitterTable.width() / maxCellSize);

        if ($('td:first', $twitterTable).width() >= maxCellSize && $('td[class*="v"]', $twitterTable).length < maxCells) {
            $('td', $twitterTable).slice(0, maxCells - 1).addClass('v').removeClass('h');
            var width = 100 / ($('td[class*="v"]', $twitterTable).length) + '%';
            $('td[class*="v"]', $twitterTable).css({'width': width});
        } else if ($('td:first', $twitterTable).width() <= maxCellSize && $('td[class*="v"]', $twitterTable).length > maxCells) {
            $('td', $twitterTable).slice(maxCells - 1, $('td', $twitterTable).length - 1).addClass('h').removeClass('v');
            $('td[class*="v"]', $twitterTable).css({'width': 100 / $('td[class*="v"]', $twitterTable).length + '%'});
        }
    }).resize();

    // Twitter bar click.
    $('.info', $twitterTable).click(function () {
        window.location.href = 'https://twitter.com/andreyshipilov';
    });

    // Twitter Jesus background.
    $('.info', $twitterTable).css({
        'background-image': ['url("/s/img/jfk/jesus-', Math.floor(Math.random() * 6) + 1, '.jpg")'].join('')
    });
});
