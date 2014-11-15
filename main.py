import webapp2
import os
import jinja2
from gaesessions import get_current_session
import webapp2
import cloudDbHandler as dbHandler
import json
from MailHandler import Mail
from csv_writer import getCsv

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
			if 'de_map' in session['functionalities']:
				template = jinja_environment.get_template('index.html')
			else:
				template = jinja_environment.get_template('404.html')
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
			if 'view_survey' in session['functionalities']:
				template = jinja_environment.get_template('index.html')
			else:
				template = jinja_environment.get_template('404.html')
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
		self.response.headers["Pragma"]="no-cache"
		self.response.headers["Cache-Control"]="no-cache, no-store, must-revalidate, pre-check=0, post-check=0"
		self.response.write("session ended")
	def post(self):
		get_current_session().terminate(clear_data=True)
		self.response.headers["Pragma"]="no-cache"
		self.response.headers["Cache-Control"]="no-cache, no-store, must-revalidate, pre-check=0, post-check=0"
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


		self.response.headers["Pragma"]="no-cache"
		self.response.headers["Cache-Control"]="no-cache, no-store, must-revalidate, pre-check=0, post-check=0"
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
			session['functionalities']=dbHandler.GetData().getFunctionalities(user_id)
			self.response.write(user_id)
		else:
			template = jinja_environment.get_template('login.html')
			self.response.write(template.render())

class ManageResearcher(webapp2.RequestHandler):
	def get(self):
		session = get_current_session()
		if session.has_key('login'):
			if 'manage_researcher' in session['functionalities']:
				template = jinja_environment.get_template('index.html')
			else:
				template = jinja_environment.get_template('404.html')
		else:
			template = jinja_environment.get_template('login.html')
		self.response.write(template.render())


class SaveProfile(webapp2.RequestHandler):

	def post(self):
		post_data = self.request.POST
		print post_data
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
		
		# session = get_current_session()
		# if session.has_key('login'):
		# 	template = jinja_environment.get_template('index.html')
		# else:
		# 	template = jinja_environment.get_template('login.html')
		self.response.write(func)
	
	def post(self):
		user_id = self.request.get('part_id')
		data=dbHandler.GetData().getSurveySections(user_id)
		print data
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
			if 'survey_approval' in session['functionalities']:
				template = jinja_environment.get_template('index.html')
			else:
				template = jinja_environment.get_template('404.html')
		else:
			template = jinja_environment.get_template('login.html')
		self.response.write(template.render())


class SMSMod(webapp2.RequestHandler):
	def get(self):
		session = get_current_session()
		if session.has_key('login'):
			if 'sms' in session['functionalities']:
				template = jinja_environment.get_template('index.html')
			else:
				template = jinja_environment.get_template('404.html')
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
			# dbHandler.PostData().disapproveSection(unchecked)
			dbHandler.PostData().checkInitSection(unchecked)
		except Exception,e:
			pass
		self.response.write('true')	

# class SurveyData(webapp2.RequestHandler):
# 	def get(self):
# 		project_id = self.request.get("project_id")
# 		survey_id = self.request.get("survey_id")
# 		starting_value = self.request.get("starting_value")
# 		ending_value = self.request.get("ending_value")
# 		all_question = dbHandler.GetData().getAllQuestions(survey_id)
# 		all_questions = [_tuple[0] for _tuple in all_question]
# 		result = dbHandler.GetData().getSurveyData(survey_id, project_id, starting_value, ending_value)
# 		result_dict	=[{'participant_ID':item[0],'question':item[4],'answer':item[2],'option':item[5],'lang_id':item[6]} for item in result]
# 		all_participants=list(set([item['participant_ID'] for item in result_dict]))
# 		final_list = []
# 		language = ''
# 		for participant in all_participants:
# 		 	participant_dict = {'participant_ID':participant,'questions':[]}
# 			temp_questions = []
# 			for item in result_dict:
# 				if item['participant_ID'] == participant:
# 					language = item['lang_id']
# 					participant_dict['questions'].append({'question':item['question'],'answer':item['answer'],'option':item['option']})
# 					temp_questions.append(item['question'])
# 			diff = set(all_questions).difference(set(temp_questions))
# 			if len(diff) > 0:
# 				for item in diff:
# 					participant_dict['questions'].append({"question":item,"answer":'','option':''})
# 			participant_dict.update({'lang_id':language})
# 			final_list.append(participant_dict)
# 		# print "Type ", type(final_list)
# 		# print json.dumps({'data':final_list},encoding='utf-8')
# 		self.response.write(json.dumps({'data':final_list},encoding='latin1'))

