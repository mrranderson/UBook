function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = $.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

$.ajaxSetup({
    beforeSend: function (xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});

function charge(amount) {
    $.post("/charge/", {'price': amount}, function (data) {
        if (data.response == true) {
            setTimeout(function () {
                $.bootstrapGrowl("Awesome! Your textbook is on its way.", {type: 'success'});
            }, 3000);
        } else {
            setTimeout(function () {
                $.bootstrapGrowl("Uh oh, something went wrong. Try again later!", {type: 'danger'});
            }, 3000);
        }
    });
}