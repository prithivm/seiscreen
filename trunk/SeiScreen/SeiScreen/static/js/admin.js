$(document).ready(function() {
	
	$('.error_message').fadeOut(3000);
	
	$('.minus').click(function () {
		var $input = $(this).parent().find('input');
		var count = parseInt($input.val()) - 1;
	        
		if (isNaN(count)) 
	        	count = 'No';
	        
	    else
	    	count = count < 1 ? 1 : count;
	
	    $input.val(count);
	    $input.change();
	
	    return false;
	});

    $('.plus').click(function () {
    	var $input = $(this).parent().find('input');
            
        $input.val(parseInt($input.val()) + 1);
        var count = parseInt($input.val())
            
        if (isNaN(count)) {
            count = 'Yes';
            $input.val(count);
        }
		
        $input.change();

        return false;
    });

	$("#page_content").jScrollPane({showArrows:true, scrollbarWidth: 30, arrowSize: 30});
	
	$('#fetch_events').click(function() {
		var eventsUrl;
		var mthresh = $('#m_thresh').attr('value');
		var onlyLocal = $('#region_selector').attr('value');
		var days = $('#days').attr('value');
		
		if (onlyLocal == 'Yes')
			onlyLocal = 'true';
			
		else
			onlyLocal = 'false';
			
		eventsUrl = '/seiscreen/fetch-events/' + mthresh + '/' + days + '/' + onlyLocal + '/-1/';
		
		$('#events_block').html('');
		
		$.get(
			eventsUrl,
			function(data) {
  				$('#events_block').html(data);
  				
  				$('#print_button').click(function() {
  				    window.open(eventsUrl + 'true/', '_blank');
  				});
			}
		);
	});
	
	$('#save_settings').click(function() {
		var map_zoom = $('#map_zoom').attr('value');
		var minimap_zoom = $('#minimap_zoom').attr('value');
		var events_map = $('#events_map').attr('value');
		var events_minimap = $('#events_minimap').attr('value');
		var events_world = $('#events_world').attr('value');
		
		$('#fmap_zoom').attr('value', map_zoom);
		$('#fminimap_zoom').attr('value', minimap_zoom);
		$('#fevents_map').attr('value', events_map);
		$('#fevents_minimap').attr('value', events_minimap);
		$('#fevents_world').attr('value', events_world);
	});
});
        
