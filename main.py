import webapp2
import os
import jinja2
from gaesessions import get_current_session
import webapp2
import cloudDbHandler as dbHandler
import json
from MailHandler import Mail

jinja_environment = jinja2.Environment(autoescape = True,
	loader = jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), 'templates')))

class MainHandler(webapp2.RequestHandler):
	def get(self):
		session = get_current_session()
		if session.has_key('login'):
			template = jinja_environment.get_template('index.html')
		else:
			template = jinja_environment.get_template('login.html')
		self.response.write(template.render())
# pageMapDESurveyor

class pageMapDESurveyor(webapp2.RequestHandler):
	def get(self):
		session = get_current_session()
		if session.has_key('login'):
			template = jinja_environment.get_template('index.html')
		else:
			template = jinja_environment.get_template('login.html')
		self.response.write(template.render())

class Profile(webapp2.RequestHandler):
	def get(self):
		session = get_current_session()
		if session.has_key('login'):
			template = jinja_environment.get_template('index.html')
		else:
			template = jinja_environment.get_template('login.html')
		self.response.write(template.render())

	def post(self):
		session = get_current_session()
		login = session.get('login')
		if login == "admin":
			template = jinja_environment.get_template('index.html')
		else:
			session['error'] = "Login first"
			template = jinja_environment.get_template('login.html')
		self.response.write(template.render())

class Survey(webapp2.RequestHandler):
	def get(self):
		session = get_current_session()
		if session.has_key('login'):
			template = jinja_environment.get_template('index.html')
		else:
			template = jinja_environment.get_template('login.html')
		self.response.write(template.render())

class VerifySurvey(webapp2.RequestHandler):
	def get(self):
		session = get_current_session()
		if session.has_key('login'):
			template = jinja_environment.get_template('index.html')
		else:
			template = jinja_environment.get_template('login.html')
		self.response.write(template.render())

class APIResearcher(webapp2.RequestHandler):
	def get(self):
		functionality=dbHandler.GetData().getResearchers()
		func = json.dumps(functionality)
		self.response.write(func)
	def post(self):
		functionality=dbHandler.GetData().getResearchers()
		func = json.dumps(functionality)
		self.response.write(func)

class Logout(webapp2.RequestHandler):
	def get(self):
		get_current_session().terminate(clear_data=True)
		self.response.write("session ended")
	def post(self):
		get_current_session().terminate(clear_data=True)
		self.response.write("session ended")

class UserProfile(webapp2.RequestHandler):
	def get(self):
		user_id = self.request.get('user_id')
		data=dbHandler.GetData().getRoleFunctionality(user_id)
		user=dbHandler.GetData().getProfile(user_id)
		functionality={'navs' : data, 'user': user}
		func = json.dumps(functionality)
		self.response.write(func)
	
	def post(self):
		user_id = self.request.get('user_id')
		data=dbHandler.GetData().getRoleFunctionality(user_id)
		user=dbHandler.GetData().getProfile(user_id)
		functionality={'navs' : data, 'user': user}
		func = json.dumps(functionality)
		self.response.write(func)

		
class Login(webapp2.RequestHandler):
	def get(self):
		session = get_current_session()
		if session.has_key('login'):
			template = jinja_environment.get_template('index.html')
		else:
			template = jinja_environment.get_template('login.html')
		self.response.write(template.render())
		
	def post(self):
		login = self.request.get('username')
		pwd = self.request.get('password')
		session = get_current_session()
		user_id=dbHandler.GetData().checkUserAuth(login,pwd)
		if len(user_id)>1:
			session['login'] = login
			session['user_id'] = user_id
			self.response.write(user_id)
		else:
			template = jinja_environment.get_template('login.html')
			self.response.write(template.render())

class ManageResearcher(webapp2.RequestHandler):
	def get(self):
		session = get_current_session()
		if session.has_key('login'):
			template = jinja_environment.get_template('index.html')
		else:
			template = jinja_environment.get_template('login.html')
		self.response.write(template.render())


