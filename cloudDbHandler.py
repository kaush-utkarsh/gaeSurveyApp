import StringIO
import webapp2
import jinja2
import cgi
import json
import ast
import datetime
import os
from google.appengine.api import rdbms

# Login Credentials

_INSTANCE_NAME = 'localhost' 
dbname = 'innovaccer_jpal'
usr='root'
pss='root'

#########################


class PostData():
	
	def addUser(self, username, first_name, last_name, email, role, DOB):
		conn = rdbms.connect(instance= _INSTANCE_NAME, database= dbname, user=usr, passwd= pss)
		cursor = conn.cursor()
		user_id = role + str(int(GetData().getUserCountWithRole(role)) + 10000 + 1)
		login_id = username
		login_password = first_name + "_" + DOB.replace("/","") 
		status = 1
		password_flag = 0
		sqlcmd = "insert into user(user_id, f_name, l_name,email,login_id,login_password,role, DOB, status, password_flag) values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (user_id, first_name,last_name,email,login_id,login_password,role,DOB,status, password_flag)
		cursor.execute(sqlcmd)
		conn.commit()
		conn.close()

	def addSurveyData(self, bulk_data):
		try:
			conn = rdbms.connect(instance= _INSTANCE_NAME, database= dbname, user=usr, passwd= pss)
			cursor = conn.cursor()
			sqlcmd = 'insert into survey_data(survey_id, part_id, sect_id, ques_no, op_id, op_text, view_type, lang_id) values (%s,%s,%s,%s,%s,%s,%s,%s)'
			cursor.executemany(sqlcmd, bulk_data)
			conn.commit()
			conn.close()
			return "200"
		except BaseException,er:
			return er


	# Function for updation of profile data through the profile page

	def saveProfileData(self,post_data):
		conn = rdbms.connect(instance=_INSTANCE_NAME, database=dbname, user=usr, passwd=pss, charset='utf8')
		cursor = conn.cursor()
		sqlcmd = "update user set f_name = %s , l_name = %s , DOB = %s ,primary_phone = %s, address = %s, line_1 = %s , city = %s ,state = %s, country = %s where user_id = %s "
		cursor.execute(sqlcmd,(post_data['f_name'],post_data['l_name'],post_data['DOB'],post_data['primary_phone'],post_data['address'],post_data['line_1'],post_data['city'],post_data['state'],post_data['country'],post_data['user_id'],))
		conn.commit()
		conn.close() 

	# User Delete Functionality in View Researcher/Manager Accessible to Admin, Researcher & Manager

	def deleteUser(self,user_id):
		conn = rdbms.connect(instance=_INSTANCE_NAME, database=dbname, user=usr, passwd=pss, charset='utf8')
		cursor = conn.cursor()
		sqlcmd = "update user set status=0 where user_id = %s "
		# print sqlcmd
		cursor.execute(sqlcmd,(user_id,))
		conn.commit()
		conn.close()    

	# Undo Delete Functionality available after deleting a user in View Researcher/Manager Accessible to Admin, Researcher & Manager

	def undoDeleteUser(self,user_id):
		conn = rdbms.connect(instance=_INSTANCE_NAME, database=dbname, user=usr, passwd=pss, charset='utf8')
		cursor = conn.cursor()
		sqlcmd = "update user set status=1 where user_id = %s "
		# print sqlcmd
		cursor.execute(sqlcmd,(user_id,))
		conn.commit()
		conn.close()   

	# Submit section in case of view surveys: sets the flag of correction table=0 for checked questions
	def checkInitSection(self,checked):
		conn = rdbms.connect(instance=_INSTANCE_NAME, database=dbname, user=usr, passwd=pss, charset='utf8')
		cursor = conn.cursor()
		sqlcmd = "INSERT INTO correction SELECT survey_data_id, survey_id, part_id, sect_id, ques_no, op_text, 0, 0 from survey_data where survey_data_id in "+str(checked.replace("[","(").replace("]",")"))
		print sqlcmd
		cursor.execute(sqlcmd)
		conn.commit()
		conn.close()  

	# Submit section in case of view surveys: deletes entry from correction table for unchecked questions
	def unCheckInitSection(self,unchecked):
		conn = rdbms.connect(instance=_INSTANCE_NAME, database=dbname, user=usr, passwd=pss, charset='utf8')
		cursor = conn.cursor()
		sqlcmd = "DELETE FROM correction where survey_data_id in "+str(unchecked.replace("[","(").replace("]",")"))
		print sqlcmd
		cursor.execute(sqlcmd)
		conn.commit()
		conn.close()  

	# Submit all the sections in case of view surveys: sets the flag of correction table=1 for all entries for that participant id
	def submitFlag(self,part_id):
		conn = rdbms.connect(instance=_INSTANCE_NAME, database=dbname, user=usr, passwd=pss, charset='utf8')
		cursor = conn.cursor()
		sqlcmd = "Update correction set flag = 1 where part_id = %s"
		print sqlcmd
		cursor.execute(sqlcmd,(part_id,))
		conn.commit()
		conn.close()  

	# Approve section in case of approve surveys: sets the corr_ststus_flag of correction table=1 for  checked questions marking them approved
	def approveSection(self,checked):
		conn = rdbms.connect(instance=_INSTANCE_NAME, database=dbname, user=usr, passwd=pss, charset='utf8')
		cursor = conn.cursor()
		sqlcmd = "Update correction set corr_status_flag=1 where survey_data_id in "+str(checked.replace("[","(").replace("]",")"))
		print sqlcmd
		cursor.execute(sqlcmd)
		conn.commit()
		conn.close()  

	# disapprove section in case of approve surveys: sets the corr_ststus_flag of correction table=0 for  checked questions marking them disapproved
	def disapproveSection(self,checked):
		conn = rdbms.connect(instance=_INSTANCE_NAME, database=dbname, user=usr, passwd=pss, charset='utf8')
		cursor = conn.cursor()
		sqlcmd = "Update correction set corr_status_flag=2 where survey_data_id in "+str(checked.replace("[","(").replace("]",")"))
		print sqlcmd
		cursor.execute(sqlcmd)
		conn.commit()
		conn.close()  
		   
