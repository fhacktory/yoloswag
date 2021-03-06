function invert_Lat_Lon(track)
{
    var ret = []
    $.each(track, function(i, item) {
	ret.push([item[1], item[0], item[2]]);
    });
    return ret
}

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
	url: 'static/img/start.png',
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
	url: 'static/img/end.png',
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

function route_display(track)
{
    var route = json_to_coord(track.points);
    var vpath = new google.maps.Polyline({
	path: route,
	geodesic: true,
	strokeColor: '#0000FF',
	strokeOpacity: 0.8,
	strokeWeight: 4,
	id_track: track.id
    });
    vpath.setMap(map);
    google.maps.event.addListener(vpath, 'click', function() {
	drawElevation(vpath.getPath());
    });
    var m_start = make_marker_start(track.points);
    var m_end = make_marker_end(track.points);
    m_start.setMap(map);
    m_end.setMap(map);
    gmarkers.push(m_start);
    gmarkers.push(m_end);
    gpaths.push(vpath);
}

function load_tracks(tracks, radius, distances, name)
{
    console.log(radius);
    console.log(distances);
    console.log(name);
    var regexp = new RegExp('.*' + name + '.*', 'gi');
    $.each(tracks, function(i, track) {
	start = new google.maps.LatLng(track.start[0], track.start[1]);
	if (name.length > 0){
	    if (track.name.match(regexp)){
		route_display(track);
	    }
	}   
	else if ((radius <= 0 || inRadius(currentPosition, start, radius))
	    && (track.distance >= distances[0] && track.distance <= distances[1]))
	{
	    route_display(track);
	}
    });
}
