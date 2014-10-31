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



class Edit_Form(webapp2.RequestHandler):
	def get(self):
		session = get_current_session()
		login = session.get('login')
		if login == "admin":
			template = jinja_environment.get_template('profile.html')
		else:
			session['error'] = "Login first"
			template = jinja_environment.get_template('login.html')
		self.response.write(template.render())

class UserManage(webapp2.RequestHandler):
	def get(self):
		session = get_current_session()
		login = session.get('login')
		if login == "admin":
			template=jinja_environment.get_template('manager.html')
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

class DataViewer(webapp2.RequestHandler):
	def get(self):
		session = get_current_session()
		login = session.get('login')
		if login == "admin":
			template = jinja_environment.get_template('sms.html')
		else:
			session['error'] = "Login first"
			template = jinja_environment.get_template('login.html')
		self.response.write(template.render())

class Scheduler(webapp2.RequestHandler):
	def get(self):
		session = get_current_session()
		count = session.get('count',0)
		session['count'] = count+1
		# jinja_environment=jinja2.Environment(autoescape=True, loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__),'templates')))
		template = jinja_environment.get_template('index.html')
		tpl_vars = {'counter':session['count']}
		self.response.write(template.render(tpl_vars))


class ManageProject(webapp2.RequestHandler):
	def get(self):
		session = get_current_session()
		session = get_current_session()
		login = session.get('login')
		if login == "admin":
			template = jinja_environment.get_template('data.html')
		else:
			session['error'] = "Login first"
			template = jinja_environment.get_template('login.html')
		self.response.write(template.render())


class Reports(webapp2.RequestHandler):
	def get(self):
		session = get_current_session()
		count = session.get('count',0)
		session['count'] = count+1
		# jinja_environment=jinja2.Environment(autoescape=True, loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__),'templates')))
		template = jinja_environment.get_template('index.html')
		tpl_vars = {'counter':session['count']}
		self.response.write(template.render(tpl_vars))

class APIResearcher(webapp2.RequestHandler):
	def get(self):
		functionality=dbHandler.GetData().getResearchers()
		func = json.dumps(functionality, ensure_ascii=False)
		self.response.write(func)
	def post(self):
		functionality=dbHandler.GetData().getResearchers()
		func = json.dumps(functionality, ensure_ascii=False)
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
		func = json.dumps(functionality, ensure_ascii=False)
		self.response.write(func)
	
	def post(self):
		user_id = self.request.get('user_id')
		data=dbHandler.GetData().getRoleFunctionality(user_id)
		user=dbHandler.GetData().getProfile(user_id)
		functionality={'navs' : data, 'user': user}
		func = json.dumps(functionality, ensure_ascii=False)
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
		func = json.dumps(functionality, ensure_ascii=False)
		self.response.write(func)

app = webapp2.WSGIApplication([
	('/', MainHandler),
	('/login', Login),
	('/logout', Logout),
	('/profile', Profile),
	('/profile-edit',Edit_Form),
	('/user', UserManage),
	('/view_survey',Survey),
	('/data-view',DataViewer),
	('/sms',Scheduler),
	('/manage-projects',ManageProject),
	('/apiResearcher',APIResearcher),
	('/apiUserProfile',UserProfile),
	('/apiSaveProfile',SaveProfile),
	('/manage_researcher',ManageResearcher),
	('/deleteUser',DelUser),
	('/undoUserDelete',UndoDelUser),
	('/entrepeneur',Reports),
	('/apiViewSurveys',apiViewSurveys)

], debug = True)