class SaveProfile(webapp2.RequestHandler):

	def post(self):
		post_data = self.request.POST
		dbHandler.PostData().saveProfileData(post_data)
		self.response.write('true')

class DelUser(webapp2.RequestHandler):

	def post(self):
		user_id = self.request.get('user_id')
		dbHandler.PostData().deleteUser(user_id)
		self.response.write('true')

class UndoDelUser(webapp2.RequestHandler):

	def post(self):
		user_id = self.request.get('user_id')
		dbHandler.PostData().undoDeleteUser(user_id)
		self.response.write('true')

class apiViewSurveys(webapp2.RequestHandler):

	def post(self):
		user_id = self.request.get('user_id')
		print user_id
		data=dbHandler.GetData().getDeSurveys(user_id)
		functionality=data #{'surveys' : data}
		func = json.dumps(functionality)
		self.response.write(func)

class apiReturnSurvey(webapp2.RequestHandler):

	def get(self):
		user_id = self.request.get('part_id')
		data=dbHandler.GetData().getSurveySections(user_id)
		# sect_id=data[0].sect_id
		sect_id=data[0]['sect_id']
		sect_name=data[0]['sect_text']
		sectdat=dbHandler.GetData().getSectionQuest(user_id,sect_id)
		sectfunc={'sect_id': sect_id,'sect_name': sect_name, 'ques' : sectdat}

		functionality={'part_id': user_id, 'sections' : data, 'sect':sectfunc}
		func = json.dumps(functionality)
		
		session = get_current_session()
		if session.has_key('login'):
			template = jinja_environment.get_template('index.html')
		else:
			template = jinja_environment.get_template('login.html')
		self.response.write(template.render(func))
	
	def post(self):
		user_id = self.request.get('part_id')
		data=dbHandler.GetData().getSurveySections(user_id)
		# sect_id=data[0].sect_id
		sect_id=data[0]['sect_id']
		sect_name=data[0]['sect_text']
		sectdat=dbHandler.GetData().getSectionQuest(user_id,sect_id)
		sectfunc={'sect_id': sect_id,'sect_name': sect_name, 'ques' : sectdat}

		functionality={'part_id': user_id, 'sections' : data, 'sect':sectfunc}
		func = json.dumps(functionality)
		self.response.write(func)

class apiReturnSection(webapp2.RequestHandler):

	def get(self):
		user_id = self.request.get('part_id')
		sect_id = self.request.get('sect_id')
		sect_name = self.request.get('sect_name')
		data=dbHandler.GetData().getSectionQuest(user_id,sect_id)
		functionality={'sect_id': sect_id,'sect_name': sect_name, 'ques' : data}
		func = json.dumps(functionality)
		self.response.write(func)

	def post(self):
		user_id = self.request.get('part_id')
		sect_id = self.request.get('sect_id')
		sect_name = self.request.get('sect_name')
		data=dbHandler.GetData().getSectionQuest(user_id,sect_id)
		functionality={'sect_id': sect_id,'sect_name': sect_name, 'ques' : data}
		func = json.dumps(functionality)
		self.response.write(func)
		
class FlagSurvey(webapp2.RequestHandler):
	def get(self):
		session = get_current_session()
		if session.has_key('login'):
			template = jinja_environment.get_template('index.html')
		else:
			template = jinja_environment.get_template('login.html')
		self.response.write(template.render())

class SurveyApprovalView(webapp2.RequestHandler):
	def get(self):
		session = get_current_session()
		if session.has_key('login'):
			template = jinja_environment.get_template('index.html')
		else:
			template = jinja_environment.get_template('login.html')
		self.response.write(template.render())

class apiCheckSection(webapp2.RequestHandler):

	def post(self):
		checked = self.request.get('checked')
		# self.response.write(checked)
		unchecked = self.request.get('unchecked')
		try:
			dbHandler.PostData().checkInitSection(checked)
		except Exception,e:
			pass
		try:
			dbHandler.PostData().unCheckInitSection(unchecked)
		except Exception,e:
			pass
		self.response.write('true')

