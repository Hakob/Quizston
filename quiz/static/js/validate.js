$(document).ready(function () {
    $("#register_form").submit(function (e) {
        e.preventDefault();
        $("#name-warning").hide();
        $("#email-warning").hide();
        $("#password-warning").hide();

        if (document.forms["register_form"]["name"].value === '') {
            $("#name-warning").show();
            setTimeout(function () {
                $("#name-warning").hide();
            }, 2000);
            return;
        } else {
            $.get("/quiz/validate_username/", {
                    name: document.forms["register_form"]["name"].value
                },
                function (data) {
                    if (data.is_taken === true) {
                        alert("This Username is already taken. Please try another.");
                        return false;
                    } else {
                        alert("Username is free");
                        $.post("/quiz/create/", {
                                name: document.forms["register_form"]["name"].value,
                                email: document.forms["register_form"]["email"].value,
                                password: document.forms["register_form"]["password"].value,
                                csrfmiddlewaretoken: document.forms["register_form"]["csrfmiddlewaretoken"].value
                            },
                            function (data, status) {
                                if (status === "success") {
                                    $("#modal1").modal('hide');
                                    $("#register-success").show();
                                }
                            }
                        );
                    }
                }
            );
        }
        if (document.forms["register_form"]["email"].value === '') {
            $("#email-warning").show();
            setTimeout(function () {
                $("#email-warning").hide();
            }, 2000);
            return;
        }
        if (document.forms["register_form"]["password"].value === '') {
            $("#password-warning").show();
            setTimeout(function () {
                $("#password-warning").hide();
            }, 2000);
            return false;
        }

    });
    $("#login_form").submit(function (e) {
        e.preventDefault();
        $.post("/quiz/validate_login/", {
                username: document.forms["login_form"]["username"].value,
                password: document.forms["login_form"]["password"].value,
                csrfmiddlewaretoken: document.forms["login_form"]["csrfmiddlewaretoken"].value
            },
            function (data, status) {
                window.location.href = "/quiz/test";
            }
        );
    });

});