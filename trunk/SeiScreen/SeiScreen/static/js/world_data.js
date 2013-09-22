function drawMarker(event, canvas) {
    var cxt = canvas.getContext('2d');
	var lat = event['lat'];
	var lon = event['lon'];
	var mag = event['mag'];
	var clr = event['color'];
	var ratio = 2.5;
	
    if (clr == 1) {
    	pic_color = '#f00'
    	ratio = 1
    }
    	
    else if (clr == 2) {
    	pic_color = '#ffff00'
	}
    
    else if (clr == 3) {
    	pic_color = '#00f';
    }
    
    else if (clr == 4) {
    	pic_color = '#f1f1f1';
   	}
    
    cxt.fillStyle = pic_color;
    
    var width = canvas.width;
    var height = canvas.height;
    
	var longitude = (width / 2) + ((lon * width) / 360.0);
	var latitude = (height / 2) - ((lat * height) / 180.0);

	cxt.beginPath();
	cxt.arc(longitude, latitude, mag / ratio, Math.PI * 2, 0, true);
	cxt.closePath();
	cxt.fill();
}

//data.global_event_list
function updateWorld(eventList, latestGlobal) {
	var canvas = $("#mapContainer")[0];	
	
	canvas.getContext('2d').clearRect(0, 0, canvas.width, canvas.height); 
	$.each(eventList, function(i, list) {
		if (i > 0) {
			drawMarker(this, canvas);
		}
		
		/*
		// Draw latest event last, so it shows at the top.
		if (i == (eventList.length - 1)) {
			drawMarker(eventList[0], canvas_circle);
		}
		*/
	});
	
	drawMarker(latestGlobal, canvas);	
}

function setupCanvas() {
    $("#mapContainer").height($("#mapContainer").width() / 2);
    $("#mapContainer")[0].width = $("#mapContainer").width();
    $("#mapContainer")[0].height = $("#mapContainer").height();  
}
