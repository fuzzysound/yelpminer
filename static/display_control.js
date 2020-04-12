/*
    Controls display of sub-containers according to checkbox changes.
*/
const arr = ["business__attributes", "review", "tip"]
arr.forEach(function(item) {
    document.getElementById(item + "-checkbox").onchange = function() {
        elm = $("#" + item)
        if (elm.css("display") == "none") {
            elm.slideDown()
        }
        else {
            elm.slideUp()
        }
    }
})