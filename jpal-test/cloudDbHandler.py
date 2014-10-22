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
class AddData():
    
    
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

    def getRoleFunctionality(self,user_id):
        conn = rdbms.connect(instance=_INSTANCE_NAME, database=dbname, user=usr, passwd=pss)
        cursor = conn.cursor()
        sqlcmd = """select f.profile_name, f.url, f.icon from functionality f 
                left join user u on u.user_id = %s
                left join role_functionality rf  on u.role=rf.role
                where rf.functionality = f.id"""
        print sqlcmd
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

        nav = {'navs' : data}
        conn.close()
        return json.loads(nav)
    
    
   
        