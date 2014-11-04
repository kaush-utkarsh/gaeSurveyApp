import webapp2
import os
import jinja2
from gaesessions import get_current_session
import webapp2
import cloudDbHandler as dbHandler
import json
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
		self.response.write(func)
	
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
	('/verifySection',apiVerifySection)

], debug = True)
