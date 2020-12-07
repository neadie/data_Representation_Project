import mysql.connector
from dbconnect import dbconnection
class DepartmentDAO:
    db = dbconnection.getConnection()
        
        
        
    def __init__(self):
        pass
        
    def create(self, department):
        
            
            cursor = DepartmentDAO.db.cursor()
            sql="insert into departments (dept_no,dept_name) VALUES (%s,%s)"
            values = [ department['dept_no'],department['dept_name'] ]
            cursor.execute(sql, values)
            self.db.commit()
            return cursor.lastrowid


    def getAll(self):
      
            
            cursor = DepartmentDAO.db.cursor()
            sql="select * from departments"
            cursor.execute(sql)
            results = cursor.fetchall()
            returnArray = []
            for result in results:
                resultAsDict = self.convertToDict(result)
                returnArray.append(resultAsDict)
            
      
            return returnArray

    def findByNo(self, dept_no):
            cursor = DepartmentDAO.db.cursor()
            sql="select * from departments where dept_no = %s"
            values = [dept_no]
            cursor.execute(sql, values)
            result = cursor.fetchone()
            return self.convertToDict(result)


    def update(self, department):
            cursor = DepartmentDAO.db.cursor()
            sql="update departments set dept_name= %s where dept_no = %s"
            print(sql)
            values =[ department['dept_name'], department['dept_no'] ]
            cursor.execute(sql, values)
            db.commit()
      
            return department

    
    def delete(self, emp_no):
            cursor = DepartmentDAO.db.cursor()
            sql="delete from departments where dept_no = %s"
            values = (emp_no,)
            cursor.execute(sql, values)
            db.commit()
           
   
    
    def __del__(self):
       db.close()     
            

    def convertToDict(self, result):
        colnames = ['dept_no','dept_name']
        department = {}

        if result:
            for i , colName in enumerate(colnames):
                value = result[i]
                department[colName] = value
        return department
       
departmentDAO = DepartmentDAO()
