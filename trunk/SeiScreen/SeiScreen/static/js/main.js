//Globals         
var fromProjection = new OpenLayers.Projection('EPSG:4326');
var toProjection   = new OpenLayers.Projection('EPSG:900913');
                        
var markers;
var small_markers;
var blinky;
var event_counter = 0;
var latest_id;
var screenReady = 0;
var global_unixtime;
var local_array = new Array();
var audio_info;
var times_played = 0;
var barSequence = new Array();
var barItems = new Array();
var seqCount = 0;
var seqCurrent = 0;
var barInterval = 0;
var settingsRefresh = 0;
var smallMapOne;
var smallMapTwo;
var smallMapThree;
var smallMapFour;
var smallMapFive;
var smallMaps = [];
var backupServers = [];
var serverCounter = 0;
var tryCounter = 0;

jQuery.fn.reverse = [].reverse;

barSequence = [
	{item: 0, interval: 7}, 
	{item: 1, interval: 7},
	{item: 0, interval: 7},
	{item: 1, interval: 7},
	{item: 2, interval: 5},
	{item: 0, interval: 7},
	{item: 1, interval: 7},
	{item: 0, interval: 7},
	{item: 1, interval: 7},
	{item: 2, interval: 5},
	{item: 3, interval: 5},
	{item: 4, interval: 5},
	{item: 5, interval: 5},
];

var lastEvent = {
	event_counter:0,
	server:''
}

function getNiceDate(date) {
    return date.getDate() + '/' + (date.getMonth() + 1) + '/' + date.getFullYear() + ' - ' + date.getHours() + ':' + date.getMinutes();
}

function update_time() {
	var global_timeago = $.timeago(global_unixtime); 

	$('#global_ago').html(global_timeago);
}

function getMarkerForMag(mag) {
	var marker;
	var number;
	var size;
	
	if (mag > 0 && mag <= 4) {
		number = 4; 
		size = 14;
	}               
	  
	else if (mag > 4 && mag <= 6) {
		number = 3; 
		size = 22;
	}
	
	else if (mag > 6 && mag <= 7) {
		number = 2; 
		size = 30;
	}                
	               
	else if (mag > 7 && mag <= 10) {
		number = 1; 
		size = 46;
	}
	
	marker = {
		number: number,
		size: size
	}
	
	return marker;
}

function locateLocalEvents() {
    map.getLayersByName('local_markers')[0].clearMarkers();
    for (var i = 0; i < local_array.length; i++) {
        var mapIndex = i + 1;
        var timeAgo = $.timeago(local_array[i].time * 1000);
        var lon = local_array[i].lon;
        var lat = local_array[i].lat;
        var mag = Math.round(local_array[i].mag * 10 ) / 10;
        var region = local_array[i].region;
        var timeAgo = $.timeago(local_array[i].time * 1000);
        var iconSource = '/static/img/geo-' + mapIndex + '.png'; 
        smallMaps[i].setCenter(
            new OpenLayers.LonLat(
                local_array[i].lon,
                local_array[i].lat
            ).transform(fromProjection, toProjection),
            small_map_zoom
        );

        var marker = new OpenLayers.Marker(
            new OpenLayers.LonLat(lon, lat).transform(fromProjection, toProjection),
            new OpenLayers.Icon(
                iconSource,
                new OpenLayers.Size(13, 18),
                new OpenLayers.Pixel(-13 / 2, -18)
            )
        );

        smallMaps[i].getLayersByName('local')[0].clearMarkers();
        smallMaps[i].getLayersByName('local')[0].addMarker(
            new OpenLayers.Marker(
                new OpenLayers.LonLat(lon, lat).transform(fromProjection, toProjection),
                new OpenLayers.Icon(
                    iconSource,
                    new OpenLayers.Size(13, 18),
                    new OpenLayers.Pixel(-13 / 2, -18)
                )
            )
        );
        map.getLayersByName('local_markers')[0].addMarker( 
            new OpenLayers.Marker(
                new OpenLayers.LonLat(lon, lat).transform(fromProjection, toProjection),
                new OpenLayers.Icon(
                    iconSource,
                    new OpenLayers.Size(13, 18),
                    new OpenLayers.Pixel(-13 / 2, -18)
                )
            )
        );

        $('#info-' + mapIndex).html('<strong>M</strong>' + mag +
                                    ' - ' + timeAgo + '<br>' + region); 
    }
}

