to_date=false;
django.jQuery(document).ready(function(){
    let to_date;
    if (django.jQuery('#id_is_working').is(':checked')) {
        django.jQuery("#id_to_date").hide();
        to_date = true;
    } else {
        django.jQuery("#id_to_date").show();
        to_date = false;
    }
    django.jQuery("#id_is_working").click(function(){
        to_date=!to_date;
        if (to_date) {
            django.jQuery("#id_to_date").hide();
        } else {
            django.jQuery("#id_to_date").show();
        }
    })
})