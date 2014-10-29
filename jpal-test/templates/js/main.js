'use strict';
var surveyApp = angular.module('surveyApp',['ngRoute', 'ngTable']);

surveyApp.factory('surveyFactory',['$http', function($http) {
	 
	 var user=localStorage.user
	 var datum;
        $.ajax({
            url: "/apiUserProfile",
            type: "post",
            async: false,
            data: {user_id:user},
            dataType: "html",
            success: function (data) {
                // console.log(data)
                datum=JSON.parse(data)
                // localStorage.user = data;
                // console.log(nv)
                // window.location.assign("/")
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
			controller  : 'surveysController'
		})

		.when('/manage_researcher', {
			templateUrl : 'pages/researchers.html',
			controller  : 'researchersController'
		})

		.when('/survey', {
			templateUrl : 'pages/survey.html',
			controller  : 'surveyController'
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

		.when('/manager', {	
			templateUrl : 'pages/manager.html',
			controller  : 'managerController'
		})

		.when('/entrepreneur', {	
			templateUrl : 'pages/entrepreneur.html',
			controller  : 'entreController'
		})
	$locationProvider.html5Mode(true);
});

surveyApp.controller('appController', function($scope,surveyFactory) {
	$scope.user = surveyFactory.user;
	$scope.navs = surveyFactory.navs;
});

surveyApp.controller('profileController', function($scope,surveyFactory) {
	$scope.user = surveyFactory.user;
	$scope.navs = surveyFactory.navs;
});

surveyApp.controller('surveysController', function($scope,surveyFactory) {
	$scope.surveys = surveyFactory.surveys;
});

surveyApp.controller('researchersController', function($scope,surveyFactory) {
	$.ajax({
            url: "/apiResearcher",
            type: "post",
            async: false,
            dataType: "html",
            success: function (data) {
                console.log(data)
                localStorage.Researchers = data;
            },
        });


	var rs=JSON.parse(localStorage.Researchers)
	$scope.researchers = rs.researchers
});

surveyApp.controller('settingsController', function($scope,surveyFactory) {
	$scope.User = surveyFactory.user;
});

surveyApp.controller('surveyController', function($scope,surveyFactory) {
	$scope.Type = surveyFactory.surveys[0].Type;
	$scope.survey = surveyFactory.surveys[0].Sections;
	$scope.questions = surveyFactory.surveys[0].Sections[0].Question;
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
	$scope.managers = surveyFactory.managers;
	$scope.projects = surveyFactory.projects;
});

surveyApp.controller('dataController', function($scope, $filter, ngTableParams, surveyFactory) {
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
});