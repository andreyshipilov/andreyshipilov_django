// IE HTML5
/*@cc_on(function(i,a){var h="abbr|article|aside|audio|canvas|details|figcaption|figure|footer|header|hgroup|mark|meter|nav|output|progress|section|summary|time|video";function j(b){for(var a=-1;++a<k;)b.createElement(e[a])}function l(c,b){for(var d=-1,f=c.length,a,e=[];++d<f;){a=c[d];(b=a.media||b)!="screen"&&e.push(l(a.imports,b),a.cssText)}return e.join("")}var c=a.createElement("div");c.innerHTML="<z>i</z>";if(c.childNodes.length!==1){var e=h.split("|"),k=e.length,n=RegExp("(^|\\s)("+h+")","gi"),o=RegExp("<(/*)("+h+")","gi"),p=RegExp("(^|[^\\n]*?\\s)("+h+")([^\\n]*)({[\\n\\w\\W]*?})","gi"),m=a.createDocumentFragment(),f=a.documentElement;c=f.firstChild;var d=a.createElement("body"),g=a.createElement("style"),b;j(a);j(m);c.insertBefore(g,c.firstChild);g.media="print";i.attachEvent("onbeforeprint",function(){var j=-1,h=l(a.styleSheets,"all"),i=[],c;for(b=b||a.body;(c=p.exec(h))!=null;)i.push((c[1]+c[2]+c[3]).replace(n,"$1.iepp_$2")+c[4]);for(g.styleSheet.cssText=i.join("\n");++j<k;){h=a.getElementsByTagName(e[j]);i=h.length;for(c=-1;++c<i;)if(h[c].className.indexOf("iepp_")<0)h[c].className+=" iepp_"+e[j]}m.appendChild(b);f.appendChild(d);d.className=b.className;d.innerHTML=b.innerHTML.replace(o,"<$1font")});i.attachEvent("onafterprint",function(){d.innerHTML="";f.removeChild(d);f.appendChild(b);g.styleSheet.cssText=""})}})(this,document)@*/;

// ScrollTo
;(function(d){var k=d.scrollTo=function(a,i,e){d(window).scrollTo(a,i,e)};k.defaults={axis:'xy',duration:parseFloat(d.fn.jquery)>=1.3?0:1};k.window=function(a){return d(window)._scrollable()};d.fn._scrollable=function(){return this.map(function(){var a=this,i=!a.nodeName||d.inArray(a.nodeName.toLowerCase(),['iframe','#document','html','body'])!=-1;if(!i)return a;var e=(a.contentWindow||a).document||a.ownerDocument||a;return d.browser.safari||e.compatMode=='BackCompat'?e.body:e.documentElement})};d.fn.scrollTo=function(n,j,b){if(typeof j=='object'){b=j;j=0}if(typeof b=='function')b={onAfter:b};if(n=='max')n=9e9;b=d.extend({},k.defaults,b);j=j||b.speed||b.duration;b.queue=b.queue&&b.axis.length>1;if(b.queue)j/=2;b.offset=p(b.offset);b.over=p(b.over);return this._scrollable().each(function(){var q=this,r=d(q),f=n,s,g={},u=r.is('html,body');switch(typeof f){case'number':case'string':if(/^([+-]=)?\d+(\.\d+)?(px|%)?$/.test(f)){f=p(f);break}f=d(f,this);case'object':if(f.is||f.style)s=(f=d(f)).offset()}d.each(b.axis.split(''),function(a,i){var e=i=='x'?'Left':'Top',h=e.toLowerCase(),c='scroll'+e,l=q[c],m=k.max(q,i);if(s){g[c]=s[h]+(u?0:l-r.offset()[h]);if(b.margin){g[c]-=parseInt(f.css('margin'+e))||0;g[c]-=parseInt(f.css('border'+e+'Width'))||0}g[c]+=b.offset[h]||0;if(b.over[h])g[c]+=f[i=='x'?'width':'height']()*b.over[h]}else{var o=f[h];g[c]=o.slice&&o.slice(-1)=='%'?parseFloat(o)/100*m:o}if(/^\d+$/.test(g[c]))g[c]=g[c]<=0?0:Math.min(g[c],m);if(!a&&b.queue){if(l!=g[c])t(b.onAfterFirst);delete g[c]}});t(b.onAfter);function t(a){r.animate(g,j,b.easing,a&&function(){a.call(this,n,b)})}}).end()};k.max=function(a,i){var e=i=='x'?'Width':'Height',h='scroll'+e;if(!d(a).is('html,body'))return a[h]-d(a)[e.toLowerCase()]();var c='client'+e,l=a.ownerDocument.documentElement,m=a.ownerDocument.body;return Math.max(l[h],m[h])-Math.min(l[c],m[c])};function p(a){return typeof a=='object'?a:{top:a,left:a}}})(jQuery);

$(function(){
	$('body').css({
		'background-image': 'none'
	});

	var sideMenu = $('#side-menu');
	if(sideMenu.length){
		$('ul a', sideMenu).click(function(e){
			e.preventDefault();
			$(this).blur();
			$.scrollTo($($(this).attr('href')), 1000, {
				offset: -20
			})
		});
		sideMenu.data('initialOffset', sideMenu.offset().top);

		$(window).scroll(function(){
			if ($(this).scrollTop() < sideMenu.data('initialOffset')){
				sideMenu.css({
					'margin-top': 0,
					'position': 'absolute'
				});
			} else {
				sideMenu.css({
					'margin-top': -sideMenu.data('initialOffset'),
					'position': 'fixed'
				});
			}
		});
	}

	$('#copyright').click(function(e){
		e.preventDefault();
		var position = $(this).position();
		$('#copyright-full').fadeIn('fast').css({
			'left': position.left - 10,
			'top': position.top - $('#hide a').position().top + 4
		});
	});

	$('#copyright-full #hide').click(function(e){
		e.preventDefault();
		$('#copyright-full').fadeOut('fast');
	});
});