class apiSubmitFlag(webapp2.RequestHandler):

	def post(self):
		part_id = self.request.get('part_id')
		dbHandler.PostData().submitFlag(part_id)
		self.response.write('true')


class apiVerifySurveys(webapp2.RequestHandler):

	def get(self):
		user_id = self.request.get('user_id')
		data=dbHandler.GetData().getVerifySurveys(user_id)
		functionality=data #{'surveys' : data}
		func = json.dumps(functionality)
		self.response.write(func)

	def post(self):
		user_id = self.request.get('user_id')
		data=dbHandler.GetData().getVerifySurveys(user_id)
		functionality=data #{'surveys' : data}
		func = json.dumps(functionality)
		self.response.write(func)


class apiViewFlaggedSection(webapp2.RequestHandler):

	def get(self):
		user_id = self.request.get('part_id')
		data=dbHandler.GetData().getFlaggedSections(user_id)
		# sect_id=data[0].sect_id
		if len(data)>0:
			sect_id=data[0]['sect_id']
			sect_name=data[0]['sect_text']
			sectdat=dbHandler.GetData().getFlaggedQuest(user_id,sect_id)
			sectfunc={'sect_id': sect_id,'sect_name': sect_name, 'ques' : sectdat}
		else:
			sectfunc={'sect_id': 'null','sect_name': 'null', 'ques' : 'null'}
		functionality={'part_id': user_id, 'sections' : data, 'sect':sectfunc}
		func = json.dumps(functionality)
		self.response.write(func)
	
	def post(self):
		user_id = self.request.get('part_id')
		data=dbHandler.GetData().getFlaggedSections(user_id)
		# sect_id=data[0].sect_id
		if len(data)>0:
			sect_id=data[0]['sect_id']
			sect_name=data[0]['sect_text']
			sectdat=dbHandler.GetData().getFlaggedQuest(user_id,sect_id)
			sectfunc={'sect_id': sect_id,'sect_name': sect_name, 'ques' : sectdat}
		else:
			sectfunc={'sect_id': 'null','sect_name': 'null', 'ques' : 'null'}
		functionality={'part_id': user_id, 'sections' : data, 'sect':sectfunc}
		func = json.dumps(functionality)
		self.response.write(func)

class apiViewFlaggedQuestion(webapp2.RequestHandler):

	def get(self):
		user_id = self.request.get('part_id')
		sect_id = self.request.get('sect_id')
		sect_name = self.request.get('sect_name')
		data=dbHandler.GetData().getFlaggedQuest(user_id,sect_id)
		functionality={'sect_id': sect_id,'sect_name': sect_name, 'ques' : data}
		func = json.dumps(functionality)
		self.response.write(func)

	def post(self):
		user_id = self.request.get('part_id')
		sect_id = self.request.get('sect_id')
		sect_name = self.request.get('sect_name')
		data=dbHandler.GetData().getFlaggedQuest(user_id,sect_id)
		functionality={'sect_id': sect_id,'sect_name': sect_name, 'ques' : data}
		func = json.dumps(functionality)
		self.response.write(func)
	
class apiVerifySection(webapp2.RequestHandler):

	def post(self):
		checked = self.request.get('checked')
		# self.response.write(checked)
		unchecked = self.request.get('unchecked')
		try:
			dbHandler.PostData().approveSection(checked)
		except Exception,e:
			pass
		try:
			dbHandler.PostData().disapproveSection(unchecked)
		except Exception,e:
			pass
		self.response.write('true')	

