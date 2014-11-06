'use strict';
var surveyApp = angular.module('surveyApp',['ngRoute', 'ngTable','ui.bootstrap']);

surveyApp.factory('surveyFactory',['$http', function($http) {
	 
	 var user = localStorage.user;

	 var datum;
        $.ajax({
            url: "/apiUserProfile",
            type: "post",
            async: false,
            data: {user_id:user},
            dataType: "html",
            success: function (data) {
                datum=JSON.parse(data)
                },
        });

     return datum;
}]);

surveyApp.config(function($routeProvider,$locationProvider) {
	$routeProvider
		.when('/', {	
			templateUrl : 'pages/profile.html',
			controller  : 'profileController'
		})

		.when('/profile', {	
			templateUrl : 'pages/profile.html',
			controller  : 'profileController'
		})

		.when('/surveys', {
			templateUrl : 'pages/surveys.html',
			controller  : 'surveyController'
		})

		.when('/manage_researcher', {
			templateUrl : 'pages/researchers.html',
			controller  : 'researchersController'
		})

		.when('/view_survey', {
			templateUrl : 'pages/surveys.html',
			controller  : 'surveysController'
		})

        .when('/survey_approval', {
            templateUrl : 'pages/approval_surveys.html',
            controller  : 'approvalController'
        })


        .when('/flag_survey', {
            templateUrl : 'pages/survey.html',
            controller  : 'surveyFlagController'
        })

        .when('/verify_survey', {
            templateUrl : 'pages/approval_survey.html',
            controller  : 'surveyVerifyController'
        })

        .when('/view_survey_data', {
             templateUrl : 'pages/view_survey_data.html',
             controller  : 'surveyDataController'
        })

        .when('/de_map', {    
             templateUrl : 'pages/de_mapping.html',
             controller  : 'mappingController'
         })

		.when('/data', {
			templateUrl : 'pages/data.html',
			controller  : 'dataController'
		})

		.when('/settings', {	
			templateUrl : 'pages/settings.html',
			controller  : 'settingsController'
		})

		.when('/sms', {	
			templateUrl : 'pages/sms.html',
			controller  : 'smsController'
		})

		.when('/manage_pm', {	
			templateUrl : 'pages/manager.html',
			controller  : 'managerController'
		})

		.when('/entrepreneur', {	
			templateUrl : 'pages/entrepreneur.html',
			controller  : 'entreController'
		})
	$locationProvider.html5Mode(true);
});


surveyApp.controller('surveyDataController', function($scope, $filter, $window,surveyFactory, $http, ngTableParams) {
    $.ajax({
         url: "/survey-misc",
         type: "get",
         async: false,
         dataType: "html",
         success: function (data) {
            $scope.misc = JSON.parse(data);
         },
    });

    console.log($scope.misc);
    var participantData;
    var questions;
    $scope.nodata = null;
    $scope.questions = [];
    $scope.participants = [];

    $.ajax({
             url: "/survey_data",
             type: "get",
             async: false,
             data: {project_id:'P0001', survey_id:'GRO01',starting_value:'0',ending_value:'1000'},
             dataType: "html",
             success: function (data) {
                 console.log(data);
                 participantData = JSON.parse(data);
                 questions = participantData.questions.slice(1,a.length-1);
                 $scope.questions =  angular.copy(questions); // Getting rid of the extra first column
                 $scope.participants = angular.copy(participantData.participants);
             },
        });
    /*$scope.columns = [{title : 'Participant ID', field : 'participant_ID', visible : true},
              {title : 'Language ID', field : 'lang_id', visible : true}];*/
        $scope.selectedValue = null;
    //$scope.misc = [];
        
      // if($scope.questions.length<1||$scope.questions.length===undefined)
      //     toastr.warning("No data to display in the table")
        $scope.unselected = [];

        $scope.trackQuestions = function(question,index) {
            $scope.addQuestion = question;
            if ($scope.unselected.indexOf(question) == -1) {
                $scope.unselected.push(question);
            }
            else {
                $scope.unselected.splice(index,1);
            }
        }

        $scope.surveyFilterID = null;
        $scope.projectFilterID = null;

        $scope.updateProjectID = function(item) {
            $scope.projectFilterID = item;
        }

        $scope.updateSurveyID = function(item) {
            $scope.surveyFilterID = item;
            $scope.disabled = '';
        }
        $scope.disabled = 'disabled';
        $scope.getDataByFilter = function (){
          console.log($scope.selectedProject);
          console.log($scope.selectedSurvey);
            $http({
                    method: 'GET',
                    url: '/survey_data',
                    params : {project_id : $scope.selectedProject,survey_id : $scope.selectedSurvey, starting_value : 0, ending_value : 100000}
            }).success(function (result) {
                    $scope.questions = angular.copy(result.questions.slice(1,a.length-1));
                    $scope.participants = angular.copy(result.participants);
            });
        }

        $scope.generateCsv = function(unselected) {
            //generate csv code send request
            var project_id = $scope.projectFilterID;
            var survey_id = $scope.surveyFilterID;
            var questions  =  $scope.unselected;

            console.log("chines adlandk")
            console.log(project_id)
            console.log(survey_id)
            console.log(questions)
        //     $.ajax({
        //      url: "/export_csv",
        //      type: "get",
        //      async: false,
        //      data: {"survey_id":survey_id,"project_id":project_id,"questions":questions},
        //      dataType: "html",
        //      success: function (data) {
        //          console.log(data);
        //      },
        // });
     $window.location.href= "/export_csv?survey_id=" + survey_id + "&project_id="+project_id+"&questions="+questions;
        }
});