class SurveyData(webapp2.RequestHandler):
	def get(self):
		project_id = self.request.get("project_id")
		survey_id = self.request.get("survey_id")
		starting_value = self.request.get("starting_value")
		ending_value = self.request.get("ending_value")
		all_questions = dbHandler.GetData().getAllQuestionsAndIds(survey_id)
		print all_questions
		all_options = dbHandler.GetData().getOptions(survey_id)
		all_participants = dbHandler.GetData().getSurveyData(starting_value,ending_value)
		# for party in all_participants:
		# 	party.pop(0)
		self.response.write(json.dumps({'questions':all_questions, 'participants':all_participants}))


class AddUser(webapp2.RequestHandler):
	def get(self):
		first_name = self.request.get("first_name")
		last_name = self.request.get("last_name")
		email = self.request.get("email")
		role = self.request.get("role")
		username = dbHandler.GetData().getUsername(first_name,last_name)
		user_id=dbHandler.PostData().addUser(username ,first_name, last_name,email, role)
		mailer='true'
		try:
			pm_id=self.request.get("pm_id")
			p_id=dbHandler.GetData().getProjectId(pm_id)
			dbHandler.PostData().addProjectUser(p_id,user_id,role)
			to = dbHandler.GetData().getEmail(pm_id)
			mailer='false'
		except Exception,e:
			pass

		if mailer=='true':
			to = email

		sender = "priyank@innovaccer.com"
		subject = "User credentials for ENTRE INFO"
		body = "<html><head></head><body><b>Username:</b><i>"+username+"</i></br><b>Password:</b><i>"+first_name+"</i></body></html>"
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

# class SurveyDataSync(webapp2.RequestHandler):
# 	def post(self):
# 		request = json.loads(self.request.body)
# 		data = request["data"]
# 		super_final_list = []
# 		for item in data:
# 			participant_ID = item['part_id']
# 			for _data_item in item['data']:
# 				final_list = []
# 				final_list.append(_data_item['survey_id'])
# 				final_list.append(participant_ID)
# 				final_list.append(_data_item['sect_id'])
# 				final_list.append(_data_item['ques_no'])
# 				final_list.append(_data_item['op_value'])
# 				final_list.append(_data_item['ans'])
# 				final_list.append(_data_item['view_type'])
# 				final_list.append(_data_item['language'])
# 				#final_list.append(_data_item['timestamp'])
# 				#final_list.append(_data_item['correction_flag'])
# 				super_final_list.append(tuple(final_list))
# 		response = dbHandler.PostData().addSurveyData(super_final_list)
# 		#self.response.write(super_final_list)
# 		self.response.write(response)


