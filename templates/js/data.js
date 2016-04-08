/*********NAVIGATION*********/
links : [{
	name : '',
	icon : ''
}];

/********** ADMIN ********/
admin: {
	ID : '',
	firstName : '',
	lastName : '',
	email : '',
	phone : '',
	altPhone : '',
	accountType : '',
	password : '',
	address : '',
	street : '',
	city : '',
	state : '',
	country : ''
}

/********* SURVEY ************/

survey: {
	ID : '',
	surveyType : '',
	table : '',
	sections : [
		ID : '',
		sectionName : '',
		questions : [
			ID : '',
			question : '',
			answer : ''
		]
	]
}

/************ RESEARCHER ********/

researcher: {
	ID : '',
	firstName : '',
	lastName : '',
	age: '',
	email : '',
	phone : '',
	altPhone : '',
	accountType : '',
	password : '',
	address : '',
	street : '',
	city : '',
	state : '',
	country : ''
}

data: {
	projectID : '',
	enterprenaurID : '',
	companyName : '',
	clinetName : '',
	bizName : '',
	phone : '',
	email : ''
}

surveysList : {
	ID : '',
	name : '',
	surveyer : '',
	participantID : '',
	companyName : '',
	location : '',
	completion : '',
	surveys: [
		ID : '',
		surveyType : '',
		table : '',
		sections : [
			ID : '',
			sectionName : '',
			questions : [
				ID : '',
				question : '',
				answer : ''
			]
		]
	]
}

projManager : {
	ID : '',
	name : '',
	project : ''
}

/*******PROJECT MANAGER*******/

projManager : {
	ID : '',
	firstName : '',
	lastName : '',
	age: '',
	email : '',
	phone : '',
	altPhone : '',
	accountType : '',
	password : '',
	address : '',
	street : '',
	city : '',
	state : '',
	country : ''
	assignedProjects : [
		projectName : ''
	]
}

project : {
	ID : '',
	name : ''
}

sms : {
	ID : '',
	participantID : '',
	companyName : '',
	projectID : '',
	scheduledDate : '',
	scheduledTime : '',
	location : '',
	week : '',
	level : '',
	repliedOn : ''
}

/********DATA EDITOR*******/

dataEditor : {
	ID : '',
	firstName : '',
	lastName : '',
	age: '',
	email : '',
	phone : '',
	altPhone : '',
	accountType : '',
	password : '',
	address : '',
	street : '',
	city : '',
	state : '',
	country : ''
	assignedProjects : [
		projectName : ''
	]
}

/*********SURVEYOR*********/

surveyor : {
	ID : '',
	firstName : '',
	lastName : '',
	age: '',
	email : '',
	phone : '',
	altPhone : '',
	accountType : '',
	password : '',
	address : '',
	street : '',
	city : '',
	state : '',
	country : ''
	assignedProjects : [
		projectName : ''
	]
}
