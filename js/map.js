var map;

function initialize() {
    var mapOptions = {
	center: new google.maps.LatLng(45.750000, 4.850000),
	zoom: 8,
	mapTypeId: google.maps.MapTypeId.TERRAIN
    };
    map = new google.maps.Map(document.getElementById("map-canvas"), mapOptions);
    var track = [[45.7500, 4.8500],[46.7500, 4.8500],[47.7500, 5.8500],[44.7500, 5.8500],[44.7500, 3.8500]];
    route_display(track);
}
google.maps.event.addDomListener(window, 'load', initialize);
