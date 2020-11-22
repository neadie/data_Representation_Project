import mysql.connector
class EmployeeDAO:
    db=""
    def __init__(self):
        self.db = mysql.connector.connect(host="localhost",user="root",password="",database="data_representation_project")

   

    def create(self, employee):
        cursor = self.db.cursor()
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
        return cursor.lastrowid


    def getAll(self):
       cursor = self.db.cursor()
       sql="SELECT emp_no,employees.first_name,employees.last_name,employees.dept_no,employees.birth_date,employees.hire_date FROM employees"
       cursor.execute(sql)
       results = cursor.fetchall()
       returnArray = []
       for result in results:
            resultAsDict = self.convertToDict(result)
            returnArray.append(resultAsDict)
       return returnArray

    def findByNo(self, emp_no):
        cursor = self.db.cursor()
        sql = 'select * from employees where emp_no = %s'
        values = [ emp_no ]
        cursor.execute(sql, values)
        result = cursor.fetchone()
        return self.convertToDict(result)


    def update(self, employee):
       cursor = self.db.cursor()
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
       return employee

    
    def delete(self, emp_no):
       cursor = self.db.cursor()
       sql="delete from employees where emp_no = %s"
       values = (emp_no,)
       cursor.execute(sql, values)
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
