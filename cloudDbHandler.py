import StringIO
import webapp2
import jinja2
import cgi
import json
import ast
import datetime
import os
from google.appengine.api import rdbms

_INSTANCE_NAME = 'localhost' 
dbname = 'innovaccer_jpal'
usr='root'
pss='root'

class PostData():
	
	def saveProfileData(self,post_data):
		conn = rdbms.connect(instance=_INSTANCE_NAME, database=dbname, user=usr, passwd=pss)
		cursor = conn.cursor()
		sqlcmd = "update user set f_name = %s , l_name = %s , DOB = %s ,primary_phone = %s, address = %s, line_1 = %s , city = %s ,state = %s, country = %s where user_id = %s "
		# print sqlcmd
		cursor.execute(sqlcmd,(post_data['f_name'],post_data['l_name'],post_data['DOB'],post_data['primary_phone'],post_data['address'],post_data['line_1'],post_data['city'],post_data['state'],post_data['country'],post_data['user_id'],))
		conn.commit()
		conn.close() 

	def deleteUser(self,user_id):
		conn = rdbms.connect(instance=_INSTANCE_NAME, database=dbname, user=usr, passwd=pss)
		cursor = conn.cursor()
		sqlcmd = "update user set status=0 where user_id = %s "
		# print sqlcmd
		cursor.execute(sqlcmd,(user_id,))
		conn.commit()
		conn.close()    

	def undoDeleteUser(self,user_id):
		conn = rdbms.connect(instance=_INSTANCE_NAME, database=dbname, user=usr, passwd=pss)
		cursor = conn.cursor()
		sqlcmd = "update user set status=1 where user_id = %s "
		# print sqlcmd
		cursor.execute(sqlcmd,(user_id,))
		conn.commit()
		conn.close()   

	def addListDetails(self,listname,list_type,status):
		try:
			conn = rdbms.connect(instance=_INSTANCE_NAME, database=dbname)
			cursor = conn.cursor()
			cursor.execute('insert into sendListDetails (listname,list_type,list_status) values (%s,%s,%s)',(listname,list_type,status))
			conn.commit()
			listid = cursor.lastrowid
			conn.close()
			return listid
		except Exception,e:
			print str(e)
			return False 
	
	
	def addLogs(self,user_id,action,objct,time,status):
		try:
			
			conn = rdbms.connect(instance=_INSTANCE_NAME, database=dbname)
			cursor = conn.cursor()
			cursor.execute('insert into log_details (user_id,action,object,time,status) values (%s,%s,%s,%s,%s)',(user_id,action,objct,'active'))
			conn.commit()
			testid = cursor.lastrowid
			conn.close()
			return testid
		except:
			return False

	def checkInitSection(self,checked):
		conn = rdbms.connect(instance=_INSTANCE_NAME, database=dbname, user=usr, passwd=pss)
		cursor = conn.cursor()
		sqlcmd = "INSERT INTO correction SELECT survey_data_id, survey_id, part_id, sect_id, ques_no, op_text, 0, null from survey_data where survey_data_id in "+str(checked.replace("[","(").replace("]",")"))
		print sqlcmd
		cursor.execute(sqlcmd)
		conn.commit()
		conn.close()  

	def unCheckInitSection(self,unchecked):
		conn = rdbms.connect(instance=_INSTANCE_NAME, database=dbname, user=usr, passwd=pss)
		cursor = conn.cursor()
		sqlcmd = "DELETE FROM correction where survey_data_id in "+str(unchecked.replace("[","(").replace("]",")"))
		print sqlcmd
		cursor.execute(sqlcmd)
		conn.commit()
		conn.close()  
	
	def submitFlag(self,part_id):
		conn = rdbms.connect(instance=_INSTANCE_NAME, database=dbname, user=usr, passwd=pss)
		cursor = conn.cursor()
		sqlcmd = "Update correction set flag = 1 where part_id = %s"
		print sqlcmd
		cursor.execute(sqlcmd,(part_id,))
		conn.commit()
		conn.close()  

		   
class updateData():
	
	def updateGuestTestStatus(self,uid,testid,status):
		conn = rdbms.connect(instance=_INSTANCE_NAME, database=dbname)
		cursor = conn.cursor()
		sqlcmd = " update score_details set status = '%s' where user_id = '%s' and test_id = '%s'"%(status,uid,testid)
		cursor.execute(sqlcmd)
		conn.commit()
		conn.close()        
		
			   
