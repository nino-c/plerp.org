"""

@author: Nino P. Cocchiarella
(c) 2016

General site-wide plerping-system
-startup routines

"""


# globals
window.artboard = null
window.ctx = null



class ArtBoard

	constructor: () ->

		@canvas = document.createElement 'canvas'
		document.body.appendChild @canvas
		@adjust_size();

		window.ctx = @canvas.getContext("2d")

	adjust_size: () ->
		console.log("adjust artboard sizes")
		@canvas.width = $(window).width()
		@canvas.height = $(window).height()



$(document).ready ->

	console.log("start iframe js app");
	window.artboard = new ArtBoard();

	window.start()

