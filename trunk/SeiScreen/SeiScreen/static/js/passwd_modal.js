/* Taken from http://www.jacklmoore.com/notes/jquery-modal-tutorial */

var modal = (function(){
    var method = {};
    var $overlay;
    var $modal;
    var $content;
    var $close;

    // Center the modal in the viewport
    method.center = function () {
        var top, left;

        top = Math.max($(window).height() - $modal.outerHeight(), 0) / 2;
        left = Math.max($(window).width() - $modal.outerWidth(), 0) / 2;

        $modal.css({
            top:top + $(window).scrollTop(), 
            left:left + $(window).scrollLeft()
        });
    };

    // Open the modal
    method.open = function (settings) {
        $content.empty().append(settings.content);

        $modal.css({
            width: settings.width || 'auto', 
            height: settings.height || 'auto'
        });

        method.center();
        $(window).bind('resize.modal', method.center);
        $modal.show();
        $overlay.show();
    };

    // Close the modal
    method.close = function () {
        $modal.hide();
        $overlay.hide();
        $content.empty();
        $(window).unbind('resize.modal');
    };

    // Generate the HTML and add it to the document
    $overlay = $('<div id="overlay"></div>');
    $modal = $('<div id="modal"></div>');
    $content = $('<div id="content"></div>');
    $close = $('<a id="close" href="#">close</a>');

    $modal.hide();
    $overlay.hide();
    $modal.append($content, $close);

    $(document).ready(function(){
        $('body').append($overlay, $modal);	
    });

    $close.click(function(e){
        e.preventDefault();
        method.close();
    });

    return method;
}());

$(document).ready(function() { 
    modal.close();
    
    $('#pass_link').click(function() {        
        $.get(
            '/seiscreen/admin-password/',
            function(passwordMarkup) {
                if (passwordMarkup != '') {
                    modal.open({content: $(passwordMarkup), width: '300px', height: '250px'});
                    $('#change_error').hide();
                    $('#change_success').hide();
                    $('#change_message').hide();
                
                    $('#cpass_button').click(function() {
                        var curPass = $('#cur_pass').val();
                        var newPass = $('#new_pass').val();
                        var newPass2 = $('#new_pass2').val();
                        var csrfToken = $('[name="csrfmiddlewaretoken"]').val();
                
                        if (newPass === newPass2 && newPass && curPass) {
                            var passData = {
                                password: curPass,
                                new_password: newPass,
                                csrfmiddlewaretoken: csrfToken 
                            };
                            
                            console.log(passData);
                            
                            $.ajax({
                                url: '/seiscreen/change-password/',
                                type: 'POST',
                                data: passData,
                                dataType: 'json',
                                success: function(response) {
                                    console.log(response);
                                    if (response.success == 'true') {
                                        $('#change_success').show();
                                        $('#change_success').fadeOut(2000);
                                    }
                                    
                                    else {
                                        $('#change_message').empty().html(response.error_message);
                                        $('#change_message').show();
                                        $('#change_message').fadeOut(2000);
                                    }    
                                },
                                error: function() {
                                    $('#change_error').show();
                                    $('#change_error').fadeOut(2000);
                                }
                            });
                        }
                        
                        else {
                            $('#change_error').show();
                            $('#change_error').fadeOut(2000);
                        }
                    });
                }
            }
        );
    });
});
