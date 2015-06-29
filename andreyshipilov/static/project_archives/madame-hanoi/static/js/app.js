// Browser check.
var $buoop = {c: 2};
function $buo_f() {
    var e = document.createElement("script");
    e.src = "//browser-update.org/update.js";
    document.body.appendChild(e);
};
try {
    document.addEventListener("DOMContentLoaded", $buo_f, false)
}
catch (e) {
    window.attachEvent("onload", $buo_f)
}

// Fonts.
WebFontConfig = {
    google: {families: ['PT+Serif:400italic:latin']}
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

// Dom ready.
$(function () {
    var $nav = $('#navigation'),
        $nav2 = $('#inner-navigation'),
        nav2waiting = true,
        $section = $('#menus'),
        $contact = $('#contact'),
        $address = $contact.find('.address-link'),
        prefix = 0,
        $allVideos = $('iframe[src^="//player.vimeo.com"], iframe[src^="//www.youtube.com"], object, embed'),
        clearVideosDimensions = function () {
            $allVideos.each(function (i, e) {
                $(e).attr('data-aspectRatio', e.height / e.width).removeAttr('height').removeAttr('width');
            });
        },
        makeVideosFluidOnResize = function () {
            var $fluidEl = $('figure.video'),
                newWidth = $fluidEl.width();

            $allVideos.each(function (i, e) {
                $(e).width(newWidth).height(newWidth * $(e).attr('data-aspectRatio'));
            });
        };

    clearVideosDimensions();
    $(window).resize(function () {
        makeVideosFluidOnResize();
    });
    window.setTimeout(function () {
        $(window).resize();
    }, 100);

    // Preload backgrouds.
    $.imgpreload([
        '/static/img/casino-mh-desktop-dining-breakfast.jpg',
        '/static/img/casino-mh-desktop-dining-allday.jpg',
        '/static/img/casino-mh-desktop-dining-dessert.jpg',
        '/static/img/casino-mh-desktop-dining-drinks.jpg',
        '/static/img/casino-mh-header-mh.jpg',
        '/static/img/casino-mh-header-nic.jpg'
    ]);

    // Init scroll.
    smoothScroll.init({
        'updateURL': false,
        'offset': 50
    });
    $.scrollIt({
        'topOffset': -50
    });

    // Simulate hover.
    $address.hover(function () {
        $contact.find('.icon-location-on').addClass('active');
    }, function () {
        $contact.find('.icon-location-on').removeClass('active');
    });

    // Set nav bar fixed.
    if ($nav.length && $nav.is(':visible')) {
        $(window).on('touchmove scroll', function () {
            prefix = $nav.hasClass('active') ? 50 : 100;

            if ($(window).scrollTop() + prefix > $section.position().top) {
                $nav.addClass('active');
                $section.addClass('active');
            } else {
                $nav.removeClass('active');
                $section.removeClass('active');
            }
        });
    }

    // Set menu block backgrounds.
    $('#menus').find('.menu').on('mouseover', function () {
        $('#menus').removeClass('bg-1 bg-2 bg-3 bg-4').addClass($(this).attr('id'));
    });

    // Set home button click.
    if (document.referrer.indexOf('madame') >= 0 && document.referrer.indexOf('hanoi') >= 0) {
        $('#back-to-home').on('click', function (e) {
            e.preventDefault();
            history.back();
        });
    }

    // Set nav bar timeout to hide.
    $(window).on('scroll', $.debounce(5000, function () {
        $nav2.addClass('hidden');
    }));
    $(window).on('scroll', function () {
        $nav2.removeClass('hidden');
    });

    var $more = $('#more'),
        $toTop = $('#to-top');

    $(document).on('scroll', function () {
        $(window).scrollTop() >= 200 ? $more.addClass('hidden') : $more.removeClass('hidden');
        $(window).scrollTop() >= $(window).height() - 50 ? $toTop.addClass('active') : $toTop.removeClass('active');
    });
});
