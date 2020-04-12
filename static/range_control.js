/*
    Controls jRange objects.
*/
$(" #business__stars").jRange({
    id: "business__stars__range",
    from: 0.0,
    to: 5.0,
    step: 0.1,
    scale: [0.0, 1.0, 2.0, 3.0, 4.0, 5.0],
    format: '%s',
    width: 300,
    showLabels: true,
    snap: true,
    disable: true
})

$(" #review__stars").jRange({
    id: "review__stars__range",
    from: 0.0,
    to: 5.0,
    step: 0.1,
    scale: [0.0, 1.0, 2.0, 3.0, 4.0, 5.0],
    format: '%s',
    width: 300,
    showLabels: true,
    snap: true,
    disable: true
})
