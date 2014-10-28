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
		login = session.get('login')
		template = jinja_environment.get_template('index.html')
		self.response.write(template.render())

class Login(webapp2.RequestHandler):
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
		
	def post(self):
		login = self.request.get('username')
		pwd = self.request.get('password')
		session = get_current_session()
		user_id=dbHandler.GetData().checkUserAuth(login,pwd)
		# self.response.write(user_id)
		session = get_current_session()
		if len(user_id)>1:
			session['login'] = login
			session['user_id'] = user_id
			# session['error'] = "None"
			functionality=dbHandler.GetData().getRoleFunctionality(user_id)
			# print functionality
			func = json.dumps(functionality, ensure_ascii=False)
			# return functionality
			# template = jinja_environment.get_template('login.html')
			self.response.write(func)


class Profile(webapp2.RequestHandler):
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
	('/profile', Profile),
	('/profile-edit',Edit_Form),
	('/user', UserManage),
	('/surveys',SurveyManage),
	('/data-view',DataViewer),
	('/sms',Scheduler),
	('/manage-projects',ManageProject),
	('/entrepeneur',Reports)
], debug = True)
