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

_INSTANCE_NAME = 'jpal-survey-app:web-database'
# _INSTANCE_NAME = 'localhost' 
dbname = 'innovaccer_jpal'
usr='root'
pss='root'

#########################


class PostData():
	
	# A good testiminy of how to keep variable/function names - Courtesy Dhruv

	# def view_data(self,query,values):
	# 	conn = rdbms.connect(instance=_INSTANCE_NAME, database=dbname, user=usr, passwd=pss)
	# 	cursor = conn.cursor()
	# 	sqlcmd = query
	# 	cursor.execute(sqlcmd,values)
	# 	conn.commit()
	# 	conn.close() 


	def view_data(self,query,values):
		try:
			conn = rdbms.connect(instance=_INSTANCE_NAME, database=dbname, user=usr, passwd=pss)
			cursor = conn.cursor()
			sqlcmd = query
			cursor.execute(sqlcmd,values)
			conn.commit()
			conn.close()
			return "200"
		except BaseException,err:
			print err
			return "500"

	def addUser(self, username, first_name, last_name, email, role):
		conn = rdbms.connect(instance= _INSTANCE_NAME, database= dbname, user=usr, passwd= pss)
		cursor = conn.cursor()
		user_id = role + str(int(GetData().getUserCountWithRole(role))+ 1)
		login_id = username
		login_password = first_name
		status = 1
		password_flag = 0
		sqlcmd = "insert into user(user_id, f_name, l_name,email,login_id,login_password,role, status, password_flag) values('%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (user_id, first_name,last_name,email,login_id,login_password,role,status, password_flag)
		cursor.execute(sqlcmd)
		conn.commit()
		conn.close()
		return user_id

	def addProject(self,UpID, project):
		conn = rdbms.connect(instance= _INSTANCE_NAME, database= dbname, user=usr, passwd= pss)
		cursor = conn.cursor()
		p_id = "P" + str(int(GetData().getProjectCount())+ 1)
		sqlcmd = "insert into project_table (id, title, user_generated_id) values('%s','%s','%s')" % (p_id, project,UpID)
		cursor.execute(sqlcmd)
		conn.commit()
		conn.close()

	def deletePMmap(self, pm_id):
		conn = rdbms.connect(instance= _INSTANCE_NAME, database= dbname, user=usr, passwd= pss)
		cursor = conn.cursor()
		sqlcmd = "delete from project_user where user_id = %s"
		cursor.execute(sqlcmd,(pm_id,))
		conn.commit()
		conn.close()

	def addProjectUser(self, project_id, user_id, role):
		conn = rdbms.connect(instance= _INSTANCE_NAME, database= dbname, user=usr, passwd= pss)
		cursor = conn.cursor()
		sqlcmd = "insert into project_user values (%s,%s,%s)"
		cursor.execute(sqlcmd,(project_id, user_id, role))
		conn.commit()
		conn.close()
		

	def delDeSuMap(self, de_id, su_id):
		conn = rdbms.connect(instance= _INSTANCE_NAME, database= dbname, user=usr, passwd= pss)
		cursor = conn.cursor()
		sqlcmd = "delete from de_surveyor where de_id = %s and surveyor_id = %s"
		cursor.execute(sqlcmd,(de_id,su_id))
		conn.commit()
		conn.close()


	# def addSurveyData(self, bulk_data):
	# 	try:
	# 		conn = rdbms.connect(instance= _INSTANCE_NAME, database= dbname, user=usr, passwd= pss)
	# 		cursor = conn.cursor()
	# 		sqlcmd = 'insert into survey_data(survey_id, part_id, sect_id, ques_no, op_id, op_text, view_type, lang_id) values (%s,%s,%s,%s,%s,%s,%s,%s)'
	# 		cursor.executemany(sqlcmd, bulk_data)
	# 		conn.commit()
	# 		conn.close()
	# 		return "200"
	# 	except BaseException,er:
	# 		return er

	def addSurveyData(self, bulk_data):
		try:
			conn = rdbms.connect(instance= _INSTANCE_NAME, database= dbname, user=usr, passwd= pss)
			cursor = conn.cursor()
			sqlcmd = 'insert into survey_data (survey_id, part_id, sect_id, ques_no, op_id, op_text, view_type,lang_id,timestamp,correction_flag,survey_data_id) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
			cursor.executemany(sqlcmd, bulk_data)
			conn.commit()
			conn.close()
			return "200"
		except BaseException,err:
			print err
			return "500"



	def changePwd(self,u_id,pwd):
		conn = rdbms.connect(instance=_INSTANCE_NAME, database=dbname, user=usr, passwd=pss, charset='utf8')
		cursor = conn.cursor()
		sqlcmd = "update user set login_password = %s where user_id = %s"
		cursor.execute(sqlcmd,(pwd,u_id,))
		conn.commit()
		conn.close() 


	# Function for updation of profile data through the profile page

	def saveProfileData(self,post_data):
		conn = rdbms.connect(instance=_INSTANCE_NAME, database=dbname, user=usr, passwd=pss, charset='utf8')
		cursor = conn.cursor()
		sqlcmd = "update user set f_name = %s , l_name = %s , primary_phone = %s, address = %s, line_1 = %s , city = %s ,state = %s, country = %s where user_id = %s "
		cursor.execute(sqlcmd,(post_data['f_name'],post_data['l_name'],post_data['primary_phone'],post_data['address'],post_data['line_1'],post_data['city'],post_data['state'],post_data['country'],post_data['user_id'],))
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
		sqlcmd = "INSERT INTO correction SELECT id, survey_id, part_id, sect_id, ques_no, op_id, op_text, view_type, timestamp, 0, 0, lang_id from survey_data where id in "+str(checked.replace("[","(").replace("]",")"))+" and id not in (select id from correction where (flag=1 or flag=0) and (corr_status_flag=0 or corr_status_flag=2))"
		print sqlcmd
		cursor.execute(sqlcmd)
		conn.commit()
		conn.close()  

	# Submit section in case of view surveys: deletes entry from correction table for unchecked questions
	def unCheckInitSection(self,unchecked):
		conn = rdbms.connect(instance=_INSTANCE_NAME, database=dbname, user=usr, passwd=pss, charset='utf8')
		cursor = conn.cursor()
		sqlcmd = "DELETE FROM correction where id in "+str(unchecked.replace("[","(").replace("]",")"))
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
		sqlcmd = "Update correction set corr_status_flag=1 where id in "+str(checked.replace("[","(").replace("]",")"))
		print sqlcmd
		cursor.execute(sqlcmd)
		conn.commit()
		conn.close()  

	# disapprove section in case of approve surveys: sets the corr_ststus_flag of correction table=0 for  checked questions marking them disapproved
	def disapproveSection(self,checked):
		conn = rdbms.connect(instance=_INSTANCE_NAME, database=dbname, user=usr, passwd=pss, charset='utf8')
		cursor = conn.cursor()
		sqlcmd = "Update correction set corr_status_flag=2 where id in "+str(checked.replace("[","(").replace("]",")"))
		print sqlcmd
		cursor.execute(sqlcmd)
		conn.commit()
		conn.close()  
		   
	

	def addDESurveyor(self,pmid, deId, suId):
		conn = rdbms.connect(instance=_INSTANCE_NAME, database=dbname, user=usr, passwd=pss)
		cursor = conn.cursor()

		p_id = GetData().getProjectId(pmid)
		print pmid, p_id
		sqlcmd = 'Insert into de_surveyor(p_id, de_id, surveyor_id) values("%s", "%s", "%s")' %(p_id, deId, suId)
		cursor.execute(sqlcmd)
		conn.commit()
		conn.close()