surveyApp.controller('mappingController', function($scope,surveyFactory) {

  $.ajax({
             url: "/de_mapping",
             type: "get",
             async: false,
             data: {pm_id:localStorage.user},
             dataType: "html",
             success: function (data) {
                console.log(data);
                 // console.log(JSON.parse(data).editor_surveyors[0].ID);
                 $scope.editors=JSON.parse(data).editor_surveyors
                 $scope.surveyers=JSON.parse(data).editor_surveyors[0].surveyers
                 $scope.currentDe=JSON.parse(data).editor_surveyors[0].ID
                 $scope.usurveyers=JSON.parse(data).surveyers
                  $scope.activeSection=0
                  console.log($scope.editors);
                 // $scope.editor.surveyers=JSON.parse(data).surveyors
             },
        });

        $scope.maxDate  = new Date();
        $scope.today = function() {
        $scope.dt = new Date();
      };
      $scope.today();

    $scope.formats = ['dd-MMMM-yyyy', 'yyyy/MM/dd', 'dd.MM.yyyy', 'shortDate'];
    $scope.format = $scope.formats[2];
      $scope.open = function($event) {
        $event.preventDefault();
        $event.stopPropagation();
        $scope.opened = true;
     };




        $scope.updateLi = function(index) {

            $scope.activeSection = index;
            $scope.surveyers=$scope.editors[index].surveyers
            console.log($scope.surveyers);
            $scope.currentDe=$scope.editors[index].ID
            
        } 
        $scope.datum=null
      $scope.submitPMSurveyor=function(role,item)
        {
          $scope.datum=null
      
          // alert(angular.element('input[name="suFName"]').val())
          $scope.datum={first_name: angular.element('input[name="suFName"]').val(),
                 last_name: angular.element('input[name="suLName"]').val(),
                 email: angular.element('input[name="semail"]').val(),
                 DOB: angular.element('input[name="sDOB"]').val(),
                role:role,
                pm_id:localStorage.user
                }
                // console.log(datum)
          $.ajax({
             url: "/addUser",
             type: "get",
             async: false,
             data: $scope.datum,
             success: function () {
              // alert('New User Added')
                angular.element('.modal').find('button[class="btn btn-danger"]').trigger('click')
                window.location.assign('/de_map')
             },
        });
        }
           $scope.submitPMEditor=function(role,item)
            {
           $scope.datum=null
      
          // alert(angular.element('input[name="suFName"]').val())
          $scope.datum={first_name: angular.element('input[name="edFName"]').val(),
                 last_name: angular.element('input[name="edLName"]').val(),
                 email: angular.element('input[name="edemail"]').val(),
                 DOB: angular.element('input[name="edDOB"]').val(),
                role:role,
                pm_id:localStorage.user
                }
                // console.log(datum)
          $.ajax({
             url: "/addUser",
             type: "get",
             async: false,
             data: $scope.datum,
             success: function () {
              // alert('New User Added')
                angular.element('.modal').find('button[class="btn btn-danger"]').trigger('click')
                window.location.assign('/de_map')

             },
        });

        }



});


surveyApp.controller('appController', function($scope,surveyFactory) {
	$scope.user = surveyFactory.user;
	$scope.navs = surveyFactory.navs;
});