class SurveyData(webapp2.RequestHandler):
	def get(self):
		project_id = self.request.get("project_id")
		survey_id = self.request.get("survey_id")
		starting_value = self.request.get("starting_value")
		ending_value = self.request.get("ending_value")
		all_question = dbHandler.GetData().getAllQuestions(survey_id)
		all_questions = [_tuple[0] for _tuple in all_question]
		result = dbHandler.GetData().getSurveyData(survey_id, project_id, starting_value, ending_value)
		result_dict	=[{'participant_ID':item[0],'question':item[4],'answer':item[2],'option':item[5],'lang_id':item[6]} for item in result]
		all_participants=list(set([item['participant_ID'] for item in result_dict]))
		#all_questions = list(set([item['question'] for item in result_dict]))
		final_list = []
		language = ''
		for participant in all_participants:
			participant_dict = {"participant_ID":participant,"questions":[]}
			temp_questions = [item for item in all_questions]
			for item in result_dict:
				if item['participant_ID'] == participant:
					language = item['lang_id']
					participant_dict['questions'].append({"question":item['question'],"answer":item['answer'],"option":item['option']})
					temp_questions.pop(temp_questions.index(item['question']))
			if len(temp_questions) > 0:
				for item in temp_questions:
					participant_dict['questions'].append({"question":item,"answer":"None","option":"None"})
			if language == None:
				language = ""
			participant_dict.update({"lang_id":language})
			final_list.append(participant_dict)
		self.response.write(final_list)

class AddUser(webapp2.RequestHandler):
	def get(self):
		first_name = self.request.get("first_name")
		last_name = self.request.get("last_name")
		email = self.request.get("email")
		role = self.request.get("role")
		DOB = self.request.get("DOB")
		username = dbHandler.GetData().getUsername(first_name,last_name)
		dbHandler.PostData().addUser(username ,first_name, last_name,email, role, DOB)
		sender = "priyank@innovaccer.com"
		to = email
		subject = "User credentials for ENTRE INFO"
		body = "<html><head></head><body><b>Username:</b><i>"+username+"</i></br><b>Password:</b><i>"+first_name+"_"+DOB.replace("/","")+"</i></body></html>"
		Mail().dispatch(sender, to, subject, body, '', '')


class LoginSync(webapp2.RequestHandler):
	def post(self):
		request = json.loads(self.request.body)
		login_id =  request['login_id']
		self.response.write(json.dumps(dbHandler.GetData().getUserDetails(login_id)))

class SurveyCorrectionSync(webapp2.RequestHandler):
	def post(self):
		request = json.loads(self.request.body)
		survey_id = request['survey_id']
		self.response.write(json.dumps(dbHandler.GetData().getCorrections(survey_id)))

class SurveyDataSync(webapp2.RequestHandler):
	def post(self):
		request = json.loads(self.request.body)
		data = request["data"]
		super_final_list = []
		for item in data:
			participant_ID = item['part_id']
			for _data_item in item['data']:
				final_list = []
				final_list.append(_data_item['survey_id'])
				final_list.append(participant_ID)
				final_list.append(_data_item['sect_id'])
				final_list.append(_data_item['ques_no'])
				final_list.append(_data_item['op_value'])
				final_list.append(_data_item['ans'])
				final_list.append(_data_item['view_type'])
				final_list.append(_data_item['language'])
				#final_list.append(_data_item['timestamp'])
				#final_list.append(_data_item['correction_flag'])
				super_final_list.append(tuple(final_list))
		response = dbHandler.PostData().addSurveyData(super_final_list)
		#self.response.write(super_final_list)
		self.response.write(response)


class SurveyDataMiscellaneous(webapp2.RequestHandler):
	def get(self):
		survey_details = dbHandler.GetData().getSurveyDetails()
		project_details = dbHandler.GetData().getProjectDetails()
		self.response.write(json.dumps({'survey_details':survey_details,'project_details':project_details}))


