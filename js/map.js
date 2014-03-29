function initialize() {
    var mapOptions = {
	center: new google.maps.LatLng(45.750000, 4.850000),
	zoom: 8,
	mapTypeId: google.maps.MapTypeId.TERRAIN
    };
    var map = new google.maps.Map(document.getElementById("map-canvas"),
				  mapOptions);
    var track = [[45.7500, 4.8500],[46.7500, 4.8500],[47.7500, 5.8500],[44.7500, 5.8500],[44.7500, 3.8500]];
    var route = json_to_coord(track);
    var m_start = make_marker_start(track);
    var m_end = make_marker_end(track);
    m_start.setMap(map);
    m_end.setMap(map);

    var flightPath = new google.maps.Polyline({
	path: route,
	geodesic: true,
	strokeColor: '#0000FF',
	strokeOpacity: 0.8,
	strokeWeight: 4
    });
    flightPath.setMap(map);
}
google.maps.event.addDomListener(window, 'load', initialize);