class GetData():

	def getUserCountWithRole(self,role):
		conn = rdbms.connect(instance=_INSTANCE_NAME, database=dbname, user=usr, passwd=pss)
		cursor = conn.cursor()
		sqlcmd = "select count(*) from user where user_id like '%"+role+"%'"
		cursor.execute(sqlcmd)
		count = cursor.fetchall()[0][0]
		conn.close()
		return count

	def getSurveyData(self, survey_id, project_id, starting_count, ending_count):
		conn = rdbms.connect(instance = _INSTANCE_NAME, database= dbname, user= usr, passwd= pss)
		cursor = conn.cursor()
		sqlcmd = "call `innovaccer_jpal`.`survey_data_all_proc`('"+survey_id+"','"+project_id+"',"+starting_count+","+ending_count+")"
		cursor.execute(sqlcmd)
		rows = cursor.fetchall()
		conn.close()
		survey_data = []
		for row in rows:
			survey_data.append(row)
		return survey_data

	def getSurveyDetails(self):
		conn = rdbms.connect(instance=_INSTANCE_NAME, database = dbname, user=usr, passwd=pss)
		cursor = conn.cursor()
		sqlcmd = "SELECT * FROM survey_details;"
		cursor.execute(sqlcmd)
		rows = cursor.fetchall()
		conn.close()
		survey_details = []
		for row in rows:
			survey_details.append({"id":row[0],"name":row[1]})
		return survey_details
	
	def getProjectDetails(self):
		conn = rdbms.connect(instance= _INSTANCE_NAME, database= dbname, user=usr, passwd = pss)
		cursor = conn.cursor()
		sqlcmd = "SELECT * FROM project_table;"
		cursor.execute(sqlcmd)
		rows = cursor.fetchall()
		conn.close()
		project_details = []
		for row in rows:
			project_details.append({"id":row[0],"name":row[1]})
		return project_details


	def getUsername(self,first_name,last_name):
		conn = rdbms.connect(instance = _INSTANCE_NAME, database= dbname, user= usr, passwd= pss)
		cursor = conn.cursor()
		sqlcmd = "select count(*) from user where f_name='%s' and l_name = '%s'" % (first_name, last_name)
		cursor.execute(sqlcmd)
		count = cursor.fetchall()[0][0]
		conn.close()
		if count == 0:
			return first_name + "_" + last_name
		else: 
			return first_name + "_" + last_name + "_" + str(int(count))
	
	def getUserDetails(self, username):
		conn = rdbms.connect(instance= _INSTANCE_NAME, database = dbname, user = usr, passwd = pss)
		cursor = conn.cursor()
		sqlcmd = "select login_id,login_password,f_name,l_name,email,user_id,status from user where login_id = '%s'" % (username,)
		cursor.execute(sqlcmd)
		rows = cursor.fetchall()
		conn.close()
		return [{'login_id':row[0],"login_password":row[1],"f_name":row[2],"l_name":row[3],"email":row[4],"user_id":row[5],"status":row[6]} for row in rows]
 
	def getCorrections(self, survey_id):
		conn = rdbms.connect(instance= _INSTANCE_NAME, database = dbname, user = usr, passwd = pss)
		cursor = conn.cursor()
		sqlcmd = "select * from correction where survey_id='%s'" % (survey_id,)
		cursor.execute(sqlcmd)
		rows = cursor.fetchall()
		conn.close()
		return [{'survey_data_id':row[0],'survey_id':row[1],'part_id':row[2],'sect_id':row[3],'ques_id':row[4],"ans":row[5],"flag":row[6],"corr_status":row[7]} for row in rows]




	# Authorize user login and password
	def checkUserAuth(self,user_id,password):
		conn = rdbms.connect(instance=_INSTANCE_NAME, database=dbname, user=usr, passwd=pss, charset='utf8')
		cursor = conn.cursor()
		sqlcmd = "select * from user where login_id = %s and login_password = %s and status=1"
		# print sqlcmd
		cursor.execute(sqlcmd,(user_id, password,))
		info = []
		for row in cursor.fetchall():
			info=row[0]
		conn.close()
		return info


	# Fetch profile of a particular user id
	def getProfile(self,user_id):
		conn = rdbms.connect(instance=_INSTANCE_NAME, database=dbname, user=usr, passwd=pss, charset='utf8')
		cursor = conn.cursor()
		sqlcmd = """select user_id as ID, f_name as fname, l_name as lname, email, primary_phone as phone, secondary_phone as altphone, 
				r.role_desc as accounttype, address, line_1 as street, city, state, country, DOB
				from user left join role r on r.role_id=user.role where user_id= %s"""
		cursor.execute(sqlcmd,(user_id,))
		user=[]
		for row in cursor.fetchall():
			user={
					'ID': row[0],
					'fName': row[1].encode('utf-8'),
					'lName': row[2].encode('utf-8'),
					'Email': row[3].encode('utf-8'),
					'Phone': row[4],
					'altphone': row[5],
					'accountType': row[6],
					'HouseNumber': row[7].encode('utf-8'),
					'Street': row[8].encode('utf-8'),
					'City': row[9].encode('utf-8'),
					'State': row[10].encode('utf-8'),
					'Country': row[11].encode('utf-8'),
					'DOB': row[12]
				}
		conn.close()
		return user

	# Role-Functionality fetch query for the construction of menu at the time of login
	def getRoleFunctionality(self,user_id):
		conn = rdbms.connect(instance=_INSTANCE_NAME, database=dbname, user=usr, passwd=pss, charset='utf8')
		cursor = conn.cursor()
		sqlcmd = """select f.profile_name, f.url, f.icon from functionality f 
				left join user u on u.user_id = %s
				left join role_functionality rf  on u.role=rf.role
				where rf.functionality = f.id"""
		cursor.execute(sqlcmd,(user_id,))
		info = []
		data=[]
		for row in cursor.fetchall():
			info={
					'name': row[0],
					'url': row[1],
					'icon': row[2]
				}
			data.append(info)
		conn.close()
		return data


	# Get all researchers for view researcher option, available to admin
	def getResearchers(self):
		conn = rdbms.connect(instance=_INSTANCE_NAME, database=dbname, user=usr, passwd=pss, charset='utf8')
		cursor = conn.cursor()
		sqlcmd = "select f_name, l_name , email, city, user_id, age from user where role='RE' and status=1"
		cursor.execute(sqlcmd)
		info = []
		data=[]
		for row in cursor.fetchall():
			info={
					'Name': row[0]+" "+row[1],
					'Email': row[2],
					'Location': row[3],
					'ID': row[4],
					'Age':row[5]
				}
			data.append(info)
		return_data = {'researchers' : data}
		conn.close()
		return return_data

	# Query for survey table for a particular DE
	def getDeSurveys(self,user_id):
		conn = rdbms.connect(instance=_INSTANCE_NAME, database=dbname, user=usr, passwd=pss, charset='utf8')
		cursor = conn.cursor()
		sqlcmd = """SELECT sda.survey_id, sde.survey_name, CONCAT(u.f_name,' ',u.l_name) as surveyor_name,  sda.part_id, u.company, CONCAT(u.city,',',u.state) as location, sda.timestamp, ds.de_id from survey_data sda
					join de_surveyor ds on ds.surveyor_id=SUBSTR(sda.part_id,length(sda.survey_id)+1,length(ds.surveyor_id))
					join survey_details sde on sde.survey_id=sda.survey_id
					join user u on u.user_id=SUBSTR(sda.part_id,length(sda.survey_id)+1,length(ds.surveyor_id))
					where ds.de_id= %s 
					and part_id not in (select part_id from correction where flag=1) and sda.survey_data_id in (select max(survey_data_id) from survey_data sd where sda.part_id=sd.part_id and sd.sect_id=sda.sect_id and sd.ques_no=sda.ques_no) 
					group by sda.part_id
					"""
		cursor.execute(sqlcmd,(user_id,))
		info = []
		user=[]
		for row in cursor.fetchall():
			info={
					'ID': row[0],
					'name': row[1],
					'surveyorName': row[2],
					'pID': row[3],
					'company': row[4],
					'location': row[5],
					'date': row[6],
					'deID': row[7]
				}
			user.append(info)
		conn.close()
		return user
	

	# Query for unique sections for section navigation box in view surveys
	def getSurveySections(self,user_id):
		conn = rdbms.connect(instance=_INSTANCE_NAME, database=dbname, user=usr, passwd=pss, charset='utf8')
		cursor = conn.cursor()
		sqlcmd = """ SELECT sda.sect_id,sec.sect_name FROM survey_data sda
					join section_details sec on sec.sect_id=sda.sect_id
					 where part_id = %s group by sda.sect_id"""
		cursor.execute(sqlcmd,(user_id,))
		info = []
		user=[]
		for row in cursor.fetchall():
			info={
					'sect_id': row[0],
					'sect_text': row[1]
				}
			user.append(info)
		conn.close()
		return user

	# Query for all questions and answers from survey data for given part_id and sect_id
	def getSectionQuest(self,user_id,sect_id):
		conn = rdbms.connect(instance=_INSTANCE_NAME, database=dbname, user=usr, passwd=pss, charset='utf8')
		cursor = conn.cursor()
		sqlcmd = """SELECT sda.sect_id, qde.sect_text, sda.ques_no, qde.ques_text,sda.op_id, sda.op_text as ans_text, corr.flag,sda.survey_data_id FROM survey_data sda
			left join ques_details qde on qde.q_no=sda.ques_no
			left join correction corr on corr.survey_data_id = sda.survey_data_id
			where qde.survey_id=sda.survey_id and sda.part_id= %s and sda.sect_id= %s 
			and sda.survey_data_id in (select max(survey_data_id) from survey_data sd where sda.part_id=sd.part_id and sd.sect_id=sda.sect_id and sd.ques_no=sda.ques_no)
			"""
		cursor.execute(sqlcmd,(user_id, sect_id,))
		info = []
		user=[]
		for row in cursor.fetchall():
			print row
			info={
					'ques_no': row[2].encode('utf-8'),
					'ques_text': row[3].encode('utf-8'),
					'op_id': row[4],
					'ans_text': row[5].encode('utf-8'),
					'flag': row[6],
					'sda_id':row[7]
				}
			user.append(info)
		conn.close()
		return user

	# Query for approval table
	def getVerifySurveys(self,user_id):
		conn = rdbms.connect(instance=_INSTANCE_NAME, database=dbname, user=usr, passwd=pss, charset='utf8')
		cursor = conn.cursor()
		sqlcmd = """SELECT corr.survey_id, sde.survey_name, CONCAT(u.f_name,' ',u.l_name) as surveyor_name,  corr.part_id, u.company, CONCAT(u.city,',',u.state) as location, sda.timestamp, ds.de_id from correction corr 
					join survey_data sda on sda.survey_data_id=corr.survey_data_id 
					join de_surveyor ds on ds.surveyor_id=SUBSTR(sda.part_id,length(sda.survey_id)+1,length(ds.surveyor_id))
					join survey_details sde on sde.survey_id=corr.survey_id
					join user u on u.user_id=SUBSTR(sda.part_id,length(sda.survey_id)+1,length(ds.surveyor_id))
					where ds.de_id= %s
					and sda.correction_flag=1 and corr.flag!=0 
					and ((corr.corr_status_flag=2 and corr.survey_data_id<sda.survey_data_id and sda.survey_data_id in (select max(survey_data_id) from survey_data sd where sda.part_id=sd.part_id and sd.sect_id=sda.sect_id and sd.ques_no=sda.ques_no)) or corr.corr_status_flag=0) 
					group by sda.part_id
				"""

		# print sqlcmd
		cursor.execute(sqlcmd,(user_id,))
		info = []
		user=[]
		for row in cursor.fetchall():
			info={
					'ID': row[0],
					'name': row[1],
					'surveyorName': row[2],
					'pID': row[3],
					'company': row[4],
					'location': row[5],
					'date': row[6],
					'deID': row[7]
				}
			user.append(info)
		conn.close()
		return user
	
	# Query for extracting sections containing flagged questions
	def getFlaggedSections(self,user_id):
		conn = rdbms.connect(instance=_INSTANCE_NAME, database=dbname, user=usr, passwd=pss, charset='utf8')
		cursor = conn.cursor()
		sqlcmd = """ SELECT sda.sect_id,sec.sect_name FROM survey_data sda
				join section_details sec on sec.sect_id=sda.sect_id
				join correction corr on corr.survey_data_id=sda.survey_data_id
				 where sda.part_id = %s 
				 and corr.flag=1 group by sda.sect_id;
				"""
		cursor.execute(sqlcmd,(user_id,))
		info = []
		user=[]
		for row in cursor.fetchall():
			info={
					'sect_id': row[0],
					'sect_text': row[1]
				}
			user.append(info)
		conn.close()
		return user
	
	# Query for extracting flagged questions of a particular section during approval	
	def getFlaggedQuest(self,user_id,sect_id):
		conn = rdbms.connect(instance=_INSTANCE_NAME, database=dbname, user=usr, passwd=pss, charset='utf8')
		cursor = conn.cursor()
		sqlcmd = """SELECT sda.sect_id, qde.sect_text, sda.ques_no, qde.ques_text,sda.op_id, sda.op_text as ans_text, corr.flag,sda.survey_data_id FROM survey_data sda
			left join ques_details qde on qde.q_no=sda.ques_no
			left join correction corr on corr.survey_data_id = sda.survey_data_id
			where qde.survey_id=sda.survey_id and sda.part_id= %s and sda.sect_id= %s and corr.flag=1 
			and sda.survey_data_id in (select max(survey_data_id) from survey_data sd where sda.part_id=sd.part_id and sd.sect_id=sda.sect_id and sd.ques_no=sda.ques_no)

			"""
		cursor.execute(sqlcmd,(user_id, sect_id,))
		info = []
		user=[]
		for row in cursor.fetchall():
			print row
			info={
					'ques_no': row[2],
					'ques_text': row[3],
					'op_id': row[4],
					'ans_text': row[5],
					'flag': row[6],
					'sda_id':row[7]
				}
			user.append(info)
		conn.close()
		return user
  
		