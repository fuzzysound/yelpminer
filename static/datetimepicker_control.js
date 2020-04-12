/*
    Controls Datetimepicker objects.
*/
$(function () {
    $(" #review__date__gte ").datetimepicker({
        viewMode: 'years',
        format: 'YYYY-MM-DD'
    })
    $(" #review__date__lte ").datetimepicker({
        viewMode: 'years',
        format: 'YYYY-MM-DD',
        useCurrent: false
    })
    $(" #tip__date__gte ").datetimepicker({
        viewMode: 'years',
        format: 'YYYY-MM-DD'
    })
    $(" #tip__date__lte ").datetimepicker({
        viewMode: 'years',
        format: 'YYYY-MM-DD',
        useCurrent: false
    })

    $(" #review__date__gte ").on("dp.change", function (e) {
        $('#review__date__lte').data("DateTimePicker").minDate(e.date);
    });
    $("#review__date__lte").on("dp.change", function (e) {
        $('#review__date__gte').data("DateTimePicker").maxDate(e.date);
    });
    $(" #tip__date__gte ").on("dp.change", function (e) {
        $('#tip__date__lte').data("DateTimePicker").minDate(e.date);
    });
    $("#tip__date__lte").on("dp.change", function (e) {
        $('#tip__date__gte').data("DateTimePicker").maxDate(e.date);
    });

    $(" #review__date__gte ").data("DateTimePicker").disable()
    $(" #review__date__lte ").data("DateTimePicker").disable()
    $(" #tip__date__gte ").data("DateTimePicker").disable()
    $(" #tip__date__lte ").data("DateTimePicker").disable()
})