function update_latest(data) {
    var global_mag = Math.round(data.latest_global.mag * 10) / 10;
    var global_depth = Math.round(data.latest_global.depth);
    var global_time = new Date(data.latest_global.time * 1000);
    var global_stations = data.latest_global.stations
    var global_status = data.latest_global.status
    var globalTime = getNiceDate(global_time)
    var worldMagClr = Math.round(data.latest_global.mag * 10) / 10;
    
    $('#Gvalue1').html(global_mag);
    $('#Gdepth1').html(global_depth);
    $('#Gtime1').html(globalTime);
    $('#Gstations1').html(global_stations);
    $('#Gstatus1').html(global_status);
    
	var worldMag = '<span style="color:#ff0000">' + worldMagClr + '</span>';
	var latest_global_time = new Date(data.latest_global.time * 1000);
	global_unixtime = latest_global_time;
	var world_title_text = 'M ' + worldMag + ', ' + data.latest_global.region + '<br>'; //+ GtimeAgo;
	
	$('#global_info').html(world_title_text);

	update_time();
	updateWorld(data.global_event_list, data.latest_global);
}


function tryServer(serverNumber) {
    var url;
    var nServers = backupServers.length;

    if (serverNumber >= nServers)
        serverNumber = 0;

    var nextServer = backupServers[serverNumber];
    url = nextServer.address + '/update/';
    $.get(url, function(data) {
        location.href = nextServer.address + '/screen/';
    });
}

function getCurrentServer() {
    var serverFound = false;
    var currentServer = 0;
    var nServers = backupServers.length;
    
    for (var i = 0; i < nServers; i++) {
        var indexIn = location.href.indexOf(backupServers[i].address);
        if (indexIn >= 0) {
            serverFound = true;
            currentServer = i;
            break;
        }
    }

    if (serverFound == false) {
        currentServer = 0;
    }

    return currentServer;
}

function nextServerNumber() {
    tryCounter++;
    var nextServer = getCurrentServer() + tryCounter;

    if (nextServer >= backupServers.length) {
        nextServer = 0;
        tryCounter = 0;
    }

    return nextServer;
}

$(document).ready(function() {
	barItems[0] = $('#bar_llocal');
	barItems[1] = $('#bar_lglobal');
	barItems[2] = $('#bar_logo');
	barItems[3] = $('#bar_inst');
	barItems[4] = $('#bar_mlegend');
	barItems[5] = $('#bar_clegend');
	
	seqCount = barSequence.length;
	
	for(var item = 0; item < barItems.length; item++)
		barItems[item].hide();
	
	seqCurrent = seqCount - 1;
	changeBar();
});

function getData() {
    $.ajax({
		cache: false,
		success: function(data) {
			if (screenReady == 0) {
				
				screenReady = 1;
				Glat = data.global_positioning.center_lat;
				Glon = data.global_positioning.center_lon;
				bound_l = data.global_positioning.bound_l;
				bound_b = data.global_positioning.bound_b;
				bound_r = data.global_positioning.bound_r;
				bound_t = data.global_positioning.bound_t;
				map_zoom = data.global_positioning.zoom_mainmap;
				small_map_zoom = data.global_positioning.zoom_minimap;
				map(Glon, Glat, bound_l, bound_b, bound_r, bound_t, map_zoom, small_map_zoom);	
    			
    			var screenHeight = $('#screen').height()
    			$('#screen').css('font-size', screenHeight / 10 + 'px');
            }

            tryCounter = 0;
            backupServers = data.servers;

            if (getCurrentServer() != 0) {
                tryServer(0)
            }

			//Connection Status Data	
		    var status = data.connection_status.status;
            var statusImage;
		    if (status == 1)
               statusImage = '/static/img/signal_high.png';
		    
		    else if (status == 2)
               statusImage = '/static/img/signal_medium.png';
		    
		    else if (status == 3)
               statusImage = '/static/img/signal_low.png';
		    
		    $('#signal').attr('src', statusImage);

		    if (settingsRefresh == 0) 
		        settingsRefresh = data.settings_change;

		    
		    else if (data.settings_change > settingsRefresh)
		        location.reload(true);
		    
			latest_id = data.global_event_list[0].id;
			latest_server = data.server
            locateLocalEvents();
		
			if (latest_id > lastEvent.event_counter || latest_server != lastEvent.server) {
				lastEvent.event_counter = latest_id;
				lastEvent.server = latest_server;
				
				update_latest(data)

		        var local_mag = Math.round(data.latest_local.mag * 10) / 10;
			    var local_depth = Math.round(data.latest_local.depth);
			    var local_time = new Date(data.latest_local.time * 1000);
			    var local_stations = data.latest_local.stations;
			    var local_status = data.latest_local.status;
			    var locatlTime = getNiceDate(local_time);
			    
			    $('#value1').html(local_mag);
			    $('#depth1').html(local_depth);
			    $('#time1').html(locatlTime);
			    $('#stations1').html(local_stations);
			    $('#status1').html(local_status);
			    
			    local_array = data.latest_local_list;
			               
				markers.clearMarkers();
				$.each(data.local_event_list.reverse(), function(i, list) {    
			        var lat = this['lat'];
			        var lon = this['lon'];
			        var mag = this['mag'];
			        var clr = this['color'];
			        var pic_number, pic_size;
			    
					//Marker Creation
					
					var marker = getMarkerForMag(mag);
			        pic_number = marker.number;
			        pic_size = marker.size;
			        			                   
			        if (clr == 1) {
			            pic_color = 'red';
			            var marker_path = '/static/img/red_circle' + marker.number + '.png';
			            $('#local_marker').attr('src', marker_path);
			        }
                
                    else if (clr == 2) {
                        pic_color = 'blue';
                    }
                    
                    else {
                        pic_color = 'gray';
                    }
                    
                    markers.addMarker(new OpenLayers.Marker(
                        new OpenLayers.LonLat(lon,lat).transform(fromProjection, toProjection), 
                        new OpenLayers.Icon(
                                '/static/img/' + pic_color + '_circle' + pic_number + '.png',
                                new OpenLayers.Size(pic_size, pic_size),
                                new OpenLayers.Pixel(-(pic_size / 2), -(pic_size / 2))
                        )
                    ));
				});
				
				var audio_source = '/seiscreen/audio/' + latest_id + '.mp3'
				audio_info = new Audio(audio_source);
				audio_info.play();  
			}
			
			else {
				update_latest(data)
			}
		},
	    error: function() {
			$('#signal').html('<img src="/static/img/signal_low.png" />');
            tryServer(nextServerNumber());
		},
	 	url: '/seiscreen/update/'
	});
}

