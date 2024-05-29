$(document).ready(function(){
    $('#language_code').keypress(function(event){
        var keycode = (event.keyCode ? event.keyCode : event.which);
        if(keycode == '13'){
            fetchTranslation();
        }
    });
    
    $('#btn_translate').click(function(){
        fetchTranslation();
    });
    
    function fetchTranslation(){
        var languageCode = $('#language_code').val();
        $.ajax({
            url: 'https://www.fourtonfish.com/hellosalut/hello/',
            type: 'GET',
            dataType: 'json',
            data: { lang: languageCode },
            success: function(data){
                $('#hello').text(data.hello);
            },
            error: function(){
                $('#hello').text('Error: Unable to fetch translation.');
            }
        });
    }
});

