/*

@author: Nino P. Cocchiarella
(c) 2016

General site-wide plerping-system
-startup routines

*/


// globals
window.artboard = undefined;
window.ctx = undefined;

// class ArtBoard {

function ArtBoard() {
	this.canvas = document.createElement('canvas');
	document.body.appendChild(this.canvas);
	this.adjust_size();

	window.ctx = this.canvas.getContext("2d");
}

ArtBoard.prototype.adjust_size = function() {
	console.log("adjust artboard sizes")
	this.canvas.width = $(window).width();
	this.canvas.height = $(window).height();
};

// } endclass ArtBoard



// site-wide startup routine
$(document).ready(function() {

	console.log("start iframe js app");
	artboard = new ArtBoard();

	start();

});