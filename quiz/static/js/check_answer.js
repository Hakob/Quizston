$("#exam-form").submit(function (event) {
    event.preventDefault();
    var answer = $('input[type=radio]:checked');
    var _answer = answer.val();
    var csrf = $("input[name=csrfmiddlewaretoken]").val();
    $.ajax({
        url: "{% url 'index' %}",
        type: "PUT",
        headers: {
            'X-CSRFToken': csrf
        },
        data: JSON.stringify({
            'answer': _answer
        }),
        dataType: 'json',
        success: function (data) {

            if (data['is_true']) {
                $('#' + _answer).css("background-color", "green");
            }
            else {
                $('#' + _answer).css("background-color", "red");
                $('#' + data['true_answer']).css("background-color", "green");
            }
        }
    });
});