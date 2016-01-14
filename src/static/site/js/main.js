
var Canvas = undefined;
var ctx = undefined;

$(document).ready(function() {
	$('[data-toggle=offcanvas]').click(function() {
		$('.row-offcanvas').toggleClass('active');
	});

	$('#sidebar').height($(window).height());

	Canvas = document.getElementById('big-canvas');

	if (Canvas != undefined) {
			
		Canvas.width = $(window).width() - 230;
		Canvas.height = $(window).height();
		console.log(Canvas);
		ctx = Canvas.getContext("2d");
		ctx.strokeStyle = "#333333";
		ctx.lineWidth = 1;

		// was to test that canvas works
		// for (var i=0; i<50; i++) {
		//    ctx.beginPath();
		//    ctx.moveTo(100,100);
		//    ctx.lineTo(300,300);
		//    ctx.lineTo(200,100);
		//    ctx.stroke();
		//}
	}

});