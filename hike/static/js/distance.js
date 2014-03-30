function distance_calculate(track, mode) {
    var service = new google.maps.DistanceMatrixService();
    path = json_to_coord(track);
    service.getDistanceMatrix(
	{
	    origins: [path[0]],
	    destinations: [path[path.length - 1]],
	    travelMode: mode,
	    unitSystem: google.maps.UnitSystem.METRIC,
	    avoidHighways: true,
	    avoidTolls: true
	}, distance_callback);
}

function distance_callback(response, status) {
    if (status != google.maps.DistanceMatrixStatus.OK) {
	alert('Error was: ' + status);
    } else {
	var origins = response.originAddresses;
	var destinations = response.destinationAddresses;
	var distinfo = document.getElementById('distance_info');
	distinfo.innerHTML = '';
//	deleteOverlays();
	$.each(origins, function(i, src) {
	    var results = response.rows[i].elements;
	    //	    addMarker(origins[i], false);
	    $.each(results, function(j, dest) {
		//		addMarker(destinations[j], true);
		distinfo.innerHTML += src + ' to ' + destinations[j]
		    + ': ' + dest.distance.text + ' in '
		    + dest.duration.text + '<br>';
	    });
	});
    }
//    return [dest.distance, dest.duration];
}

function codeAddress()
{
    var address = document.getElementById('address').value;
    var radius = parseInt(document.getElementById('radius').value, 10) * 1000;
    geocoder.geocode( { 'address': address}, function(results, status) {
	if (status == google.maps.GeocoderStatus.OK) {
	    map.setCenter(results[0].geometry.location);
	    var marker = new google.maps.Marker({
		map: map,
		position: results[0].geometry.location
	    });
	    if (circle) circle.setMap(null);
	    circle = new google.maps.Circle({center:marker.getPosition(),
					     radius: radius,
					     fillOpacity: 0.35,
					     fillColor: "#FF0000",
					     map: map});
	    var bounds = new google.maps.LatLngBounds();
	    for (var i=0; i<gmarkers.length;i++) {
		if (google.maps.geometry.spherical.computeDistanceBetween(gmarkers[i].getPosition(),marker.getPosition()) < radius) {
		    bounds.extend(gmarkers[i].getPosition())
		    gmarkers[i].setMap(map);
		} else {
		    gmarkers[i].setMap(null);
		}
	    }
	    map.fitBounds(bounds);

	} else {
	    alert('Geocode was not successful for the following reason: ' + status);
	}
    });
}