function map(Glon, Glat, bound_l, bound_b, bound_r, bound_t, map_zoom, small_map_zoom) {
    var extent = new OpenLayers.Bounds(bound_l, bound_b, bound_r, bound_t).transform(fromProjection,toProjection);

	map = new OpenLayers.Map('basicMap', {
        controls: [
        ]
	});

	map.addLayer(new OpenLayers.Layer.OSM());
	map.setCenter(new OpenLayers.LonLat(Glon, Glat).transform(fromProjection, toProjection), map_zoom);

    cacheWrite = new OpenLayers.Control.CacheWrite({
    	autoActivate: true,
    	imageFormat: 'image/jpeg',
	});

	cacheRead = new OpenLayers.Control.CacheRead();
	map.addControl(cacheWrite);
	map.addControl(cacheRead);
		
	markers = new OpenLayers.Layer.Markers('markers');
    localMarkers = new OpenLayers.Layer.Markers('local_markers');
    
	map.addLayer(markers);
    map.addLayer(localMarkers);

    if (smallMaps.length == 0) {    
        smallMaps.push(smallMapOne);
        smallMaps.push(smallMapTwo);
        smallMaps.push(smallMapThree);
        smallMaps.push(smallMapFour);
        smallMaps.push(smallMapFive);
        for (var i = 0; i < smallMaps.length; i++) {
            mapIndex = i + 1;
            smallMaps[i] = new OpenLayers.Map(
                'local-' + mapIndex, {
                    restrictedExtent: extent,
                    controls: [
                        new OpenLayers.Control.Navigation(),
                        new OpenLayers.Control.Attribution()
                    ],
                    maxResolution: 'auto'
                }
            );

            smallMaps[i].addLayer(new OpenLayers.Layer.OSM());
            smallMaps[i].addLayer(new OpenLayers.Layer.Markers('local'));
            smallMaps[i].setCenter(new OpenLayers.LonLat(Glon, Glat).transform(fromProjection, toProjection), small_map_zoom);
        }
    }
}

function changeBar() {
	var nindex;
	var cindex = seqCurrent;

	if (seqCurrent + 1 >= seqCount)
		nindex = 0;
		
	else
		nindex = seqCurrent + 1;

	var citem = barSequence[cindex].item;
	var nitem = barSequence[nindex].item;
	var interval = barSequence[nindex].interval * 1000;
	
	barItems[citem].fadeOut(100);
	barItems[nitem].fadeIn(100);
	
	seqCurrent = nindex;
	
	if (barInterval != 0)
		clearInterval(barInterval);
		
	barInterval = setInterval('changeBar()', interval);
}

function startClock(){
    var nd = new Date();
    var h, m, s;
    var time = ' ';
    
	h = nd.getHours();
	m = nd.getMinutes();
	s = nd.getSeconds();
		
	if (h <= 9)
		h = '0' + h;
	
	else if (m <= 9) 
		 m = '0' + m;
	
	else if (s <= 9) 
		s = '0' + s;
	
	time += h + ':' + m + ':' + s; 
	$("#time").html(time);		
};