class SurveyDataSync(webapp2.RequestHandler):
	def post(self):
		radioQues=['8','11i','13','16','27','33','34','Z1','26']
		#-------------------------------------------------------------------------------
		#print self.request.get("usersJSON")
		request = json.loads(self.request.get("usersJSON"))
		# sections = dbHandler.GetData().getAllSections()
		data = request
		super_final_list = []
		participant_ID_ = ''
		survey_id_ = ''
		for _data_item in data:
			final_list = []
			final_list.append(_data_item['survey_id'])
			final_list.append(_data_item['part_id'])
			final_list.append(_data_item['sect_id'])
			final_list.append(_data_item['ques_no'])
			final_list.append(_data_item['op_value'])
			try:
				final_list.append(_data_item['ans'])
			except Exception,e:
				final_list.append('')
			final_list.append(_data_item['view_type'])
			final_list.append(_data_item['language'])
			final_list.append(_data_item['created_at'])
			final_list.append(_data_item['correction_flag'])
			final_list.append(_data_item['ID'])
			super_final_list.append(tuple(final_list))
			participant_ID_ = _data_item['part_id']
			survey_id_ = _data_item['survey_id']
			# print _data_item['ans']
		print "part_id"
		print participant_ID_
		survey_id_ = participant_ID_.split("SU")[0]
		surveyor_id = participant_ID_.split(survey_id_)[1]
		surveyor_id = surveyor_id.split("EN")[0]
		print "surveyor_id"
		print surveyor_id
		status1 = dbHandler.PostData().addSurveyData(super_final_list)
		print "status from addSurveyData"+status1
		#------------------------------------------------------------------------------
		
		participants_id = [item['part_id'] for item in data]
		participants_id = list(set(participants_id))
		participant_list = []
		participant_list.append({'part_id':participants_id[0]})
		lang = ''
		#-------------------------------------change for options--------------------------
		options_tuple = dbHandler.GetData().getOptions('GRO01')
		print "options tuple"
		print options_tuple
		#-----------------------------------------
		# for item in data:
		# 	try:
		# 		participant_list.append({item['ques_no']:(item['op_value']+": "+item['ans']+"")})
		# 	except Exception,ex:
		# 		participant_list.append({item['ques_no']:(item['op_value'])})
		# 	lang = item['language']
		for item in data:
			for option in options_tuple:
				if (str(item['ques_no']).strip() == str(option[0]).strip()) and (str(item['op_value']).strip()==str(option[1]).strip()):
					if item['ques_no'] in radioQues:
						if option[3] == 'text_box':
							participant_list.append({item['ques_no']:(option[2])})
							participant_list.append({item['ques_no']+'-TB':(item['ans'])})

						else:
							participant_list.append({item['ques_no']:(option[2])})
							participant_list.append({item['ques_no']+'-TB':('')})
					else:
						try:
							participant_list.append({item['ques_no']:(option[2]+": "+item['ans']+"")})
						except Exception,ex:
							participant_list.append({item['ques_no']:(option[2])})
					lang = item['language']
		print participant_list
		for item in participant_list:
			if 'ignore' in item.keys():
				participant_list.remove(item)
		participant_list.append({'lang_id':lang})
		#self.response.write(participant_list)
		query = 'insert into view_data_table('
#		for item in participant_list:
#			query += ",".join(item[0].key())
#		query+=') values('
#		for item in participant_list:
#			query+= ",".join
		keys = [item.keys()[0] for item in participant_list]
		values = [item.values() for item in participant_list]
		query += "" + ",".join(["`%s`"]*len(keys)) % tuple(keys) + ") VALUES(" + ",".join(["%s"]*len(values)) + ")"
		values_list = []
		for item in values:
			values_list.append(item[0])
		status2 = dbHandler.PostData().view_data(query,tuple(values_list))
		print ("status1: "+ status1)
		print ("status2: "+ status2)
		#self.response.write(json.dumps(dbHandler.GetData().getCorrections('GRO01',surveyor_id)))
		
		sample_mock = [{"survey_data_id":"asd","survey_id":"asd","part_id":"asd","sect_id":"asd","ques_id":"raasd","ans":"asd","flag":"asd","corr_status":"asd","op_value":"asd"}]
		self.response.write(json.dumps(sample_mock))
		# if status1 == "200" and status2 =="200":
		# 	self.response.write("200")
		# else:
		# 	self.response.write("500")


class SurveyDataMiscellaneous(webapp2.RequestHandler):
	def get(self):
		survey_details = dbHandler.GetData().getSurveyDetails()
		project_details = dbHandler.GetData().getProjectDetails()
		self.response.write(json.dumps({'survey_details':survey_details,'project_details':project_details}))


