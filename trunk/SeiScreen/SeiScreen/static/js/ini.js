jQuery(document).ready(function() {	
    setupCanvas();
	getData(); 
	startClock();
	setInterval('getData()', 15000);
	setInterval('startClock()', 1000);
	setInterval('update_time()', 10000);
});
