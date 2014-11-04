import webapp2
import jinja2
import cgi
import os
import smtplib
import json
import StringIO
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from google.appengine.api import mail
from google.appengine.ext import deferred
import time
import logging
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import parseaddr

SMTP_SERVER = "smtp.sendgrid.net"
SMTP_PORT = 587
SMTP_USERNAME = "lkoankit1"
SMTP_PASSWORD = "innovation123"


class Mail():
	def dispatch(self, sender, to, subject, body, cc=None, bcc=None):
		try:
			message = mail.EmailMessage()
			message.sender = sender
			message.subject = subject
			message.to = to
			if cc:
				message.cc = cc
			if bcc:
				message.bcc = bcc
			message.html = body
			message.send()
		except Exception, e:
			logging.error("Failed to send mail. Retrying with SMTP Mail.")
			logging.error(str(e))
			SMTPMail().dispatch(sender, to, subject, body, cc, bcc)


class SMTPMail(Mail):

	def dispatch(self, sender, to, subject, body, cc=None, bcc=None):
		message = MIMEMultipart('alternative')
		message["From"] = sender
		message["To"] = to
		message["Subject"] = subject

		recepients = []
		recepients.append(parseaddr(to)[1]) # strip out name from Name <email>
		if cc:
			if type(cc) == list:
				message["Cc"] = ", ".join(cc)
				for c in cc:
					recepients.append(parseaddr(c)[1]) # strip out name from Name <email>
			else:
				message["Cc"] = cc
				recepients.append(parseaddr(cc)[1]) # strip out name from Name <email>
		if bcc:
			if type(bcc) == list:
				message["Bcc"] = ", ".join(bcc)
				for c in bcc:
					recepients.append(parseaddr(c)[1]) # strip out name from Name <email>
			else:
				message["Bcc"] = bcc
				recepients.append(parseaddr(bcc)[1]) # strip out name from Name <email>

		message['Content-Type'] = "text/html; charset=utf-8"

		html_body = MIMEText(body, 'html', 'UTF-8')
		message.attach(html_body)
		
		s = smtplib.SMTP(host=SMTP_SERVER, port=SMTP_PORT)
		s.ehlo()

		try:
			print recepients
			s.login(SMTP_USERNAME, SMTP_PASSWORD)
			s.sendmail(sender, recepients, message.as_string())
		except Exception, e:
			print "Error sending email: " + str(e)

		s.quit()