$(document).ready(function() {
    getEvents();
    setInterval('getEvents()', 10000);
});

function getEvents() {
    var eventsUrl = '/seiscreen/fetch-events/0/100/false/10/'
    
    $.get(
        eventsUrl,
        function(data) {
            $('#events_block').empty().html(data);
            
            $('#print_button').click(function() {
                window.open(eventsUrl + 'true/', '_blank');
            });
        }
    );
}
