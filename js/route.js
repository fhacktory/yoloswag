function json_to_coord(track)
{
    var ret = []
    $.each(track, function(i, item) {
	ret.push(new google.maps.LatLng(item[0], item[1]));
    });
    return ret
}

function toggleBounce()
{
    if (this.getAnimation() != null)
	this.setAnimation(null);
    else
	this.setAnimation(google.maps.Animation.BOUNCE);
}

function make_marker_start(track)
{
    var image = {
	url: 'img/start.png',
	size: new google.maps.Size(32, 32),
	origin: new google.maps.Point(0,0),
	anchor: new google.maps.Point(10, 30)
    };
    var marker = new google.maps.Marker({
        icon: image,
	draggable:false,
	animation: google.maps.Animation.DROP,
	position: new google.maps.LatLng(track[0][0], track[0][1]),
        title: "start"
    });
    google.maps.event.addListener(marker, 'click', toggleBounce);
    return marker;
}

function make_marker_end(track)
{
    var image = {
	url: 'img/end.png',
	size: new google.maps.Size(32, 32),
	origin: new google.maps.Point(0,0),
	anchor: new google.maps.Point(10, 30)
    };
    var marker = new google.maps.Marker({
	icon: image,
	draggable:false,
	animation: google.maps.Animation.DROP,
	position: new google.maps.LatLng(track[track.length - 1][0], track[track.length - 1][1]),
	title: 'end'
    });
    google.maps.event.addListener(marker, 'click', toggleBounce);
    return marker;
}
      