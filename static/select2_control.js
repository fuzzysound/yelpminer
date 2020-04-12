/*
Controls Select2 objects.
*/
var selectData = JSON.parse(document.getElementById("select-data").textContent)

$(" #business__city ").select2({
    data: selectData["city"]
})

$(" #business__state ").select2({
    data: selectData["state"]
})

$(" #business__categories ").select2({
    data: selectData["categories"]
})
