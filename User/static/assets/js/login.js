
    $(function() {
       $("form[name='login']").validate({
         rules: {
           email:{
           required:true
           },
           password: {
             required: true,

           }
         },
          messages: {
           email:{
           required:"Please enter a valid username"},

           password: {
             required: "Please enter password",

           }

         },
         submitHandler: function(form) {
           form.submit();
         }
       });
    });