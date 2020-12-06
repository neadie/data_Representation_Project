import mysql.connector
import dbconfig as cfg
class EmployeeDept:
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
            if err.errno == mysql.connector.errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == mysql.connector.errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
               print(err)
            
        return db

    def getConnection(self):
        try:
           db = mysql.connector.connect(
              pool_name='my_connection_pool'
            )
        except mysql.connector.Error as err:
            if err.errno == mysql.connector.errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == mysql.connector.errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
               print(err)
        return db

    def __init__(self):
        try:
            db=self.initConnectToDB()
            db.close()
        except mysql.connector.Error as err:
            if err.errno == mysql.connector.errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == mysql.connector.errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
               print(err)
        
   


    def getAll(self):
        try:
          db = self.getConnection()
          cursor = db.cursor()
          sql="select CONCAT(employees.first_name, employees.last_name) AS employeeName, departments.dept_name from employees inner join departments using(dept_no)"
          cursor.execute(sql)
          results = cursor.fetchall()
          returnArray = []
          for result in results:
             resultAsDict = self.convertToDict(result)
             returnArray.append(resultAsDict)
          cursor.close()
          db.close()
        except mysql.connector.Error as err:
            if err.errno == mysql.connector.errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == mysql.connector.errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
               print(err)
        return returnArray

    def findByNo(self, emp_no):
        try:
            db = self.getConnection()
            cursor = db.cursor()
            sql = 'select CONCAT(employees.first_name, employees.last_name) AS employeeName, departments.dept_name from employees inner join departments using(dept_no) where employees.emp_no = %s'
            values = [ emp_no ]
            cursor.execute(sql, values)
            result = cursor.fetchone()
            cursor.close()
            db.close()
        except mysql.connector.Error as err:
            if err.errno == mysql.connector.errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == mysql.connector.errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
               print(err)
        return self.convertToDict(result)


   


    def convertToDict(self, result):
        colnames = ['employeeName','dept_name']
        employeeDept = {}

        if result:
            for i , colName in enumerate(colnames):
                value = result[i]
                employeeDept[colName] = value
        return employeeDept   
employeeDept = EmployeeDept()
