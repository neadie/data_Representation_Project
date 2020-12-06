import mysql.connector
import dbconfig as cfg
class DepartmentDAO:
    def initConnectToDB(self):
        try:
            db = mysql.connector.connect(
              host=       cfg.mysql['host'],
              user=       cfg.mysql['user'],
              password=   cfg.mysql['password'],
              database=   cfg.mysql['database'],
              pool_name='my_connection_pool',
              pool_size=10
          )
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
               print(err)
        return db

    def getConnection(self):
        db = mysql.connector.connect(
            pool_name='my_connection_pool'
        )
        return db

    def __init__(self):
        try:
            db=self.initConnectToDB()
            db.close()
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
               print(err)
        
        
        
        
    def create(self, department):
        try:
            db = self.getConnection()
            cursor = db.cursor()
            sql="insert into departments (dept_no,dept_name) VALUES (%s,%s)"
            values = [ department['dept_no'],department['dept_name'] ]
            cursor.execute(sql, values)
            self.db.commit()
            db.close()
        except mysql.connector.Error as err:
                if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                    print("Something is wrong with your user name or password")
                elif err.errno == errorcode.ER_BAD_DB_ERROR:
                    print("Database does not exist")
                else:
                  print(err)
        return cursor.lastrowid


    def getAll(self):
        try:
            db = self.getConnection()
            cursor = db.cursor()
            sql="select * from departments"
            cursor.execute(sql)
            results = cursor.fetchall()
            returnArray = []
            for result in results:
                resultAsDict = self.convertToDict(result)
                returnArray.append(resultAsDict)
            db.close()
        except mysql.connector.Error as err:
           if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
               print("Something is wrong with your user name or password")
           elif err.errno == errorcode.ER_BAD_DB_ERROR:
               print("Database does not exist")
           else:
               print(err)
        return returnArray

    def findByNo(self, dept_no):
        try:
            db = self.getConnection()
            cursor = db.cursor()
            sql="select * from departments where dept_no = %s"
            values = [dept_no]
            cursor.execute(sql, values)
            result = cursor.fetchone()
            db.close()
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
        return self.convertToDict(result)


    def update(self, department):
        try:
            db = self.getConnection()
            cursor = db.cursor()
            sql="update departments set dept_name= %s where dept_no = %s"
            print(sql)
            values =[ department['dept_name'], department['dept_no'] ]
            cursor.execute(sql, values)
            self.db.commit()
            db.close()
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
              print(err)
        return department

    
    def delete(self, emp_no):
        try:
            db = self.getConnection()
            cursor = db.cursor()
            sql="delete from departments where dept_no = %s"
            values = (emp_no,)
            cursor.execute(sql, values)
            db.commit()
            db.close()
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
              print(err)
         
            

    def convertToDict(self, result):
        colnames = ['dept_no','dept_name']
        department = {}

        if result:
            for i , colName in enumerate(colnames):
                value = result[i]
                department[colName] = value
        return department
       
departmentDAO = DepartmentDAO()
