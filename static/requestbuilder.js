/*
Builds HTTP request with input values.
*/
var operatorMap = JSON.parse(document.getElementById("operator-map").textContent)

function addToParams(params, index, prefix, field, v) {
    if (typeof(v) == "string") {
        var key = index + prefix + field
        var operator = v
        if (operator == "contains") {
            var val = document.getElementById(key).value
        }
        else if (operator == "in") {
            if (field == "categories") {
                var select = $("#" + key)
                var selected = []
                for (item of select.select2('data')) {
                    selected.push(item.text)
                }
                if (selected.length == 0) {
                    return
                }
                var val = selected.join(',')
            }
            else {
                var checkboxes = $("." + key + "-checkbox")
                var checked = []
                for (box of checkboxes) {
                    if (box.checked) {
                        checked.push(box.value)
                    }
                }
                if (checked.length == 0) {
                    return
                }
                var val = checked.join(',')
            }
        }
        else if (operator == "eq") {
            if (field == "is_open") {
                var val = (document.getElementById(key).value == "Yes") ? "1" : "0"
            }
            else if (key.includes("attributes")) {
                if (document.getElementById(key).checked) {
                    var val = "true"
                }
                else {
                    return
                }
            }
            else {
                var val = $("#" + key).select2('data')[0].text
            }
        }
        else if (operator == "range") {
            if (field == "stars") {
                var val = document.getElementById(key).value
            }
            else if (field == "date") {
                var gte = document.getElementById(key + "__gte").value + " 00:00:00"
                var lte = document.getElementById(key + "__lte").value + " 00:00:00"
                var val = gte + ',' + lte
            }
        }
        else if (operator == "either") {
            if (!document.getElementById(key.split("__").slice(0,-1).join("__") + "-checkbox").checked) {
                return
            }
            if (document.getElementById(key).checked) {
                var val = "true"
            }
            else {
                return
            }
        }
        if (key.includes("attributes") | ["review", "tip"].includes(index)) {
            if (key.includes("attributes")) {
                var top_checkbox = document.getElementById("business__attributes-checkbox")
            }
            else if (index == "review") {
                var top_checkbox = document.getElementById("review-checkbox")
            }
            else {
                var top_checkbox = document.getElementById("tip-checkbox")
            }
            if (!top_checkbox.checked) {
                return
            }
        }
        var checkbox = document.getElementById(key + "-checkbox")
        if (!checkbox) {
            params[key + "__" + operator] = val
        }
        else if (checkbox.checked){
            params[key + "__" + operator] = val
        }
    }
    else {
        for (let [k2, v2] of Object.entries(v)) {
            addToParams(params, index, prefix + field + "__", k2, v2)
        }
    }
}
function buildRequest() {
    params = {}
    for (let [index, field] of Object.entries(operatorMap)) {
        for (let [k, v] of Object.entries(field)) {
            addToParams(params, index, "__", k, v)
        }
    }
    params["limit"] = document.getElementById("limit").value
    params["offset"] = "0"
    params["business-sort-by"] = (document.getElementById("business-sort-by").value == "Stars") ? "stars" : "review_count"
    params["review-join"] = (document.getElementById("review-checkbox").checked) ? "true" : "false"
    params["tip-join"] = (document.getElementById("tip-checkbox").checked) ? "true" : "false"
    params["num-reviews"] = document.getElementById("num-reviews").value
    params["review-sort-by"] = document.getElementById("review-sort-by").value.toLowerCase()
    params["num-tips"] = document.getElementById("num-tips").value
    params["tip-sort-by"] = (document.getElementById("tip-sort-by").value == "Date") ? "date" : "compliment_count"
    paramsStrings = []
    for (let [k, v] of Object.entries(params)) {
        paramsStrings.push(k + '=' + v)
    }
    return window.location.href + "rest?" + paramsStrings.join('&')
}

function showURL() {
    url = buildRequest()
    document.getElementById("request").value = url
}

function goToURL() {
    url = buildRequest()
    window.open(url)
}

document.getElementById("build-request").onclick = showURL
document.getElementById("view-on-browser").onclick = goToURL