class GetData():

	def getAllRecords(self, survey_id, project_id, query):

		conn = rdbms.connect(instance = _INSTANCE_NAME, database= dbname, user= usr, passwd= pss)
		cursor = conn.cursor()
		sqlcmd = "call `innovaccer_jpal`.`all_records`('"+survey_id+"','"+project_id+"','"+query+"')"
		print sqlcmd
		cursor.execute(sqlcmd)
		rows = cursor.fetchall()
		conn.close()
		survey_data = []
		for row in rows:
			survey_data.append(row)
		return survey_data


	def getAllQuestionsAndIds(self,survey_id):
		conn = rdbms.connect(instance=_INSTANCE_NAME, database=dbname, user=usr, passwd=pss)
		cursor = conn.cursor()
		sqlcmd = "select ques_short_text from ques_details where survey_id='%s' and q_no not in ('X5', 'end') and q_no not like 'sect%%' order by prim_key" % (survey_id)
		print sqlcmd
		cursor.execute(sqlcmd)
		rows = cursor.fetchall()
		conn.commit()
		conn.close()
		final_list=[]
		for row in rows:
			final_list.append(row[0])
		return final_list

	# def getOptions(self,survey_id):
	# 	conn = rdbms.connect(instance=_INSTANCE_NAME, database=dbname, user=usr, passwd=pss)
	# 	cursor = conn.cursor()
	# 	sqlcmd = "select ques_no,op_id,op_text from options where survey_id='%s'" %(survey_id,)
	# 	cursor.execute(sqlcmd)
	# 	rows = cursor.fetchall()
	# 	conn.commit()
	# 	conn.close()
	# 	return rows

	def getOptions(self,survey_id):
		conn = rdbms.connect(instance=_INSTANCE_NAME, database=dbname, user=usr, passwd=pss)
		cursor = conn.cursor()
		sqlcmd = "select ques_no,op_id,op_value,feature from options where survey_id='%s'" % (survey_id,)
		cursor.execute(sqlcmd)
		rows = cursor.fetchall()
		conn.commit()
		conn.close()
		finalRows = []
		for row in rows:
			finalRows.append(row)
		return finalRows


	def getUserCountWithRole(self,role):
		conn = rdbms.connect(instance=_INSTANCE_NAME, database=dbname, user=usr, passwd=pss)
		cursor = conn.cursor()
		sqlcmd = "select MAX(substr(user_id,3,7)) from user where role = '"+role+"'"
		cursor.execute(sqlcmd)
		count = cursor.fetchall()[0][0]
		conn.close()
		return count


	def getFunctionalities(self,user_id):
		conn = rdbms.connect(instance=_INSTANCE_NAME, database=dbname, user=usr, passwd=pss, charset='utf8')
		cursor = conn.cursor()
		sqlcmd = """select f.url from functionality f 
					inner join role_functionality rf on rf.functionality=f.id 
					inner join user u on u.role=rf.role where user_id= %s"""
		cursor.execute(sqlcmd,(user_id,))
		
		data=[]
		for row in cursor.fetchall():
			data.append(row[0])
		conn.close()
		return data


	def getProjectCount(self):
		conn = rdbms.connect(instance=_INSTANCE_NAME, database=dbname, user=usr, passwd=pss)
		cursor = conn.cursor()
		sqlcmd = "select MAX(substr(id,2,5)) from project_table"
		cursor.execute(sqlcmd)
		count = cursor.fetchall()[0][0]
		conn.close()
		return count
	
	def checkPID(self,p_id):
		conn = rdbms.connect(instance = _INSTANCE_NAME, database= dbname, user= usr, passwd= pss)
		cursor = conn.cursor()
		sqlcmd = "select count(*) from project_table where user_generated_id='%s'" % (p_id)
		cursor.execute(sqlcmd)
		count = cursor.fetchall()[0][0]
		conn.close()
		return count
	# def getSurveyData(self, survey_id, project_id, starting_count, ending_count):
	# 	conn = rdbms.connect(instance = _INSTANCE_NAME, database= dbname, user= usr, passwd= pss,charset='utf8')
	# 	cursor = conn.cursor()
	# 	sqlcmd = "call `innovaccer_jpal`.`survey_data_all_proc`('"+survey_id+"','"+project_id+"',"+starting_count+","+ending_count+")"
	# 	cursor.execute(sqlcmd)
	# 	rows = cursor.fetchall()
	# 	conn.close()
	# 	survey_data = []
	# 	for row in rows:
	# 		survey_data.append(row)
	# 	return survey_data

	def getSurveyData(self,starting_count,ending_count):
		conn = rdbms.connect(instance = _INSTANCE_NAME, database= dbname, user= usr, passwd= pss)
		cursor = conn.cursor()
		sqlcmd = "select part_id,lang_id,X1,X2,X3,X4,1A,1B,2,3A,3B,3C,4A,4B,5A,5B,6A,6B,6C,6D,6E,6F,7A,7B,7C,7D,7E,8,`8-TB`,9,10,11a,11b,11c,11d,11e,11f,11g,11h,11i,`11i-TB`,12,13,`13-TB`,14,15,16,`16-TB`,17,18a,18iia,18b,18iib,18c,18iic,18d,18iid,18e,18iie,19,20,21,22,23a,23b,23c,23d,23e,24,25,26,`26-TB`,27,`27-TB`,28a,28b,28c,28d,28e,28f,29a,29b,29c,29d,29e,29f,30a,30b,30c,30d,30e,30f,30g,31,32,33,`33-TB`,34,`34-TB`,35,36,37,38,39,40,41,42,43,Z1,`Z1-TB`,Z2A,Z2B,Z2C,Z2D,Z2E,Z2F from view_data_table limit "+starting_count+","+ending_count
		cursor.execute(sqlcmd)
		rows = cursor.fetchall()
		conn.close()
		final_rows = []
		for row in rows:
			row = list(row)
			for i in range(len(row)):
				if row[i]=='blank: ' or row[i]== 'date: ':
					row[i]=''
				row[i]=str(row[i]).strip(': ')
			final_rows.append(row)
		return final_rows

	def getLoginDet(self,uid,utype):
		conn = rdbms.connect(instance = _INSTANCE_NAME, database= dbname, user= usr, passwd= pss)
		cursor = conn.cursor()
		print uid, utype
		if utype=='user_id':
			sqlcmd = """select login_id,login_password,user_id, f_name,l_name from user where user_id = %s"""
		else:
			sqlcmd = """select login_id,login_password,user_id, f_name,l_name from user where login_id = %s"""
			
		cursor.execute(sqlcmd,(uid,))
		rows = cursor.fetchall()
		u=[]
		final_rows = {}
		for row in rows:
			final_rows['login_id']=row[0]
			final_rows['password']=row[1]
			final_rows['device_id']=row[2]
			final_rows['f_name']=row[3]
			final_rows['l_name']=row[4]
		conn.close()
		u.append(final_rows)
		return u


	def getAllSurveyData(self):
		conn = rdbms.connect(instance = _INSTANCE_NAME, database= dbname, user= usr, passwd= pss)
		cursor = conn.cursor()
		sqlcmd = "select * from view_data_table"
		cursor.execute(sqlcmd)
		rows = cursor.fetchall()
		conn.close()
		final_rows = []
		for row in rows:
			final_rows.append(list(row))
		return final_rows

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

	def getEmail(self,user_id):
		conn = rdbms.connect(instance = _INSTANCE_NAME, database= dbname, user= usr, passwd= pss)
		cursor = conn.cursor()
		sqlcmd = "select email from user where user_id = '%s'" % (user_id)
		cursor.execute(sqlcmd)
		email = cursor.fetchall()[0][0]
		conn.close()
		return email
	
	def getUserDetails(self, username):
		conn = rdbms.connect(instance= _INSTANCE_NAME, database = dbname, user = usr, passwd = pss)
		cursor = conn.cursor()
		sqlcmd = "select login_id,login_password,f_name,l_name,email,user_id,status from user where login_id = '%s'" % (username,)
		cursor.execute(sqlcmd)
		rows = cursor.fetchall()
		conn.close()
		return [{'login_id':row[0],"login_password":row[1],"f_name":row[2],"l_name":row[3],"email":row[4],"user_id":row[5],"status":row[6]} for row in rows]
 
	def getPwd(self, u_id):
		conn = rdbms.connect(instance= _INSTANCE_NAME, database = dbname, user = usr, passwd = pss)
		cursor = conn.cursor()
		sqlcmd = "select login_password from user where user_id = '%s'" % (u_id,)
		cursor.execute(sqlcmd)
		rows = cursor.fetchall()
		conn.close()
		for r in rows:
			p=r[0]
		return p

	def getloginPwd(self, u_id):
		conn = rdbms.connect(instance= _INSTANCE_NAME, database = dbname, user = usr, passwd = pss)
		cursor = conn.cursor()
		sqlcmd = "select login_password from user where login_id = '%s'" % (u_id,)
		cursor.execute(sqlcmd)
		rows = cursor.fetchall()
		conn.close()
		p=''
		for r in rows:
			p=r[0]
		return p


	def getCorrections(self, survey_id):
		conn = rdbms.connect(instance= _INSTANCE_NAME, database = dbname, user = usr, passwd = pss)
		cursor = conn.cursor()
		sqlcmd = "select * from correction where survey_id='%s'" % (survey_id,)
		cursor.execute(sqlcmd)
		rows = cursor.fetchall()
		conn.close()
		return [{'id':row[0],'survey_id':row[1],'part_id':row[2],'sect_id':row[3],'ques_id':row[4],"ans":row[5],"flag":row[6],"corr_status":row[7]} for row in rows]

	def getAllDE(self,p_id):
		conn = rdbms.connect(instance=_INSTANCE_NAME, database=dbname, user=usr, passwd=pss)
		cursor = conn.cursor()
		sqlcmd = "SELECT user_id FROM project_user where project_id = %s and user_id like 'DE%%'"
		# print sqlcmd
		deList = []
		cursor.execute(sqlcmd,(p_id,))
		for row in cursor.fetchall():
			deList.append(row[0])
		return deList


	def getNameUser(self, listUserId):
		# To return a directory of userId : userName(First Name + Last Name) for a given list of User Ids.
		conn = rdbms.connect(instance=_INSTANCE_NAME, database=dbname, user=usr, passwd=pss)
		cursor = conn.cursor()
		sqlcmd = "SELECT user_id, CONCAT(f_name, ' ', l_name) FROM user where user_id in ('" + "','".join(listUserId) + "')"
		# cursor.execute(sqlcmd,(userStr,))
		cursor.execute(sqlcmd)
		# user_dict = []
		user_dict = {}	#  Dictionary to hold User Id and Name Mapping
		for row in cursor.fetchall():
			user_dict[row[0]] = row[1]

		return user_dict

	def getDESuMap(self, deList):
		# Select query to return the mapping between Data Editor and Surveyor based on the Project Manager ID.
		conn = rdbms.connect(instance=_INSTANCE_NAME, database=dbname, user=usr, passwd=pss)
		cursor = conn.cursor()
		sqlcmd = "SELECT ds.de_id, ds.surveyor_id FROM de_surveyor ds where ds.de_id in ('" + "','".join(deList) + "')"
		print sqlcmd
		cursor.execute(sqlcmd)
		de_su_map = {}	#To store Data editor Surveyor Mapping under the concerned Project Manager
		# user_list = []	# To store list of DE and Surveyors under the PM
		for row in cursor.fetchall():
			de = row[0].strip()
			su = row[1].strip()
			if de in de_su_map.keys():
				# If Data Editor already exists in the dictionary
				de_su_map[de].append(su)
			else:
				# If Data Editor doesn't exist in the dictionary
				de_su_map[de] = [su]

		return de_su_map
		   
	def getUnassSurveyor(self, pm_id):
		# To return a directory of userId : userName(First Name + Last Name) of all Unassigned Surveyors for a given Project Manager's Id.
		conn = rdbms.connect(instance=_INSTANCE_NAME, database=dbname, user=usr, passwd=pss)
		cursor = conn.cursor()
		sqlcmd = """select pu.user_id, CONCAT(u.f_name, ' ', u.l_name) from project_user pu, user u 
					where pu.user_id = u.user_id
						and pu.project_id = (select pu1.project_id from project_user pu1 where pu1.user_id = '%s')
						and pu.user_id like 'SU%%'
    					and pu.user_id not in (select ds.surveyor_id 
												from de_surveyor ds 
												where ds.p_id = (select pu1.project_id 
																	from project_user pu1 
																		where pu1.user_id = '%s'))""" %(pm_id,pm_id)
		# print sqlcmd
		cursor.execute(sqlcmd)
		unass_surveyors_list = []
		unass_surveyors_dict = {}	#  Dictionary to hold User Id and Name Mapping
		for row in cursor.fetchall():
			unass_surveyors_dict['name'] = row[1]
			unass_surveyors_dict['ID'] = row[0]
			unass_surveyors_dict_temp = {}
			for k in unass_surveyors_dict.keys():
				unass_surveyors_dict_temp[k] = unass_surveyors_dict[k]

			unass_surveyors_list.append(unass_surveyors_dict_temp)
		return unass_surveyors_list


	# Authorize user login and password
	def checkUserAuth(self,user_id,password):
		conn = rdbms.connect(instance=_INSTANCE_NAME, database=dbname, user=usr, passwd=pss, charset='utf8')
		cursor = conn.cursor()
		sqlcmd = "select * from user where login_id = %s and login_password = %s and status=1 and role!='SU'"
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

	def getAllSections(self):
		conn = rdbms.connect(instance=_INSTANCE_NAME, database=dbname, user=usr, passwd=pss, charset='utf8')
		cursor = conn.cursor()
		sqlcmd = "Select sect_id, sect_name from section_details"
		cursor.execute(sqlcmd)
		info = {}
		
		for row in cursor.fetchall():
			info[row[1].lower()]=row[0]	
		
		conn.close()
		return info




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

	def getAllQuestions(self, survey_id):
		conn = rdbms.connect(instance=_INSTANCE_NAME, database=dbname, user=usr, passwd=pss)
		cursor = conn.cursor()
		sqlcmd = "select ques_short_text from ques_details where survey_id='%s'" % (survey_id)
		cursor.execute(sqlcmd)
		rows = cursor.fetchall()
		conn.commit()
		conn.close()
		return rows
	# Query for survey table for a particular DE
	def getDeSurveys(self,user_id):
		conn = rdbms.connect(instance=_INSTANCE_NAME, database=dbname, user=usr, passwd=pss, charset='utf8')
		cursor = conn.cursor()
		sqlcmd = """SELECT sda.survey_id, sde.survey_name, CONCAT(u.f_name,' ',u.l_name) as surveyor_name,  sda.part_id, u.company, CONCAT(u.city,',',u.state) as location, sda.timestamp, ds.de_id from survey_data sda,de_surveyor ds, survey_details sde,user u where
 ds.surveyor_id=SUBSTR(sda.part_id,length(sda.survey_id)+1,length(ds.surveyor_id))
and sde.survey_id=sda.survey_id
and u.user_id=SUBSTR(sda.part_id,length(sda.survey_id)+1,length(ds.surveyor_id))
and ds.de_id= %s
and part_id not in (select part_id from correction where flag=1) and sda.id in (select max(id) from survey_data sd where sda.part_id=sd.part_id and sd.sect_id=sda.sect_id and sd.ques_no=sda.ques_no) 
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
					'date': str(row[6]),
					'deID': row[7]
				}
			user.append(info)
			# print user
		conn.close()
		return user
	

	# Query for unique sections for section navigation box in view surveys
	def getSurveySections(self,user_id):
		conn = rdbms.connect(instance=_INSTANCE_NAME, database=dbname, user=usr, passwd=pss, charset='utf8')
		cursor = conn.cursor()
		sqlcmd = """ SELECT sda.sect_id,sec.sect_name FROM survey_data sda
					join section_details sec on sec.sect_id=sda.sect_id
					 where part_id = %s and sda.sect_id!='GRO01_1' group by sda.sect_id"""
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
		sqlcmd = """SELECT sda.sect_id, qde.sect_text, sda.ques_no, qde.ques_text,sda.op_id, sda.op_text as ans_text, corr.flag,sda.id FROM survey_data sda
			left join ques_details qde on qde.q_no=sda.ques_no
			left join correction corr on corr.id = sda.id
			where qde.survey_id=sda.survey_id and sda.part_id= %s and sda.sect_id= %s 
			and sda.id in (select max(id) from survey_data sd where sda.part_id=sd.part_id and sd.sect_id=sda.sect_id and sd.ques_no=sda.ques_no)
			
			"""
			# and (sda.ques_no not like 'sec%' or sda.ques_no not like 'igno%')
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
					join survey_data sda on sda.id>corr.id
					join de_surveyor ds on ds.surveyor_id=SUBSTR(sda.part_id,length(sda.survey_id)+1,length(ds.surveyor_id))
					join survey_details sde on sde.survey_id=corr.survey_id
					join user u on u.user_id=SUBSTR(sda.part_id,length(sda.survey_id)+1,length(ds.surveyor_id))
					where ds.de_id= %s
					and sda.correction_flag=1 and corr.flag!=0 
					and corr.corr_status_flag=0
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
					'date': str(row[6]),
					'deID': row[7]
				}
			user.append(info)
		conn.close()
		return user
	def getCorrectionsSur(self, surveyor_id, last_index):
		conn = rdbms.connect(instance = _INSTANCE_NAME, database= dbname, user= usr, passwd= pss)
		cursor = conn.cursor()
		sqlcmd = """SELECT * FROM innovaccer_jpal.correction 
					where SUBSTR(part_id,length(survey_id)+1,length(%s))=%s and id>%s and flag=1 and (corr_status_flag=2 or corr_status_flag=0);"""
			
		cursor.execute(sqlcmd,(surveyor_id,surveyor_id,last_index))
		rows = cursor.fetchall()
		surveys=[]

		# final_rows = {}
		for row in rows:
			final_rows = {}
			final_rows['flag']=row[9]
			final_rows['corr_status_flag']=row[10]
			final_rows['ID']=row[0]
			final_rows['survey_id']=row[1]
			final_rows['part_id']=row[2]
			final_rows['sect_id']=row[3]
			final_rows['ques_no']=row[4]
			final_rows['op_value']=row[5]
			final_rows['ans']=row[6]
			final_rows['view_type']=row[7]
			final_rows['language']=row[11]
			surveys.append(final_rows)
		conn.close()
		
		return surveys





	# Query for extracting sections containing flagged questions
	def getFlaggedSections(self,user_id):
		conn = rdbms.connect(instance=_INSTANCE_NAME, database=dbname, user=usr, passwd=pss, charset='utf8')
		cursor = conn.cursor()
		sqlcmd = """ SELECT sda.sect_id,sec.sect_name FROM survey_data sda
				join section_details sec on sec.sect_id=sda.sect_id
				join correction corr on corr.id=sda.id
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
		sqlcmd = """SELECT sda.sect_id, qde.sect_text, sda.ques_no, qde.ques_text,sda.op_id, sda.op_text as ans_text, corr.flag,sda.id FROM survey_data sda
			left join ques_details qde on qde.q_no=sda.ques_no
			left join correction corr on corr.id = sda.id
			where qde.survey_id=sda.survey_id and sda.part_id= %s and sda.sect_id= %s and corr.flag=1 
			and sda.id in (select max(id) from survey_data sd where sda.part_id=sd.part_id and sd.sect_id=sda.sect_id and sd.ques_no=sda.ques_no)

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

	def getProjectId(self, user_id):
		conn = rdbms.connect(instance=_INSTANCE_NAME, database=dbname, user=usr, passwd=pss)
		cursor = conn.cursor()
		sqlcmd = "SELECT project_id FROM project_user where user_id = %s"
		# print sqlcmd
		cursor.execute(sqlcmd,(user_id,))
		return cursor.fetchall()[0][0]

	def getManagerProjects(self):
		conn = rdbms.connect(instance=_INSTANCE_NAME, database=dbname, user=usr, passwd=pss, charset='utf8')
		cursor = conn.cursor()
		sqlcmd = """SELECT pu.user_id, CONCAT(u.f_name,' ',u.l_name) as manager_name, pu.project_id, pt.title from project_user pu
					left join user u on pu.user_id=u.user_id
					left join project_table pt on pt.id=pu.project_id
					where pu.role_id='PM'
					group by pu.project_id
				"""
		cursor.execute(sqlcmd)
		info = []
		user=[]
		for row in cursor.fetchall():
			print row
			info={
					'ID': row[0],
					'Name': row[1],
					'project_id': row[2],
					'Project': row[3]
				}
			user.append(info)
		conn.close()
		return user

	def getUnassProjects(self):
		conn = rdbms.connect(instance=_INSTANCE_NAME, database=dbname, user=usr, passwd=pss, charset='utf8')
		cursor = conn.cursor()
		sqlcmd = "Select id, title,user_generated_id from project_table where id not in (select project_id from project_user where 1)"
		cursor.execute(sqlcmd)
		info = []
		user=[]
		for row in cursor.fetchall():
			print row
			info={
					'ID': row[0],
					'Name': row[1],
					'UserKey':row[2]
					}
			user.append(info)
		conn.close()
		return user