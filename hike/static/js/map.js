var map;

function initialize() {
    var mapOptions = {
	center: new google.maps.LatLng(45.750000, 4.850000),
	zoom: 12,
	mapTypeId: google.maps.MapTypeId.TERRAIN
    };
    map = new google.maps.Map(document.getElementById("map-canvas"), mapOptions);
    load_tracks();
    load_POIs();
}
google.maps.event.addDomListener(window, 'load', initialize);
