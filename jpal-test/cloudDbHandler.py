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
        sqlcmd = "select * from user where login_id = %s and login_password = %s"
        # print sqlcmd
        cursor.execute(sqlcmd,(user_id, password))
        info = []
        for row in cursor.fetchall():
            info=row[0]
        conn.close()
        return info

    def getResearchers(self):
        conn = rdbms.connect(instance=_INSTANCE_NAME, database=dbname, user=usr, passwd=pss)
        cursor = conn.cursor()
        sqlcmd = "select f_name, l_name , email, city from user where role='RE'"
        # print sqlcmd
        cursor.execute(sqlcmd)
        info = []
        data=[]
        for row in cursor.fetchall():
            info={
                    'Name': row[0]+" "+row[1],
                    'Email': row[2],
                    'Location': row[3]
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
        cursor.execute(sqlcmd,(user_id))
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
    
    
    def getProfile(self,user_id):
        conn = rdbms.connect(instance=_INSTANCE_NAME, database=dbname, user=usr, passwd=pss)
        cursor = conn.cursor()
        sqlcmd = """select user_id as ID, f_name as fname, l_name as lname, email, primary_phone as phone, secondary_phone as altphone, 
                r.role_desc as accounttype, address, line_1 as street, city, state, country, DOB
                from user left join role r on r.role_id=user.role where user_id= %s"""

        # print sqlcmd
        cursor.execute(sqlcmd,(user_id))
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
    
    
   
        