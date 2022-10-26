function showAddPopup(triggeringLink) {
    var name = triggeringLink.id.replace(/^create_/, '');
    href = triggeringLink.href;
    var win = window.open(href, name, 'height=500,width=800,resizable=yes,scrollbars=yes');
    win.focus();
    return false;
}

function closePopup(win, newID, newRepr, id) {
    //$(id).append('<option value=' + newID + ' selected >' + newRepr + '</option>')
    window.location.reload();
    win.close();
}

function closeDeletePopup(win) {
    window.location.reload();
    win.close();
}

function clearStorage() {
    sessionStorage.clear();
}

function keepStorage() {
    document.querySelectorAll('textarea, input, select').forEach(function (e) {
        if (e.name != "csrfmiddlewaretoken" && e.value != '') {//e.value === '') { 
            val = sessionStorage.getItem(e.name, e.value)
            console.log("Restored: ", e.name, val)
            if (val != null) e.value = val;
        }
        e.addEventListener('input', function () {
            sessionStorage.setItem(e.name, e.value);
            console.log("Saved: ", e.name, e.value)
        })
        e.addEventListener('textarea', function () {
            sessionStorage.setItem(e.name, e.value);
            console.log("Saved: ", e.name, e.value)
        })
    })
}

document.addEventListener("DOMContentLoaded", function () {
    keepStorage()

});

$(document).ready(function () {
    $('.form-select').select2({
        language: "ru",
        width: "100%",
        theme: "bootstrap-5"
      });

    document.querySelectorAll('select').forEach(function (e) {
        e.onchange = function () {
            sessionStorage.setItem(e.name, e.value);
            console.log("Saved: ", e.name, e.value)
        }
    })

    $('#id_shipping_date').datetimepicker({
        format: 'd.m.Y',
        timepicker: false,
    });
    $('#id_manufactured_date').datetimepicker({
        format: 'd.m.Y',
        timepicker: false,
    });
});