class displayMapDESurveyor(webapp2.RequestHandler):
	# To get mapping between Data Editor and Surveyor for display on screen.
	def get(self):
		pm_id = self.request.get('pm_id')	#Get PMID from front end

		deSu = dbHandler.GetData().getDESuMap(pm_id)
		print deSu
		list_user_id = deSu.keys()

		list_user = []
		for lu in list_user_id:
			list_user.append(lu)

		#Create a unique list of Data Editor and Surveyors
		if list_user_id:
			for de in list_user_id:
				print de
				list_user.extend(deSu[de])

			# Get Names of all users in the mapping.
			nameUserDict = dbHandler.GetData().getNameUser(list_user)
			print nameUserDict
			# Create JSON in desired structure 
			# {de_id: , de_name: , surveyors [{ID: '', name: '']}, {ID: '', name: '']}}
			de_su_dict = {}
			de_su_map = []
			for de in deSu.keys():
				print de
				de_su_dict['ID'] = de
				de_su_dict['name'] = nameUserDict[de]
				de_su_dict['surveyers'] = []
				suDict = {}
				for su in deSu[de]:
					print su
					suDict['ID'] = su
					suDict['name'] = nameUserDict[su]
					de_su_dict['surveyers'].append(suDict)
					print de_su_dict
					suDict = {}
				de_su_dict_bk = {}
				for k in de_su_dict.keys():
					de_su_dict_bk[k] = de_su_dict[k]
				de_su_map.append(de_su_dict_bk)
				# de_su_dict.clear()
			print de_su_dict
		else:
			# No Mapping present. Return Error Message
			de_su_dict = {}

		surveyer_list = dbHandler.GetData().getUnassSurveyor(pm_id)
		# print de_su_map
		func = json.dumps({'editor_surveyors':de_su_map, 'surveyers': surveyer_list}, ensure_ascii=False)
		self.response.write(func)
	
class ViewSurveyData(webapp2.RequestHandler):
	def get(self):
		session = get_current_session()
		if session.has_key('login'):
			template = jinja_environment.get_template('index.html')
		else:
			template = jinja_environment.get_template('login.html')
		self.response.write(template.render())


class DeleteMapping(webapp2.RequestHandler):
	def get(self):
		de_id = self.request.get("de_id")
		su_id = self.request.get("su_id")
		dbHandler.PostData().delDeSuMap(de_id,su_id)
		self.response.write("true")

class AddMapping(webapp2.RequestHandler):
	def get(self):
		de_id = self.request.get("de_id")
		print "de_id"
		print de_id
		su_id = self.request.get("su_id")
		print "su_id"
		print su_id
		pm_id = self.request.get("pm_id")
		print "pm_id"
		print pm_id
		print pm_id, de_id, su_id
		dbHandler.PostData().addDESurveyor(pm_id, de_id, su_id)	
		self.response.write({su_id,pm_id})




app = webapp2.WSGIApplication([
	('/', MainHandler),
	('/login', Login),
	('/logout', Logout),
	('/profile', Profile),
	('/view_survey',Survey),
	('/apiResearcher',APIResearcher),
	('/apiUserProfile',UserProfile),
	('/apiSaveProfile',SaveProfile),
	('/manage_researcher',ManageResearcher),
	('/deleteUser',DelUser),
	('/undoUserDelete',UndoDelUser),
	('/apiViewSurveys',apiViewSurveys),
	('/returnSurvey',apiReturnSurvey),
	('/returnSection',apiReturnSection),
	('/flag_survey',FlagSurvey),
	('/checkSection',apiCheckSection),
	('/survey_approval',SurveyApprovalView),
	('/submitFlags',apiSubmitFlag),
	('/apiVerifySurveys',apiVerifySurveys),
	('/apiViewFlaggedSection',apiViewFlaggedSection),
	('/apiViewFlaggedQuestion',apiViewFlaggedQuestion),
	('/verify_survey',VerifySurvey),
	('/verifySection',apiVerifySection),
	('/addUser',AddUser),
	('/login_details',LoginSync),

	('/survey_data_sync',SurveyDataSync),
	('/survey-misc',SurveyDataMiscellaneous),
	('/survey_data',SurveyData),
	('/getCorrectionsSync',SurveyCorrectionSync),
	('/view_survey_data',ViewSurveyData),
	('/de_mapping',displayMapDESurveyor),
	('/de_map',pageMapDESurveyor),
	('/del_map',DeleteMapping),
	('/add_map',AddMapping)

], debug = True)