class displayMapDESurveyor(webapp2.RequestHandler):
	# To get mapping between Data Editor and Surveyor for display on screen.
	def get(self):
		pm_id = self.request.get('pm_id')	#Get PMID from front end
		# self.response.write(pm_id)
		#Get Project Id
		p_id = dbHandler.GetData().getProjectId(pm_id)
		# self.response.write(p_id)
		#Get Data Editor List
		deList = dbHandler.GetData().getAllDE(p_id)
		print deList
		# self.response.write(deList)
		#Get Surveyors mapping
		deSuMap = dbHandler.GetData().getDESuMap(deList)
		# self.response.write(deSuMap) 
		# deSu = dbHandler.GetData().getDESuMap(pm_id)

		list_user = []
		for lu in deList:
			list_user.append(lu)

		de_su_map = []
		#Create a unique list of Data Editor and Surveyors
		if list_user:
			for de in deSuMap.keys():
				list_user.extend(deSuMap[de])
			
			# self.response.write(list_user)
			# Get Names of all users in the mapping.
			nameUserDict = dbHandler.GetData().getNameUser(list_user)
			# self.response.write(nameUserDict)
			# Create JSON in desired structure 
			# {de_id: , de_name: , surveyors [{ID: '', name: '']}, {ID: '', name: '']}}
			de_su_dict = {}
			de_su_map = []
			for de in deList:
				if de in deSuMap.keys():
					# print de
					de_su_dict['ID'] = de
					de_su_dict['name'] = nameUserDict[de]
					de_su_dict['surveyers'] = []
					suDict = {}
					for su in deSuMap[de]:
						print su
						suDict['ID'] = su
						suDict['name'] = nameUserDict[su]
						de_su_dict['surveyers'].append(suDict)
						# print de_su_dict
						suDict = {}
					de_su_dict_bk = {}
					for k in de_su_dict.keys():
						de_su_dict_bk[k] = de_su_dict[k]
					de_su_map.append(de_su_dict_bk)
				else:
					# print de
					de_su_dict['ID'] = de
					de_su_dict['name'] = nameUserDict[de]
					de_su_dict['surveyers'] = []
					de_su_dict_bk = {}
					for k in de_su_dict.keys():
						de_su_dict_bk[k] = de_su_dict[k]
					de_su_map.append(de_su_dict_bk)
				# de_su_dict.clear()
			# self.response.write(de_su_map)
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
			if 'view_survey_data' in session['functionalities']:
				template = jinja_environment.get_template('index.html')
			else:
				template = jinja_environment.get_template('404.html')
		else:
			template = jinja_environment.get_template('login.html')
		self.response.write(template.render())


class ManagePM(webapp2.RequestHandler):
	def get(self):
		session = get_current_session()
		if session.has_key('login'):
			if 'manage_pm' in session['functionalities']:
				template = jinja_environment.get_template('index.html')
			else:
				template = jinja_environment.get_template('404.html')
		else:
			template = jinja_environment.get_template('login.html')
		self.response.write(template.render())


class Settings(webapp2.RequestHandler):
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

class apiManagePM(webapp2.RequestHandler):
	def post(self):
		manager_project=dbHandler.GetData().getManagerProjects()
		unass_project=dbHandler.GetData().getUnassProjects()	
		functionality={'managers': manager_project,'projects': unass_project}
		func = json.dumps(functionality)
		self.response.write(func)


class apiAddPM(webapp2.RequestHandler):
	def post(self):
		first_name = self.request.get("first_name")
		last_name = self.request.get("last_name")
		email = self.request.get("email")
		role = self.request.get("role")
		
		project= self.request.get("project")
		username = dbHandler.GetData().getUsername(first_name,last_name)
		user_id=dbHandler.PostData().addUser(username ,first_name, last_name,email, role)
		sender = "priyank@innovaccer.com"
		to = email
		subject = "User credentials for ENTRE INFO"
		body = "<html><head></head><body><b>Username:</b><i>"+username+"</i></br><b>Password:</b><i>"+first_name+"</i></body></html>"
		Mail().dispatch(sender, to, subject, body, '', '')
		dbHandler.PostData().addProjectUser(project,user_id,'PM')

