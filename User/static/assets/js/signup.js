$("#signup").click(function() {
    $("#first").fadeOut("fast", function() {
    $("#second").fadeIn("fast");
    });
    });

    $("#signin").click(function() {
    $("#second").fadeOut("fast", function() {
    $("#first").fadeIn("fast");
    });
    });







    $(function() {

      $("form[name='registration']").validate({
        rules: {
          username: {
          required: true
          },

          email: {
            required: true,
            email: true
          },
          password: {
            required: true,
            minlength: 5
          },
          confirmpassword: {
          required: true,
          minlength: 5
          }
        },
        
        messages: {
        username: "Please enter a username",

          password: {
            required: "Please provide a password",
            minlength: "Your password must be at least 5 characters long"
          },
          confirmpassword: {
            required: "Please provide a password",
            minlength: "Your password must be at least 5 characters long"
          },
          email: "Please enter a valid email address"
        },
      
        submitHandler: function(form) {
          form.submit();
        }
      });
    });
    