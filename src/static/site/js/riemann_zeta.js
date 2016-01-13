// {Re[Zeta[1/2+I x]], Im[Zeta[1/2+I x]]}, 
// {x,-30, 30},

// AxesLabel->{"x"} , PlotStyle->{Red, Blue}, 
// Ticks->{Table[4x-28,{x,0,14}]}, 
// ImageSize->{800,600}], 
// Graphics[Text[Style[\[DoubleStruckCapitalR][\[Zeta][ I x + "1/2"]],14,Red ,Background ->White],{-22,2.6} ]], Graphics[Text[Style[\[GothicCapitalI][\[Zeta][ I x + "1/2"]],14,Blue ,Background ->White],{-14,2.6} ]]]

function CC(a,b) {
	return new numeric.T(a,b);
}

function zeta(z) {
	var I = CC(0,1);
	var half = CC(0.5, 0);
	var val = half.add( (I.mul(z)) );
	return new Array( val.x, val.y );
}

function zeta_list(list) {
	_.each(list, function(z) { return zeta(CC(z)); });
}

var domain = _.range(-30,31); 	// the set of ints such that -30 < x < 30 must be written like this!
var image = _.map(domain, function(z) { return zeta(CC(z)); });

console.log(image);
