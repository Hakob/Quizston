$(document).ready(function(){
   $("#register_form").submit(function(e){
       e.preventDefault();
       $("#name-warning").hide();
       $("#email-warning").hide();
       $("#password-warning").hide();
       if(document.forms["register_form"]["name"].value == '')
       {
           $("#name-warning").show();
           return;
       }
       if(document.forms["register_form"]["email"].value=='')
       {
           $("#email-warning").show();
           return;
       }
       if(document.forms["register_form"]["password"].value=='')
       {
           $("#password-warning").show();
           return;
       }
       $.post("/quiz/create/",
           {
               name : document.forms["register_form"]["name"].value,
               email : document.forms["register_form"]["email"].value,
               password : document.forms["register_form"]["password"].value,
               csrfmiddlewaretoken :document.forms["register_form"]["csrfmiddlewaretoken"].value
           },
           function(data,status)
           {
               if (status == "success")
               {
                   $("#modal1").modal('hide');
                   $("#register-success").show();
               }
           }
       );
   }) ;
   $("#login_form").submit(function(e){
      // alert("hello");
       e.preventDefault();
       $.post("/quiz/validate_login/",
           {
               username : document.forms["login_form"]["username"].value,
               password : document.forms["login_form"]["password"].value,
               csrfmiddlewaretoken : document.forms["login_form"]["csrfmiddlewaretoken"].value
           },
           function(data,status)
           {
                   window.location.href="/quiz/test";
           }
       );
   });

    // $("#exam-form").submit(function(e){
    //        e.preventDefault();
    //        $.post("/quiz/add_exam/",
    //            {
    //                exam_name : document.forms["exam-form"]["exam_name"].value,
    //                user : document.forms["exam-form"]["user"].value,
    //                csrfmiddlewaretoken :document.forms["exam-form"]["csrfmiddlewaretoken"].value
    //            },
    //            function(data,status)
    //            {
    //                 $("#exam_list").append(template(document.forms["exam-form"]["user"].value,document.forms["exam-form"]["exam_name"].value));
    //                $(".add_exam").click();
    //                document.forms["exam-form"]["exam_name"].value = "";
    //            }
    //        );
    // });

});
