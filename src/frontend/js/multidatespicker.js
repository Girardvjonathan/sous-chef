$(function() {
    // LXYANG: rename this file as orderbatchcreate.js?
    // Place batch orders

    // Initialize delivery dates
    var orders = []
    var initial_dates = [];
    $.each(
        ($('#id_delivery_dates').val() || '').split('|'),
        function (idx, elem) {
            if (elem) initial_dates.push(elem);
        });

    // --
    // Init multidatepicker on input directly would be simpler,
    // but a glitch would appear, so I init multidatespicker on an empty div#delivery_dates
    // and link it to an HTML input#id_delivery_dates using altField option
    // @see: https://github.com/dubrox/Multiple-Dates-Picker-for-jQuery-UI/issues/162
    $('#delivery_dates').multiDatesPicker({
        addDates: initial_dates,
        dateFormat: "yy-mm-dd",
        separator: "|",
        minDate: 0,
        numberOfMonths: 2,
        altField: '#id_delivery_dates',
        onSelect: function (dateText, inst) {
            $('#form_create_batch #id_is_submit').val("0");
            $('#form_create_batch').submit();
        }
    });
    $('.ui.accordion.meals').show();

    // fill in defaults
    (function fillInDefaults() {
        $("#form_create_batch .accordion[id^='date-']").each(function (idx, elem) {
            try {
                var client_meals_default = $(elem).data('client-meals-default');  // auto JSON
            } catch (e) {
                return;
            }
            var date = $(elem).attr('id').slice(5);
            // fill in data
            $.each(client_meals_default, function (key, value) {
                var selector = "#id_"+key+"_"+date+"_quantity";
                if (!$(selector).val()) {
                    $(selector).val(value);
                    dismissFieldError($(selector));
                }
            });
            if (client_meals_default.hasOwnProperty('size')) {
                var selector = "#id_size_"+date;
                if (!$(selector).dropdown('get value')[0]) {
                    $(selector).dropdown('set selected', client_meals_default.size);
                    dismissFieldError($(selector));
                }
            };
        });
    })();

    function dismissFieldError(elem) {
        $(elem).closest('.error').removeClass('error');
    }

    $('#form_create_batch #id_client .ui.dropdown').dropdown('setting', 'onChange', function (value, text, $selectedItem) {
        // on client change, update the form to update the client default.
        $('#form_create_batch #id_is_submit').val("0");
        $('#form_create_batch').submit();
    });

    $("#form_create_batch").on('submit', function collectInactiveAccordionsDates() {
        var dates = [];
        $('#form_create_batch #order_create_batch_items .accordion').has('.content:not(.active)').each(function (idx, elem) {
            var id = $(elem).attr('id');
            var date = id.slice(5);
            dates.push(date);
        });
        $('#form_create_batch #id_accordions_active').val(dates.join('|'));
    });
});
