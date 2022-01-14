$(document).ready(function () {

    $("#hide-banner").click(function () {
        if ($.cookie("banner")) {
            var val = $.cookie("banner");
            val = val == 0 ? 1 : 0;
        } else {
            var val = 1;
        }

        $.cookie('banner', val, { expires: 365, path: '/' });
        $("#the-banner").slideToggle('slow');
        $("span#show-hide").html(val <= 0 ? 'Show' : 'Hide');

    });

    $("div.add_tabs a").click(function () {
        $("div.add_tabs a").removeClass('selected');
        $(this).addClass('selected');
        $("div.the_tabs div").hide();
        $("div#" + $(this).attr('id') + 's').show('slow');
    });

    $("#wox-searchi").blur(function () {
        if ($(this).val() == '') {
            $(this).val('Search here...');
        }
    });

    $("#wox-searchi").focus(function () {
        if ($(this).val() == 'Search here...') {
            $(this).val('');
        }
    });

    $("#wox-cancel-login").click(function () {
        $("#wox-login-login").slideUp("slow", function () {
            $("#wox-login-all").slideDown("slow");
        });
    });

    $("#wox-login-link").click(function () {
        $("#wox-login-all").slideUp("slow", function () {
            $("#wox-login-login").slideDown("slow");
        });
    });

    if ($("#wox-announcement").length > 0) {
        $("#wox-announcement").slideDown();
        setTimeout(function () {
            $("#wox-announcement").slideUp();
        }, 10000);
    }

    $("#wox-announcement img.close").click(function () {
        $("#wox-announcement").slideUp();
    });

});