surveyApp.controller('profileController', function($scope,$window,surveyFactory) {
	$scope.user = surveyFactory.user;
	$scope.navs = surveyFactory.navs;
    $scope.reset = function(){
        $window.location.assign("/")
    }
    $scope.saveProfile = function(){
        console.log("Saving profile")
        $.ajax({
            url: "/apiSaveProfile",
            type: "post",
            async: false,
            data: $('form[id="profileForm"]').serializeArray(),
            dataType: "html",
            success: function (data) {
                // console.log(data)
                toastr.success("Profile Successfully Updated")
                // $window.location.assign("/")
            },
            error: function(data){
              toastr.error("Profile Could not be updated")
            }
        });
    };

    $scope.formats = ['dd-MMMM-yyyy', 'yyyy/MM/dd', 'dd.MM.yyyy', 'shortDate'];
    $scope.format = $scope.formats[2];

$scope.maxDate  = new Date();
$scope.today = function() {
        $scope.dt = new Date();
      };
      $scope.today();

      $scope.open = function($event) {
        $event.preventDefault();
        $event.stopPropagation();

        $scope.opened = true;
    };


});

// surveyApp.controller('surveysController', function($scope,surveyFactory) {
// 	$scope.surveys = surveyFactory.surveys;
// });


surveyApp.controller('surveyFlagController', function($scope,surveyFactory) {
	
	var pid=localStorage.pID


	        $.ajax({
            url: "/returnSurvey",
            type: "post",
            async: false,
            data: {part_id:pid},
            dataType: "html",
            success: function (data) {
              $scope.PID=JSON.parse(data).part_id 
              $scope.sections=JSON.parse(data).sections  
              $scope.questions=JSON.parse(data).sect.ques
              $scope.sect_ID=JSON.parse(data).sect.sect_id
              $scope.sect_Name=JSON.parse(data).sect.sect_name
              console.log(JSON.parse(data).sect.sect_name);
            $scope.activeSection=0
            }
       		 }); 



        $scope.getQuestions = function(index, sec_ID, sec_Name) {
            $scope.activeSection = index;
            
            $.ajax({
            url: "/returnSection",
            type: "post",
            async: false,
            data: {part_id:$scope.PID,sect_id:sec_ID,sect_name:sec_Name},
            dataType: "html",
            success: function (data) {
            	$scope.questions=JSON.parse(data).ques
            	$scope.sect_ID=JSON.parse(data).sect_id
            	$scope.sect_Name=JSON.parse(data).sect_name
           }
        }); 
	};


});

surveyApp.controller('surveyVerifyController', function($scope,surveyFactory) {
    
    var pid=localStorage.pID


            $.ajax({
            url: "/apiViewFlaggedSection",
            type: "post",
            async: false,
            data: {part_id:pid},
            dataType: "html",
            success: function (data) {
              $scope.PID=JSON.parse(data).part_id 
              $scope.sections=JSON.parse(data).sections  
              $scope.questions=JSON.parse(data).sect.ques
              $scope.sect_ID=JSON.parse(data).sect.sect_id
              $scope.sect_Name=JSON.parse(data).sect.sect_name
             $scope.activeSection=0
            }
             }); 



        $scope.getQuestions = function(index, sec_ID, sec_Name) {
            $scope.activeSection = index;
            
            $.ajax({
            url: "/apiViewFlaggedQuestion",
            type: "post",
            async: false,
            data: {part_id:$scope.PID,sect_id:sec_ID,sect_name:sec_Name},
            dataType: "html",
            success: function (data) {
                $scope.questions=JSON.parse(data).ques
                $scope.sect_ID=JSON.parse(data).sect_id
                $scope.sect_Name=JSON.parse(data).sect_name
           }
        }); 
    };

});

surveyApp.controller('researchersController', function($scope,surveyFactory) {
	$.ajax({
            url: "/apiResearcher",
            type: "post",
            async: false,
            dataType: "html",
            success: function (data) {
                localStorage.Researchers = data;
            },
        });

    $scope.maxDate  = new Date();
    $scope.today = function() {
            $scope.dt = new Date();
          };
          $scope.today();

	var rs=JSON.parse(localStorage.Researchers)
	$scope.researchers = rs.researchers
});

surveyApp.controller('settingsController', function($scope,surveyFactory) {
	$scope.User = surveyFactory.user;
});

