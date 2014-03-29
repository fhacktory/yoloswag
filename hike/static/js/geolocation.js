function geolocation_onError(error){
    console.log(error);
}

function geolocation_onSuccess(position){
    map.panTo(new google.maps.LatLng(position.coords.latitude, position.coords.longitude));
    map.setZoom(15);
}

function geolocation_setCurrentPosition()
{
    navigator.geolocation.getCurrentPosition(geolocation_onSuccess, geolocation_onError);
}