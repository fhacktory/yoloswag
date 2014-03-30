var map;
var elevator;
var currentPosition;

var gpaths = new Array();
var gmarkers = new Array();

function initialize() {
    var mapOptions = {
	center: new google.maps.LatLng(45.750000, 4.850000),
	zoom: 12,
	mapTypeId: google.maps.MapTypeId.TERRAIN
    };
    map = new google.maps.Map(document.getElementById("map-canvas"), mapOptions);
    elevator = new google.maps.ElevationService();
    currentPosition = new google.maps.LatLng(45.750000, 4.850000);
    geolocation_setCurrentPosition();
    onLoad();
}

function refresh()
{
    console.log("REFRESSH");
    $.each(gpaths, function(i, path) {
	path.setMap(null);
//	delete path;
    });
    $.each(gmarkers, function(i, mark) {
	mark.setMap(null);
//	delete mark;
    });
    console.log("RELOAD");
    onLoad();
}

google.maps.event.addDomListener(window, 'load', initialize);