surveyApp.filter('unique', function() { return function (arr, field) { var o = {}, i, l = arr.length, r = []; for(i=0; i<l;i+=1) { o[arr[i][field]] = arr[i]; } for(i in o) { r.push(o[i]); } return r; }; })


surveyApp.controller('surveysController', function($scope,surveyFactory) {

   var user=localStorage.user
     var datjson;
   var datum;
        $.ajax({
            url: "/apiViewSurveys",
            type: "post",
            async: false,
            data: {user_id:user},
            dataType: "html",
            success: function (data) {
               datjson=JSON.parse(data)

              },
        });
        if(datjson.length < 1) {
                        $scope.errorMsg='No Data to be Displayed'
                    }

        var surveyList=[]
        $.each(datjson,function(i,item){
            if ($.inArray(item, surveyList) === -1) {
        surveyList.push(item)
            }
        })
        console.log(surveyList)
            $scope.surveysList=angular.copy(surveyList)
        $scope.surveys=datjson
 });


surveyApp.controller('approvalController', function($scope,surveyFactory) {

    var user=localStorage.user
    var datum;
       $.ajax({
           url: "/apiVerifySurveys",
           type: "post",
           async: false,
           data: {user_id:user},
           dataType: "html",
               success: function (data) {
                    $scope.approval_surveys=JSON.parse(data)

                },
            });


       
        if($scope.approval_surveys.length < 1) {
                        toastr.error("No Data to be Displayed");
                        $scope.errorMsg='No Data to be Displayed'
                    }
                    
    $scope.requestType='approval'
 });



surveyApp.controller('mainController', function($scope,surveyFactory) {
});

surveyApp.controller('entreController', function($scope,surveyFactory) {
	$scope.user = surveyFactory.user;
});

surveyApp.controller('smsController', function($scope,surveyFactory) {
	$('.btn-group').button();
});

surveyApp.controller('managerController', function($scope,surveyFactory) {
    $.ajax({
           url: "/apiManagePM",
           type: "post",
           async: false,
           dataType: "html",
               success: function (data) {
                    $scope.managers=JSON.parse(data).managers
                    $scope.projects=JSON.parse(data).projects
                   
                },
            });


$scope.maxDate  = new Date();
$scope.today = function() {
        $scope.dt = new Date();
      };
      $scope.today();

 $scope.submitPMForm=function(item)
{

  $scope.datum=null
      
          // alert(angular.element('input[name="suFName"]').val())
          $scope.datum={first_name: angular.element('input[name="managerFirstName"]').val(),
         last_name: angular.element('input[name="managerLastName"]').val(),
         email: angular.element('input[name="email"]').val(),
         DOB: angular.element('input[name="DOB"]').val(),
         role: 'PM',
        project:angular.element('form[id="pmProjectForm"]').find('select').val()}
          $.ajax({
             url: "/addPM",
             type: "post",
             async: false,
             data:  $scope.datum,
             success: function () {
                 window.location.assign('/manage_pm')
             },
        });

}


$scope.createProject=function()
{
          $.ajax({
             url: "/addProject",
             type: "post",
             async: false,
             data: {project_name: angular.element('input[name="projectName"]').val()},
             success: function () {
                 window.location.assign('/manage_pm')                
             },
        });

}




	// $scope.managers = surveyFactory.managers;
	// $scope.projects = surveyFactory.projects;
});

/*surveyApp.controller('dataController', function($scope, $filter, ngTableParams, surveyFactory) {
	 	var data = surveyFactory.data2;
            $scope.columns = [
                { title: 'ID', field: 'ID', visible: true },
                { title: 'Schedule Name', field: 'ScheduleName', visible: true },
                { title: 'Date', field: 'Date', visible: true },
                { title: 'Time', field: 'Time', visible: true },
                { title: 'Project ID', field: 'ProjectID', visible: true },
                { title: 'Batch', field: 'Batch', visible: true },
                { title: 'Language', field: 'Language', visible: true },
                { title: 'Status', field: 'Status', visible: true }
            ];
            $scope.tableParams = new ngTableParams({
                page: 1,            // show first page
                count: 10,          // count per page
                filter: {
                    name: 'M'       // initial filter
                }
            }, {
                total: data.length, // length of data
                getData: function($defer, params) {
                    // use build-in angular filter
                    var orderedData = params.sorting() ?
                            $filter('orderBy')(data, params.orderBy()) :
                            data;

                    $defer.resolve(orderedData.slice((params.page() - 1) * params.count(), params.page() * params.count()));
                }
            });
});*/
