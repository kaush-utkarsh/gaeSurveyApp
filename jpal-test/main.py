import webapp2
import os
import jinja2
from gaesessions import get_current_session
import webapp2
import cloudDbHandler as dbHandler
import json
jinja_environment = jinja2.Environment(autoescape = True,
	loader = jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), 'templates/pages')))

class MainHandler(webapp2.RequestHandler):
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
			functionality=dbHandler.GetData().getRoleFunctionality(user_id)
			func = json.dumps(functionality, ensure_ascii=False)
			self.response.write(func)

class ManageResearcher(webapp2.RequestHandler):
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
		session = get_current_session()
		login = session.get('login')
		if login == "admin":
			template=jinja_environment.get_template('manager.html')
		else:
			session['error'] = "Login first"
			template = jinja_environment.get_template('login.html')
		self.response.write(template.render())


class SurveyManage(webapp2.RequestHandler):
	def get(self):
		session = get_current_session()
		session = get_current_session()
		login = session.get('login')
		if login == "admin":
			template = jinja_environment.get_template('surveys.html')
		else:
			session['error'] = "Login first"
			template = jinja_environment.get_template('login.html')
		self.response.write(template.render())

class DataViewer(webapp2.RequestHandler):
	def get(self):
		session = get_current_session()
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





app = webapp2.WSGIApplication([
	('/', MainHandler),
	('/login', Login),
	('/logout', Logout),
	('/profile', Profile),
	('/profile-edit',Edit_Form),
	('/user', UserManage),
	('/surveys',SurveyManage),
	('/data-view',DataViewer),
	('/sms',Scheduler),
	('/manage-projects',ManageProject),
	('/apiResearcher',APIResearcher),
	('/manage_researcher',ManageResearcher),
	('/entrepeneur',Reports)

], debug = True)
