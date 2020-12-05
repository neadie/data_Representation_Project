import mysql.connector
import dbconfig as cfg
class EmployeeDAO:
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

    def create(self, employee):
        db = self.getConnection()
        cursor = db.cursor()
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
        db.close()
        return cursor.lastrowid


    def getAll(self):
       db = self.getConnection()
       cursor = db.cursor()
       sql="SELECT emp_no,employees.first_name,employees.last_name,employees.dept_no,employees.birth_date,employees.hire_date FROM employees"
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
        sql = 'select * from employees where emp_no = %s'
        values = [ emp_no ]
        cursor.execute(sql, values)
        result = cursor.fetchone()
        db.close()
        return self.convertToDict(result)


    def update(self, employee):
       db = self.getConnection()
       cursor = db.cursor()
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
       db.close()
       return employee

    
    def delete(self, emp_no):
        db = self.getConnection()
        cursor = db.cursor()
        sql="delete from employees where emp_no = %s"
        values = (emp_no,)
        cursor.execute(sql, values)
        db.close()
        self.db.commit()


    def convertToDict(self, result):
        colnames = ['emp_no','first_name', 'last_name','dept_no','birth_date', 'hire_date']
        employee = {}

        if result:
            for i , colName in enumerate(colnames):
                value = result[i]
                employee[colName] = value
        return employee   
employeeDAO = EmployeeDAO()
