function $(v) {return(document.getElementById(v))}

var prefix = 'link'
var postfix = 'area'
var delimiter = '_'
var oldonload = window.onload
window.onload = typeof window.onload != 'function' ? make : function () {oldonload(); make()}

//
function make(){
	var links = document.getElementsByTagName('a')
	var re = new RegExp(prefix + '\\d+\\' + delimiter + '\\d+')
	for (var i=0; i<links.length; i++){
		var link = links[i];
		if (link.getAttribute('href') && re.test(link.getAttribute('rel'))){
			link.className = link.rel.substring(link.rel.indexOf(delimiter) + 1) > 1 ? 'dashed' : 'nondashed'
			var area = postfix + link.rel.substring(prefix.length,link.rel.indexOf('_'))
//			$(area + delimiter + i).style.display = 'none'
			link.onclick = function () {check(this,area); this.blur(); return false}
		}
	}
}

//
function check(obj,area){
	var group = obj.rel.substring(prefix.length,obj.rel.indexOf('_'))
	var element = obj.rel.substring(obj.rel.indexOf(delimiter) + 1)
	var cLinks = document.getElementsByTagName("a");
	var cRe = new RegExp(prefix + group + '\\' + delimiter + '\\d+')
	for (var i=0; i<cLinks.length; i++){
		var cLink = cLinks[i];
		if (cRe.test(cLink.getAttribute('rel')) && cLink.getAttribute('rel') == prefix + group + delimiter + element){
			cLink.className = 'nondashed'
			$(postfix + group + delimiter + element).style.display = 'block'
		} else {
			cLink.className = cRe.test(cLink.getAttribute('rel')) ? 'nondashed' : ''
			if(cRe.test(cLink.getAttribute('rel'))){
//				$(postfix + group + delimiter + eval(i+1)).style.display = 'none'
				cLink.className = 'dashed'
			}
		}
	}
}
