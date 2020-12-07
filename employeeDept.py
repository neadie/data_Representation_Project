import mysql.connector
import dbconfig as cfg
class EmployeeDept:


   def __init__(self):
        pass


    def getAll(self):
       
            db = dbconnection.getConnection()
            cursor = db.cursor()
            sql="select CONCAT(employees.first_name, employees.last_name) AS employeeName, departments.dept_name from employees inner join departments using(dept_no)"
            cursor.execute(sql)
            results = cursor.fetchall()
            returnArray = []
            for result in results:
               resultAsDict = self.convertToDict(result)
               returnArray.append(resultAsDict)
           
        
       return returnArray

    def findByNo(self, emp_no):
    
            db = dbconnection.getConnection()
            cursor = db.cursor()
            sql = 'select CONCAT(employees.first_name, employees.last_name) AS employeeName, departments.dept_name from employees inner join departments using(dept_no) where employees.emp_no = %s'
            values = [ emp_no ]
            cursor.execute(sql, values)
            result = cursor.fetchone()
       
        return self.convertToDict(result)


   


    def convertToDict(self, result):
        colnames = ['employeeName','dept_name']
        employee = {}

        if result:
            for i , colName in enumerate(colnames):
                value = result[i]
                employee[colName] = value
        return employee   
employeeDept = EmployeeDept()
