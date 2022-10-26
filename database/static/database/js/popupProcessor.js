/*
    Создаём новое окно при нажатии кнопки добавить
    В окне добавления вызываем функцию closePopup
    сохраняем данные, обновляем страницу
    ??????
    PROFIT
*/

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
            console.log(val)
            console.log(e.value)
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
        e.addEventListener('select', function () {
            sessionStorage.setItem(e.name, e.value);
            console.log("Saved: ", e.name, e.value)
        })
    })
}

document.addEventListener("DOMContentLoaded", function () {
    console.log(document.querySelectorAll('textarea, input, select'))
    keepStorage()

});
