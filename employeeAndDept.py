import mysql.connector
import dbconfig as cfg
class EmployeeDept:
    def initConnectToDB(self):
        db = mysql.connector.connect(
            host=       cfg.mysql['host'],
            user=       cfg.mysql['user'],
            password=   cfg.mysql['password'],
            database=   cfg.mysql['database'],
            pool_name='my_connection_pool',
            pool_size=10
        )
        return db

    def getConnection(self):
        db = mysql.connector.connect(
            pool_name='my_connection_pool'
        )
        return db

    def __init__(self): 
        db=self.initConnectToDB()
        db.close()
   


    def getAll(self):
       db = self.getConnection()
       cursor = db.cursor()
       sql="select CONCAT(employees.first_name, employees.last_name) AS employeeName, departments.dept_name from employees inner join departments using(dept_no)"
       cursor.execute(sql)
       results = cursor.fetchall()
       returnArray = []
       for result in results:
            resultAsDict = self.convertToDict(result)
            returnArray.append(resultAsDict)
       db.close()
       return returnArray

    def findByNo(self, emp_no):
        db = self.getConnection()
        cursor = db.cursor()
        sql = 'select CONCAT(employees.first_name, employees.last_name) AS employeeName, departments.dept_name from employees inner join departments using(dept_no) where employees.emp_no = %s'
        values = [ emp_no ]
        cursor.execute(sql, values)
        result = cursor.fetchone()
        db.close()
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
