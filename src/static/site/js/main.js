/*

@author: Nino P. Cocchiarella
(c) 2016

General site-wide plerping-system
-startup routines

*/

function print(x) {
	console.log(x);
}

// function adjust_sidebar() {

// 	console.log('adjust sidebar height');
// 	var sidebar = $("#sidebar");
// 	sidebar.height( $(window).height() );
	

// 	var canvas_iframe = $("#big-canvas");
// 	canvas_iframe.width( $(window).width() - sidebar.width() );
// 	canvas_iframe.height( $(window).height() );

// }



// site-wide startup routine
$(document).ready(function() {

	print("start main js app");
	var canvas_iframe = $("#big-canvas");
	//canvas_iframe.css({'top':'50px'});
	canvas_iframe.width( $(window).width() );
	canvas_iframe.height( $(window).height() );


	// for the sidebar, from "Edge"
	$('[data-toggle=offcanvas]').click(function() {
		$('.row-offcanvas').toggleClass('active');
	});


});