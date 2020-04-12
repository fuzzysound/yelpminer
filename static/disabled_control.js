/*
    Controls 'disabled' attribute according to checkbox changes.
*/
var items = {
    business: {
        "name": "",
        "city": "",
        "state": "",
        "categories": "",
    },
    review: {
        "text": "",
        "date": "",
    },
    tip: {
        "text": "",
        "date": ""
    }
}

for (let [index, value] of Object.entries(items)) {
    for (let item in value) {
        document.getElementById(index + "__" + item + "-checkbox").onchange = function() {
            if (item == "date") {
                document.getElementById(index + "__" + item + "__gte").disabled = !this.checked
                document.getElementById(index + "__" + item + "__lte").disabled = !this.checked
                }
            else {
                document.getElementById(index + "__" + item).disabled = !this.checked
            }
        }
    }
}

var choiceAttributes = JSON.parse(document.getElementById("choice-attributes").textContent)
for (let [attr, value] of Object.entries(choiceAttributes)) {
    document.getElementById("business__attributes__" + attr + "-checkbox").onchange = function() {
        for (let subattr in value.choice) {
            document.getElementById("business__attributes__" + attr + "__" + subattr).disabled = !this.checked
        }
    }
}

document.getElementById("business__is_open-checkbox").onchange = function() {
    document.getElementById("business__is_open").disabled = !this.checked
}

document.getElementById("business__stars-checkbox").onchange = function() {
    $("#business__stars").jRange("toggleDisable")
}
document.getElementById("review__stars-checkbox").onchange = function() {
    $("#review__stars").jRange("toggleDisable")
}
