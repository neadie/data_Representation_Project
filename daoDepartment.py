import mysql.connector
class DepartmentDAO:
    db=""
    def __init__(self):
        self.db = mysql.connector.connect(host="localhost",user="root",password="",database="data_representation_project")

    def create(self, department):
        cursor = self.db.cursor()
        sql="insert into departments (dept_no,dept_name) VALUES (%s,%s)"
        values = [
            department['dept_no'],
            department['dept_name']    
        ]
        cursor.execute(sql, values)
        self.db.commit()
        return cursor.lastrowid


    def getAll(self):
       cursor = self.db.cursor()
       sql="select * from departments"
       cursor.execute(sql)
       results = cursor.fetchall()
       returnArray = []
       for result in results:
            resultAsDict = self.convertToDict(result)
            returnArray.append(resultAsDict)
       return returnArray

    def findByNo(self, dept_no):
       cursor = self.db.cursor()
       sql="select * from departments where dept_no = %s"
       values = [dept_no]
       cursor.execute(sql, values)
       result = cursor.fetchone()
       return self.convertToDict(result)


    def update(self, department):
       print(department)
       cursor = self.db.cursor()
       sql="update departments set dept_name= %s where dept_no = %s"
       print(sql)
       values =[
             department['dept_name'],
             department['dept_no']
             
           ]
       cursor.execute(sql, values)
       self.db.commit()
       return department

    
    def delete(self, emp_no):
       cursor = self.db.cursor()
       sql="delete from departments where dept_no = %s"
       values = (emp_no,)
       cursor.execute(sql, values)
       self.db.commit()

    def convertToDict(self, result):
        colnames = ['dept_no','dept_name']
        department = {}

        if result:
            for i , colName in enumerate(colnames):
                value = result[i]
                department[colName] = value
        return department
       
departmentDAO = DepartmentDAO()
