import mysql.connector
import dbconfig as cfg
        
class DBConnection :
 
    
   __instance = None
  
   
   @staticmethod 
   def getInstance():
      """ Static access method. """
      if DBConnection.__instance == None:
         DBConnection()
      return DBConnection.__instance


   @staticmethod
   def getConnection():
     
            db = mysql.connector.connect(
            pool_name='my_connection_pool'
        )
     
            return db
    
   def __init__(self):
      """ Virtually private constructor. """
      if DBConnection.__instance != None:
         raise Exception("This class is a singleton!")
      else:
         DBConnection.__instance = self
         db=DBConnection.initConnectToDB()
         db.close()
       
   @staticmethod     
   def initConnectToDB():
        db = mysql.connector.connect(
            host=       cfg.mysql['host'],
            user=       cfg.mysql['user'],
            password=   cfg.mysql['password'],
            database=   cfg.mysql['database'],
            pool_name='my_connection_pool',
            pool_size=10
        )
        return db



dbconnection = DBConnection.getInstance()

