// app.js
//
// Handle form submission
$(document).ready(function() {
    $('input.btn').click(function(event) {
        // Stop the event from propagating to other instances of that class
        event.stopPropagation();
        // Stop the event from propagating to children
        event.stopImmediatePropagation();
        // Prevent link from routing
        event.preventDefault();
        var form = $(this).data('formname');
        console.log(form);
        if ($.isArray(form)) {
            $.each(form, function(index, value) {
                console.log(`[*] Button selected: ${value}`);
            });
        } else {
            console.log('Not an array');
        }
        // console.log(`[*] Button selected: ${$(this).attr('data-formname')}`);
    });
});
