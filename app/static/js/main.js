$(function () {
    $('#btn-create-article').click(function () {
        $.ajax({
            url: "/create_article",
            data: $('form').serialize(),
            type: 'POST',
            dataType: 'json',
            success: function (response) {
                window.location.pathname = response.slug;
                document.cookie = "owner_id=" + response.owner_id;
            }
        });
    });

    $('#btn-update-article').click(function () {
        $.ajax({
            url: window.location.pathname,
            data: $('form').serialize(),
            type: 'POST',
            dataType: 'json',
            success: function (response) {
                window.location.pathname = response.slug;
            }
        });
    });
});