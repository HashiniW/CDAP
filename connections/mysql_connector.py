import json
from pprint import pprint
import pymysql


class Mysql_Connection:
        
    def conenction(self):
        #db conenction
        try:
            
            # cnx = pymysql.connect(host="localhost", user='root',passwd="", database='cfd')
            cnx = pymysql.connect(host="localhost", user='root',passwd="Shalitha@123", database='cfd')
            
            return  cnx
        except:
            return 'connection error'   
       
        