class apiAddProject(webapp2.RequestHandler):
	def post(self):
		project_name = self.request.get("project_name")
		project_u_id = self.request.get("project_user_id")
		dbHandler.PostData().addProject(project_u_id,project_name)
		
class apiDeletePM(webapp2.RequestHandler):
	def post(self):
		pm_id = self.request.get("pm_id")
		dbHandler.PostData().deleteUser(pm_id)
		dbHandler.PostData().deletePMmap(pm_id)
		self.response.write('true')

class UserPwd(webapp2.RequestHandler):
	def post(self):
		user_id = self.request.get("user_id")
		pwd = self.request.get("pwd")
		upwd=dbHandler.GetData().getPwd(user_id)
		if upwd==pwd:
			self.response.write('true')
		if upwd!=pwd:
			self.response.write('false')


class apiCheckPwd(webapp2.RequestHandler):
	def post(self):
		login_id = self.request.get("username")
		pwd = self.request.get("password")
		upwd=dbHandler.GetData().getloginPwd(login_id)
		print upwd
		resp = 'false'
		if len(upwd)!=0 and upwd==pwd:
			resp='true'

		self.response.write(resp)

class ChangePwd(webapp2.RequestHandler):
	def post(self):
		user_id = self.request.get("user_id")
		pwd = self.request.get("pwd")
		dbHandler.PostData().changePwd(user_id,pwd)
		self.response.write('true')

class checkProjectID(webapp2.RequestHandler):
	def post(self):
		p_id = self.request.get("project_user_id")
		count=dbHandler.GetData().checkPID(p_id)
		if count==0:
			self.response.write('true')
		else:
			self.response.write('false')
# ip- type- login_id/device_id  value- corresponding id	
# o/p- login_id password device_id f_name l_name
class appLogin(webapp2.RequestHandler):
	def post(self):
		urequest = json.loads(self.request.get("usersJSON"))
		l_type = urequest[0]["type"]
		l_value = urequest[0]["value"]
		if l_type=='login_id':
			print 'login'
			user=dbHandler.GetData().getLoginDet(l_value,'login_id')
			user_det=json.dumps(user)
		elif l_type=='device_id':
			print 'device'
			user=dbHandler.GetData().getLoginDet(l_value,'user_id')
			user_det=json.dumps(user)
		else:
			user_det='false'
		self.response.write(user_det)


class appCorrection(webapp2.RequestHandler):
	def get(self):
		surveyor_id = self.request.get("device_id")
		last_index = self.request.get("ID")
		surveys=dbHandler.GetData().getCorrectionsSur(surveyor_id,str(last_index))
		surveys_det=json.dumps(surveys)
		self.response.write(surveys_det)
	def post(self):
		urequest = json.loads(self.request.get("corrJSON"))
		surveyor_id = urequest[0]["device_id"]
		last_index = urequest[0]["ID"]
		surveys=dbHandler.GetData().getCorrectionsSur(surveyor_id,str(last_index))
		surveys_det=json.dumps(surveys)
		self.response.write(surveys_det)

