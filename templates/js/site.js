
$(window).on('resize load', function() {
		    $('body').css({"padding-top": $(".navbar").height() + 20 + "px"});
		});

function saveProfile()
        {
       $('form[id="profileForm"]').validate()
        $.ajax({
            url: "/apiSaveProfile",
            type: "post",
            async: false,
            data: $('form[id="profileForm"]').serializeArray(),
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
        localStorage.pID=$(item).parents('tr').find('#pID').val()
        console.log($(item).parents('tr').find('#pID').val())
        
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

        function submitFlag()
        { 
 
           $.ajax({
            url: "/submitFlags",
            type: "post",
            async: false,
            data: {part_id: $('#partId').val()},
            dataType: "html",
            success: function (data) {
                window.location.assign('/view_survey')
            },
        });
       }

       function returnCorrectedSurvey(item)
        {
        console.log($(item).parents('tr').find('#pID').val())
        localStorage.pID=$(item).parents('tr').find('#pID').val()
        window.location.assign('/verify_survey')
        }

        function checkBoxToggle(item)
        {
          if($(item).attr('checked')=='checked')
            $(item).removeAttr('checked')
          else
            $(item).attr('checked','checked')
        }
        
        function submitVerifiedSection()
        { 
          var arr_checked=[]
          var arr_unchecked=[]
          $('input[type="checkbox"]').each(function(i,item){
          if($(item).attr('checked')=="checked")
            arr_checked.push(item.value)
          else
            arr_unchecked.push(item.value)
          })
            

           $.ajax({
            url: "/verifySection",
            type: "post",
            async: false,
            data: {checked: JSON.stringify(arr_checked), unchecked: JSON.stringify(arr_unchecked)},
            dataType: "html",
            success: function (data) {
                if($('#sectionsNav').find('li').length>1)
                {       $('li[value='+$('input[name="sectId"]').val()+']:eq(0)').remove()
                  $('#sectionsNav').find('li:eq(0)').trigger('click')
                }
                else
                  window.location.assign('/survey_approval')
            },
        });

        }

function submitPMuser(role,item)
{
  datum={first_name: $(item).parents('form').find('input[name="editorFName"]').val(),
         last_name: $(item).parents('form').find('input[name="editorLName"]').val(),
         email: $(item).parents('form').find('input[name="email"]').val(),
         DOB: $(item).parents('form').find('input[name="DOB"]').val(),
        role:role,
        pm_id:localStorage.user
        }
          $.ajax({
             url: "/addUser",
             type: "get",
             async: false,
             data: datum,
             success: function () {
                
             },
        });

}

function removeDEMap(item)
{

          $.ajax({
             url: "/del_map",
             type: "get",
             async: false,
             data: {de_id:$(item).parent().parent().find('input[type="hidden"]:eq(1)').val(), su_id:$(item).parent().parent().find('input[type="hidden"]:eq(0)').val()},
             success: function () {
                window.location.assign('/de_map')
             },
        });

  }

  function addDEMap(item)
{         
          var datum= {su_id:$(item).parent().parent().find('input[type="hidden"]').val(),
                      de_id:$('#list').find('li[class="ng-scope active"]').find('input').val(),
                     pm_id:localStorage.user}
          console.log(datum)
          $.ajax({
             url: "/add_map",
             type: "get",
             async: false,
             data: datum,
             success: function () {
                window.location.assign('/de_map')
             },
        });

  }

  function submitPMForm(item)
{
  datum={first_name: $(item).parents('form').find('input[name="managerFirstName"]').val(),
         last_name: $(item).parents('form').find('input[name="managerLastName"]').val(),
         email: $(item).parents('form').find('input[name="email"]').val(),
         DOB: $(item).parents('form').find('input[name="DOB"]').val(),
         role: 'PM',
        project:$(item).parents('form').find('select').val()}
          $.ajax({
             url: "/addPM",
             type: "post",
             async: false,
             data: datum,
             success: function () {
                 window.location.assign('/manage_pm')
             },
        });

}

function createProject(item)
{
  datum={project_name: $(item).parents('form').find('input').val()}
          $.ajax({
             url: "/addProject",
             type: "post",
             async: false,
             data: datum,
             success: function () {
                 window.location.assign('/manage_pm')                
             },
        });

}


function deletePM(item)
        {
            // console.log($(item).parents('tr').find('input[type="hidden"]:eq(0)').val())
            $.ajax({
            url: "/deletePM",
            type: "post",
            async: false,
            data: {pm_id: $(item).parents('tr').find('input[type="hidden"]:eq(0)').val()},
            dataType: "html",
            success: function (data) {
               $(item).attr('disabled','disabled')
               },
        });
         }
