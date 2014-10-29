
$(window).on('resize load', function() {
		    $('body').css({"padding-top": $(".navbar").height() + 20 + "px"});
		});

 function SignIn(item)
        {

        un=$(item).parent().parent().find('input[type="text"]').val()
        pd=$(item).parent().parent().find('input[type="password"]').val()
        $.ajax({
            url: "/login",
            type: "post",
            async: false,
            data: {username:un,password:pd},
            dataType: "html",
            success: function (data) {
                console.log(data)
                // nv=JSON.parse(data)
                localStorage.dataObject = data;
                // console.log(nv)
                window.location.assign("/")
            },
        });
    }

   function LogOut()
   		{
   			$.ajax({
            url: "/logout",
            type: "post",
            async: false,
            dataType: "html",
            success: function (data) {
                
                localStorage.clear();
                // console.log(nv)
                window.location.assign("/login")
            },
        });
   		}

