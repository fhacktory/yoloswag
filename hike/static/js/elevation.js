// Load the Visualization API and the columnchart package.
google.load('visualization', '1', {packages: ['corechart']});

function drawElevation(path) {

  // Create a new chart in the elevation_chart DIV.
    chart = new google.visualization.LineChart(document.getElementById('elevation_chart'));
    var a = path.j
    while (a.length > 256)
	a = a.filter(function(item, i){return (i % 2);});
    var pathRequest = {
	'path': a,
	'samples': 256
    }
    elevator.getElevationAlongPath(pathRequest, plotElevation);
}

function plotElevation(results, status) {
    if (status != google.maps.ElevationStatus.OK) {
	return;
    }
    var elevations = results;


    var elevationPath = [];
    for (var i = 0; i < results.length; i++) {
	elevationPath.push(elevations[i].location);
    }

  // Display a polyline of the elevation path.
//    var pathOptions = {
//	path: elevationPath,
//	opacity: 1,
//	map: map
//    }
//    polyline = new google.maps.Polyline(pathOptions);

  // Extract the data from which to populate the chart.
  // Because the samples are equidistant, the 'Sample'
  // column here does double duty as distance along the
  // X axis.
    var data = new google.visualization.DataTable();
    data.addColumn('string', 'Sample');
    data.addColumn('number', 'Elevation');
    $.each(results, function(i, point) {
	data.addRow(['', point.elevation]);
    });

  // Draw the chart using the data within its DIV.
    document.getElementById('elevation_chart').style.display = 'block';
    chart.draw(data, {
	height: 150,
	legend: 'none',
	titleY: 'Elevation (m)'
    });
}