class GetData():
	
	
	def checkUserAuth(self,user_id,password):
		conn = rdbms.connect(instance=_INSTANCE_NAME, database=dbname, user=usr, passwd=pss)
		cursor = conn.cursor()
		sqlcmd = "select * from user where login_id = %s and login_password = %s and status=1"
		# print sqlcmd
		cursor.execute(sqlcmd,(user_id, password,))
		info = []
		for row in cursor.fetchall():
			info=row[0]
		conn.close()
		return info

	def getResearchers(self):
		conn = rdbms.connect(instance=_INSTANCE_NAME, database=dbname, user=usr, passwd=pss)
		cursor = conn.cursor()
		sqlcmd = "select f_name, l_name , email, city, user_id, age from user where role='RE' and status=1"
		# print sqlcmd
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



	def getRoleFunctionality(self,user_id):
		conn = rdbms.connect(instance=_INSTANCE_NAME, database=dbname, user=usr, passwd=pss)
		cursor = conn.cursor()
		sqlcmd = """select f.profile_name, f.url, f.icon from functionality f 
				left join user u on u.user_id = %s
				left join role_functionality rf  on u.role=rf.role
				where rf.functionality = f.id"""
		# print sqlcmd
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

		# return_data = {'navs' : data, 'user': user}
		conn.close()
		return data



	def getDeSurveys(self,user_id):
		conn = rdbms.connect(instance=_INSTANCE_NAME, database=dbname, user=usr, passwd=pss)
		cursor = conn.cursor()
		sqlcmd = """SELECT sda.survey_id, sde.survey_name, CONCAT(u.f_name,' ',u.l_name) as surveyor_name,  sda.part_id, u.company, CONCAT(u.city,',',u.state) as location, sda.timestamp, ds.de_id from survey_data sda
					join de_surveyor ds on ds.surveyor_id=SUBSTRING( sda.part_id,length(sda.survey_id)+1 ,length(sda.part_id)-locate('EN',sda.part_id)+1)
					join survey_details sde on sde.survey_id=sda.survey_id
					join user u on u.user_id=SUBSTRING( sda.part_id,length(sda.survey_id)+1 ,length(sda.part_id)-locate('EN',sda.part_id)+1)
					where ds.de_id= %s 
					and part_id not in (select part_id from correction where flag=1) 
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
	
	def getProfile(self,user_id):
		conn = rdbms.connect(instance=_INSTANCE_NAME, database=dbname, user=usr, passwd=pss)
		cursor = conn.cursor()
		sqlcmd = """select user_id as ID, f_name as fname, l_name as lname, email, primary_phone as phone, secondary_phone as altphone, 
				r.role_desc as accounttype, address, line_1 as street, city, state, country, DOB
				from user left join role r on r.role_id=user.role where user_id= %s"""

		# print sqlcmd
		cursor.execute(sqlcmd,(user_id,))
		# info = []
		user=[]
		for row in cursor.fetchall():
			user={
					'ID': row[0],
					'fName': row[1],
					'lName': row[2],
					'Email': row[3],
					'Phone': row[4],
					'altphone': row[5],
					'accountType': row[6],
					'HouseNumber': row[7],
					'Street': row[8],
					'City': row[9],
					'State': row[10],
					'Country': row[11],
					'DOB': row[12]
				}
			# user.append(info)
		conn.close()
		return user

	def getSurveySections(self,user_id):
		conn = rdbms.connect(instance=_INSTANCE_NAME, database=dbname, user=usr, passwd=pss)
		cursor = conn.cursor()
		sqlcmd = """ SELECT sda.sect_id,sec.sect_name FROM survey_data sda
					join section_details sec on sec.sect_id=sda.sect_id
					 where part_id = %s group by sda.sect_id"""

		# print sqlcmd
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


	def getSectionQuest(self,user_id,sect_id):
		conn = rdbms.connect(instance=_INSTANCE_NAME, database=dbname, user=usr, passwd=pss)
		cursor = conn.cursor()
		sqlcmd = """SELECT sda.sect_id, qde.sect_text, sda.ques_no, qde.ques_text,sda.op_id, sda.op_text as ans_text, corr.flag,sda.survey_data_id FROM survey_data sda
			left join ques_details qde on qde.q_no=sda.ques_no
			left join correction corr on corr.survey_data_id = sda.survey_data_id
			where qde.survey_id=sda.survey_id and sda.part_id= %s and sda.sect_id= %s """

		# print sqlcmd
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

	def getVerifySurveys(self,user_id):
		conn = rdbms.connect(instance=_INSTANCE_NAME, database=dbname, user=usr, passwd=pss)
		cursor = conn.cursor()
		sqlcmd = """SELECT corr.survey_id, sde.survey_name, CONCAT(u.f_name,' ',u.l_name) as surveyor_name,  corr.part_id, u.company, CONCAT(u.city,',',u.state) as location, sda.timestamp, ds.de_id from correction corr 
					join survey_data sda on sda.survey_data_id=corr.survey_data_id 
					join de_surveyor ds on ds.surveyor_id=SUBSTRING( corr.part_id,length(corr.survey_id)+1 ,length(corr.part_id)-locate('EN',corr.part_id)+1)
					join survey_details sde on sde.survey_id=corr.survey_id
					join user u on u.user_id=SUBSTRING( corr.part_id,length(corr.survey_id)+1 ,length(corr.part_id)-locate('EN',corr.part_id)+1)
					where ds.de_id= %s
					and sda.correction_flag=1 and corr.flag!=0
					group by sda.part_id;
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
	

	def getFlaggedSections(self,user_id):
		conn = rdbms.connect(instance=_INSTANCE_NAME, database=dbname, user=usr, passwd=pss)
		cursor = conn.cursor()
		sqlcmd = """ SELECT sda.sect_id,sec.sect_name FROM survey_data sda
				join section_details sec on sec.sect_id=sda.sect_id
				join correction corr on corr.survey_data_id=sda.survey_data_id
				 where sda.part_id = %s 
				 and corr.flag=1 group by sda.sect_id;
				"""

		# print sqlcmd
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
	
	
 	def getFlaggedQuest(self,user_id,sect_id):
		conn = rdbms.connect(instance=_INSTANCE_NAME, database=dbname, user=usr, passwd=pss)
		cursor = conn.cursor()
		sqlcmd = """SELECT sda.sect_id, qde.sect_text, sda.ques_no, qde.ques_text,sda.op_id, sda.op_text as ans_text, corr.flag,sda.survey_data_id FROM survey_data sda
			left join ques_details qde on qde.q_no=sda.ques_no
			left join correction corr on corr.survey_data_id = sda.survey_data_id
			where qde.survey_id=sda.survey_id and sda.part_id= %s and sda.sect_id= %s and corr.flag=1
			"""

		# print sqlcmd
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
  
		