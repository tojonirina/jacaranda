$(document).ready(function () {

    var height = $(window).height();
    $('ul.leftmenu').css({'height':height});

    // Click on add user
    $('#add').on('click', function () {
        $('#background').css({'display':'block', 'transition':'display 1s linear'});
    });

    // Close add form
    $('#close').on('click', function () {
        $('#background').css({'display':'none', 'transition':'display 1s linear'});
    });

    $('select.type').change(function(){
        var type = $(this).val();
        if(type === 'old') {
            $('.old_field').show();
            $('.new_field').hide();
        } else if(type === 'new') {
            $('.old_field').hide();
            $('.new_field').show();
        } else {
            alert('error');
        }
    });

    
});