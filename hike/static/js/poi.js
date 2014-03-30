function get_poi_image(type)
{
    var image = {
	size: new google.maps.Size(32, 32),
	origin: new google.maps.Point(0,0),
	anchor: new google.maps.Point(10, 30),
    };
    switch (type)
    {
    case 0:
	image.url = 'static/img/poi.png';
	break;
    case 1:
	image.url = 'static/img/pov.png';
	break;
    case 2:
	image.url = 'static/img/source.png';
	break;
    case 3:
	image.url = 'static/img/watertap.png';
	break;
    case 4:
	image.url = 'static/img/pass.png';
	break;
    case 5:
	image.url = 'static/img/summit2.png';
	break;
    case 6:
	image.url = 'static/img/parking.png';
	break;
    }
    return image;
}

function poi_display(poi)
{
    var marker = new google.maps.Marker({
        icon: get_poi_image(poi.type),
	draggable:false,
//	animation: google.maps.Animation.DROP,
	position: new google.maps.LatLng(poi.position[0], poi.position[1]),
        title: poi.name
    });
    marker.setMap(map);
    gmarkers.push(marker);
}

function load_POIs(pois)
{
    $.each(pois, function(i, poi) {
	poi_display(poi);
    });
}
