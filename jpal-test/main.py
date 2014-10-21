import webapp2
import os
import jinja2
from gaesessions import get_current_session
import webapp2

jinja_environment = jinja2.Environment(autoescape=True,
	loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), 'templates/pages')))

class MainHandler(webapp2.RequestHandler):
	def get(self):
		session=get_current_session()
		count=session.get('count',0)
		session['count']=count+1
		# jinja_environment=jinja2.Environment(autoescape=True, loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__),'templates')))
		template=jinja_environment.get_template('index.html')
		tpl_vars={'counter':session['count']}
		self.response.write(template.render(tpl_vars))

class Login(webapp2.RequestHandler):
	def get(self):
		session=get_current_session()
		count=session.get('count',0)
		session['count']=count+1
		# jinja_environment=jinja2.Environment(autoescape=True, loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__),'templates')))
		template=jinja_environment.get_template('index.html')
		tpl_vars={'counter':session['count']}
		self.response.write(template.render(tpl_vars))


class Profile(webapp2.RequestHandler):
	def get(self):
		session=get_current_session()
		count=session.get('count',0)
		session['count']=count+1
		# jinja_environment=jinja2.Environment(autoescape=True, loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__),'templates')))
		template=jinja_environment.get_template('index.html')
		tpl_vars={'counter':session['count']}
		self.response.write(template.render(tpl_vars))



class Edit_Form(webapp2.RequestHandler):
	def get(self):
		session=get_current_session()
		count=session.get('count',0)
		session['count']=count+1
		# jinja_environment=jinja2.Environment(autoescape=True, loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__),'templates')))
		template=jinja_environment.get_template('index.html')
		tpl_vars={'counter':session['count']}
		self.response.write(template.render(tpl_vars))




class UserManage(webapp2.RequestHandler):
	def get(self):
		session=get_current_session()
		count=session.get('count',0)
		session['count']=count+1
		# jinja_environment=jinja2.Environment(autoescape=True, loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__),'templates')))
		template=jinja_environment.get_template('index.html')
		tpl_vars={'counter':session['count']}
		self.response.write(template.render(tpl_vars))



class SurveyManage(webapp2.RequestHandler):
	def get(self):
		session=get_current_session()
		count=session.get('count',0)
		session['count']=count+1
		# jinja_environment=jinja2.Environment(autoescape=True, loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__),'templates')))
		template=jinja_environment.get_template('index.html')
		tpl_vars={'counter':session['count']}
		self.response.write(template.render(tpl_vars))



class DataViewer(webapp2.RequestHandler):
	def get(self):
		session=get_current_session()
		count=session.get('count',0)
		session['count']=count+1
		# jinja_environment=jinja2.Environment(autoescape=True, loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__),'templates')))
		template=jinja_environment.get_template('index.html')
		tpl_vars={'counter':session['count']}
		self.response.write(template.render(tpl_vars))



class Scheduler(webapp2.RequestHandler):
	def get(self):
		session=get_current_session()
		count=session.get('count',0)
		session['count']=count+1
		# jinja_environment=jinja2.Environment(autoescape=True, loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__),'templates')))
		template=jinja_environment.get_template('index.html')
		tpl_vars={'counter':session['count']}
		self.response.write(template.render(tpl_vars))


class ManageProject(webapp2.RequestHandler):
	def get(self):
		session=get_current_session()
		count=session.get('count',0)
		session['count']=count+1
		# jinja_environment=jinja2.Environment(autoescape=True, loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__),'templates')))
		template=jinja_environment.get_template('index.html')
		tpl_vars={'counter':session['count']}
		self.response.write(template.render(tpl_vars))


class Reports(webapp2.RequestHandler):
	def get(self):
		session=get_current_session()
		count=session.get('count',0)
		session['count']=count+1
		# jinja_environment=jinja2.Environment(autoescape=True, loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__),'templates')))
		template=jinja_environment.get_template('index.html')
		tpl_vars={'counter':session['count']}
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
], debug=True)
