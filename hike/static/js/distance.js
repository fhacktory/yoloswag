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

function inRadius(from, marker, radius)
{
    var center = new google.maps.Marker({
	map: map,
	position: from
    });
//    circle = new google.maps.Circle({center:center.getPosition(),
//				     radius: radius,
//				     fillOpacity: 0.35,
//				     fillColor: "#FF0000",
//				     map: map});
    var bounds = new google.maps.LatLngBounds();
    var dist = google.maps.geometry.spherical.computeDistanceBetween(from, marker);
    if (dist < radius)
	return true;
    else
	return false;
}
