import mysql.connector
import dbconfig as cfg
class EmployeeDAO:
    db=""
    def connectToDB(self):
        self.db = mysql.connector.connect(
            host=       cfg.mysql['host'],
            user=       cfg.mysql['user'],
            password=   cfg.mysql['password'],
            database=   cfg.mysql['database']
        )
    def __init__(self): 
        self.connectToDB()
     
    
    def getCursor(self):
        if not self.db.is_connected():
            self.connectToDB()
        return self.db.cursor()
    

    def create(self, employee):
            cursor = self.getCursor()
            sql = "insert into employees (first_name, last_name, dept_no,birth_date, hire_date) values (%s,%s,%s,%s,%s)"
            values = [
  
              employee['first_name'],
              employee['last_name'],
              employee['dept_no'],
              employee['birth_date'],
              employee['hire_date']
           ]
            cursor.execute(sql, values)
            self.db.commit()
            lastRowId=cursor.lastrowid
            cursor.close()
            return lastRowId
      
            


    def getAll(self):
            cursor = self.getCursor()
            sql="SELECT emp_no,employees.first_name,employees.last_name,employees.dept_no,employees.birth_date,employees.hire_date FROM employees"
            cursor.execute(sql)
            results = cursor.fetchall()
            returnArray = []
            for result in results:
              resultAsDict = self.convertToDict(result)
              returnArray.append(resultAsDict)
            cursor.close()  
            return returnArray

    def findByNo(self, emp_no):
            cursor = self.getCursor()
            sql = 'select * from employees where emp_no = %s'
            values = [ emp_no ]
            cursor.execute(sql, values)
            result = cursor.fetchone()
            emp = self.convertToDict(result)
            cursor.close()
            return emp


    def update(self, employee):

            cursor = self.getCursor()
            sql = "update employees set first_name = %s, last_name = %s,dept_no = %s, birth_date=%s, hire_date=%s where emp_no = %s"
            values = [
            
              employee['first_name'],
              employee['last_name'],
              employee['dept_no'],
              employee['birth_date'],
              employee['hire_date'],
              employee['emp_no']
           ]
            cursor.execute(sql, values)
            self.db.commit()
            cursor.close()
            return employee

    
    def delete(self, emp_no):
        
            cursor = self.getCursor()
            sql="delete from employees where emp_no = %s"
            values = (emp_no,)
            cursor.execute(sql, values)
            self.db.commit()
            cursor.close()
  
        


    def convertToDict(self, result):
        colnames = ['emp_no','first_name', 'last_name','dept_no','birth_date', 'hire_date']
        employee = {}

        if result:
            for i , colName in enumerate(colnames):
                value = result[i]
                employee[colName] = value
        return employee   



   

employeeDAO = EmployeeDAO()