class ExportData(webapp2.RequestHandler):
	def get(self):
		survey_id= self.request.get("survey_id")
		project_id = self.request.get("project_id")
		questions = list(self.request.get("questions"))
		


		project_id = self.request.get("project_id")
		survey_id = self.request.get("survey_id")
		if survey_id == 'null' or survey_id == None:
			survey_id = 'GRO01'
		all_questions = dbHandler.GetData().getAllQuestionsAndIds(survey_id)
		all_questions.insert(0,'Participant ID')
		#all_options = dbHandler.GetData().getOptions(survey_id)
		#all_participants = dbHandler.GetData().getSurveyData(starting_value,ending_value)
		all_participants = dbHandler.GetData().getAllSurveyData()
		headers = all_questions
		final_rows = all_participants
		for party in all_participants:
			party.pop(0)
		# data = dbHandler.GetData().getAllQuestionsAndIds(survey_id)
		# question_id_collection = [{'question_id':question[0], 'question_text': question[1]} for question in list(data)]
		# all_questions = [question['question_text'] for question in question_id_collection]
		# left_questions = set(all_questions)-set(questions)
		# final_question_collection = []
		# for question in left_questions:
		# 	for item in question_id_collection:
		# 		if item['question_text'] == question:
		# 			final_question_collection.append(item['question_id'])
		# query = ''
		# for row in final_question_collection:
		# 	if 'sect' not in row:
		# 		query += ' final.q_no = "'+ row + '" or'
		# query = query[:-2]
		# all_records_based_on_selected_questions  = dbHandler.GetData().getAllRecords(survey_id, project_id, query)
		# result_dict	=[{'participant_ID':item[0],'question':item[4],'answer':item[2],'option':item[5],'lang_id':item[6]} for item in all_records_based_on_selected_questions]
		# result_dict_questions = [item['question'] for item in result_dict]
		# all_question = dbHandler.GetData().getAllQuestions(survey_id)
		# all_questions = [_tuple[0] for _tuple in all_question]
		# final_questions=[]
		# final_questions.append('Participant ID')
		# final_questions.append('Language')
		# for item in left_questions: #change
		# 	final_questions.append(item)
		# headers = final_questions
		# participantIDs = [row['participant_ID'] for row in result_dict]
		# participantIDs = set(participantIDs)
		# participantData_list = []
		# for participant in participantIDs:
		# 	language =''
		# 	participantData = {'participant':participant,'answers_questions':[]}
		# 	for item in result_dict:
		# 		if  item['participant_ID'] == participant:
		# 			participantData['answers_questions'].append({"answer":item['answer'],"question":item['question']})
		# 			language = item['lang_id']
		# 	participantData.update({'language':language})
		# 	_final_list = []
		# 	__questions_answer_list = [row for row in participantData['answers_questions']]
		# 	question_lis = []
		# 	answer_lis =[]
		# 	for item in __questions_answer_list:
		# 		question_lis.append(item['question'])
		# 		answer_lis.append(item['answer'])
		# 	for _que in left_questions:
		# 		if _que in question_lis:
		# 			_final_list.append(answer_lis[question_lis.index(_que)])
		# 		else :
		# 			_final_list.append('')
		# 	participantData['answers_questions'] = []
		# 	participantData['answers_questions'].append(_final_list)
		# 	participantData_list.append(participantData)
		# final_rows = []
		# for item in participantData_list:
		# 	sample = []
		# 	sample.append(item['participant'])
		# 	if item['language'] == None:
		# 		sample.append("None")
		# 	else: sample.append(item['language'])
		# 	for answer in item['answers_questions'][0]:
		# 		sample.append(answer)
		# 	final_rows.append(sample)
		self.response.headers.add_header("Content-Type","application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
		self.response.headers.add_header("Content-Disposition","attachment; filename=SurveyData.CSV")
		#self.response.write(final_rows)
		self.response.write(getCsv(headers,final_rows))

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
	('/manage_pm',ManagePM),
	('/survey_data_sync',SurveyDataSync),
	('/survey-misc',SurveyDataMiscellaneous),
	('/survey_data',SurveyData),
	('/getCorrectionsSync',SurveyCorrectionSync),
	('/view_survey_data',ViewSurveyData),
	('/de_mapping',displayMapDESurveyor),
	('/de_map',pageMapDESurveyor),
	('/del_map',DeleteMapping),
	('/sms',SMSMod),
	('/add_map',AddMapping),
	('/apiManagePM',apiManagePM),
	('/addPM',apiAddPM),
	('/addProject',apiAddProject),
	('/settings',Settings),
	('/userPwd',UserPwd),
	('/changePwd',ChangePwd),
	('/deletePM',apiDeletePM),
	('/checkPwd',apiCheckPwd),
	('/export_csv',ExportData),
	('/checkProjectID',checkProjectID),
	('/appLogin',appLogin),
	('/appCorrection',appCorrection)


], debug = True)
