import mysql.connector
import dbconfig as cfg


class Singleton:

    def __init__(self, cls):
        self._cls = cls

    def Instance(self):
        try:
            return self._instance
        except AttributeError:
            self._instance = self._cls()
            return self._instance

    def __call__(self):
        raise TypeError('Singletons must be accessed through `Instance()`.')

    def __instancecheck__(self, inst):
        return isinstance(inst, self._cls)

@Singleton     
class DBConnection(object) :
 
    def getConnection(self):
          if self.conn == None:
               self.conn= mysql.connector.connect(pool_name='my_connection_pool')
          return self.conn
         
    
    def __init__(self):
        self.conn = mysql.connector.connect(
            host=       cfg.mysql['host'],
            user=       cfg.mysql['user'],
            password=   cfg.mysql['password'],
            database=   cfg.mysql['database'],
            pool_name='my_connection_pool',
            pool_size=10
        )

    def __del__(self):
        if self.conn != None:
            self.conn.close()

   
       

        
        
        


dbconnection = DBConnection.Instance()

