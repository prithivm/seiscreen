var globeReady = 0;

//data.global_event_list
function updateWorld(eventList, latestGlobal) {
	if (globeReady == 0) {
		getGlobe();
		globeReady = 1;
	}
		
	var globe_markers = []; 
	$.each(eventList, function(i, list) {
		var e_lat = this['lat'];
		var e_lon = this['lon'];
		var e_mag = this['mag'];			                                
                    
		if (e_mag > 0 && e_mag <= 6) {color=1}        
        if (e_mag > 6 && e_mag <= 10) {color=0}
				
		globe_markers.push(e_lat,e_lon,e_mag,color);
		globe.addData(globe_markers,{format : 'legend'});
		globe.createPoints();
	});
}
	

function getGlobe() {
	if (!Detector.webgl) {
		Detector.addGetWebGLMessage();
	}
	 
    else {    
        var container = document.getElementById('globeContainer');
        
		globe = new DAT.Globe(container, function(label) {
        	return new THREE.Color([0xff0000, 0x0000ff][label]);
        });     
	}
                
    globe.animate();
                
	if (globe != undefined) {
		setInterval('globe.autoRotation(globe.target.x-0.01, 0)', 111);
	}
}