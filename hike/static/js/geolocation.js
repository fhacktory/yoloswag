function geolocation_onError(error){    
    console.log(error);
}

function geolocation_onSuccess(position){
    currentPosition = position.coords;
    map.panTo(new google.maps.LatLng(position.coords.latitude, position.coords.longitude));
    map.setZoom(15);
    var marker = new google.maps.Marker({
	draggable:false,
	animation: google.maps.Animation.DROP,
	position: new google.maps.LatLng(position.coords.latitude, position.coords.longitude),
        title: "You"
    });
    marker.setMap(map);
}

function geolocation_setCurrentPosition()
{
    navigator.geolocation.getCurrentPosition(geolocation_onSuccess, geolocation_onError);
}