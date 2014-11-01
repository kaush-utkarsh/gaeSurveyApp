
$(window).on('resize load', function() {
		    $('body').css({"padding-top": $(".navbar").height() + 20 + "px"});
		});

function saveProfile(item)
        {
       
        $.ajax({
            url: "/apiSaveProfile",
            type: "post",
            async: false,
            data: $('form').serializeArray(),
            dataType: "html",
            success: function (data) {
                // console.log(data)
                window.location.assign("/")
            },
        });
        }


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
                localStorage.user = data;
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

function deleteUserRow(item)
        {
            // console.log($(item).parents('tr').find('input[type="hidden"]').val())
            $.ajax({
            url: "/deleteUser",
            type: "post",
            async: false,
            data: {user_id: $(item).parents('tr').find('input[type="hidden"]').val()},
            dataType: "html",
            success: function (data) {
               $(item).attr('disabled','disabled')
               $(item).parent().find('button:eq(1)').show()
            },
        });
         }

        function undoDelete(item)
        {
            $.ajax({
            url: "/undoUserDelete",
            type: "post",
            async: false,
            data: {user_id: $(item).parents('tr').find('input[type="hidden"]').val()},
            dataType: "html",
            success: function (data) {
               
               $(item).parent().find('button:eq(0)').removeAttr('disabled')
               $(item).attr('style','display:none')
            },
        });
        }

        function returnSurveyData(item)
        {
        console.log($(item).parents('tr').find('#pID').val())
        localStorage.pID=$(item).parents('tr').find('#pID').val()
        window.location.assign('/flag_survey')
        }

        function checkBoxToggle(item)
        {
          if($(item).attr('checked')=='checked')
            $(item).removeAttr('checked')
          else
            $(item).attr('checked','checked')
        }

        function flagSection()
        { 
          var arr_checked=[]
          var arr_unchecked=[]
          $('input[type="checkbox"]').each(function(i,item){
          if($(item).attr('checked')=="checked")
            arr_checked.push(item.value)
          else
            arr_unchecked.push(item.value)
          })
          console.log(arr_checked)
          // console.log(arr_unchecked)

           $.ajax({
            url: "/checkSection",
            type: "post",
            async: false,
            data: {checked: JSON.stringify(arr_checked), unchecked: JSON.stringify(arr_unchecked)},
            dataType: "html",
            success: function (data) {

            },
        });

        }