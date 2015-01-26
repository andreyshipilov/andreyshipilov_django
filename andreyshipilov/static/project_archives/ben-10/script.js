$(document).ready(function (){
    //$.squidy({head_img: 'ben10.png'});

    /* Logo action */
    $('.logo').click(function (){
        $(this).blur();
        $('.step-1, .step-2, .step-3, .step-4').hide();
        $('.oyna-button').hide().removeClass('oyna-clicked');
        $('.flash').show();
        return false;
    })

    /* Geri Ileri buttons */
    $('.toStep1').click(function (){
        $('.step-2, .step-3, .step-4').hide();
        $('.step-1').show();
        return false;
    })
    $('.toStep2').click(function (){
        $('.step-1, .step-3, .step-4').hide();
        $('.step-2').show();
        return false;
    })
    $('.toStep3').click(function (){
        $('.step-1, .step-2, .step-4').hide();
        $('.step-3').show();
        return false;
    })
    $('.toStep4').click(function (){
        $('.step-1, .step-2, .step-3').hide();
        $('.step-4').show();
        $.nyroModalManual({
            url: '#flash-game' + $('#flash-game-id').val(),
            endRemove: function() {$('.step-3').show()}
        });
        return false;
    })
    
    /*  Character selection */
    $('.char-1, .char-2, .char-3').click(function (){
        $('.char-1, .char-2, .char-3').removeClass('char-clicked');
        $(this).addClass('char-clicked');
        $('#flash-game-id').val($(this).attr('rel'))
        $('.step-1').hide();
        $('.step-2').show();
        return false;
    })
    
    /* Tabs */
    $('.tab1').click(function(){
        $('.tab1').removeClass('tab1unchosen').addClass('tab1chosen').blur();
        $('.tab2').removeClass('tab2chosen').addClass('tab2unchosen');
        $('.tab3').removeClass('tab3chosen').addClass('tab3unchosen');
        $('.results_tab2, .results_tab3, .all_results_tab2, .all_results_tab3').hide();
        $('.results_tab1, .all_results_tab1').show();
        return false;
    })
    $('.tab2').click(function(){
        $('.tab2').removeClass('tab2unchosen').addClass('tab2chosen').blur();
        $('.tab1').removeClass('tab1chosen').addClass('tab1unchosen');
        $('.tab3').removeClass('tab3chosen').addClass('tab3unchosen');
        $('.results_tab1, .results_tab3, .all_results_tab1, .all_results_tab3').hide();
        $('.results_tab2, .all_results_tab2').show();
        return false;
    })
    $('.tab3').click(function(){
        $('.tab3').removeClass('tab3unchosen').addClass('tab3chosen').blur();
        $('.tab1').removeClass('tab1chosen').addClass('tab1unchosen');
        $('.tab2').removeClass('tab2chosen').addClass('tab2unchosen');
        $('.results_tab1, .results_tab2, .all_results_tab1, .all_results_tab2').hide();
        $('.results_tab3, .all_results_tab3').show();
        return false;
    })
})

/* Oyna button */
function oynaButton() {
    $('.oyna-button').show().addClass('oyna-clicked').blur();
    $('.step-1, .step-2, .step-3, .step-4').hide();
    $('.flash').hide();
    $('.step-1').show();
}