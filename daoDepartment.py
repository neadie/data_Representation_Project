import mysql.connector
import dbconfig as cfg
class DepartmentDAO:
    db = ""
        
        
        
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
        
    def create(self, department):
            cursor = self.getCursor()
            sql="insert into departments (dept_no,dept_name) VALUES (%s,%s)"
            values = [ department['dept_no'],department['dept_name'] ]
            cursor.execute(sql, values)
            self.db.commit()
            lastRowId=cursor.lastrowid
            cursor.close()
            return lastRowId


    def getAll(self):
      
            
            cursor = self.getCursor()
            sql="select * from departments"
            cursor.execute(sql)
            results = cursor.fetchall()
            returnArray = []
            for result in results:
                resultAsDict = self.convertToDict(result)
                returnArray.append(resultAsDict)
            cursor.close()
            return returnArray

    def findByNo(self, dept_no):
            cursor = self.getCursor()
            sql="select * from departments where dept_no = %s"
            values = [dept_no]
            cursor.execute(sql, values)
            result = cursor.fetchone()
            dept = self.convertToDict(result)
            cursor.close()
            return dept


    def update(self, department):
            cursor = self.getCursor()
            sql="update departments set dept_name= %s where dept_no = %s"
            print(sql)
            values =[ department['dept_name'], department['dept_no'] ]
            cursor.execute(sql, values)
            self.db.commit()
            cursor.close()
            return department

    
    def delete(self, emp_no):
            cursor = self.getCursor()
            sql="delete from departments where dept_no = %s"
            values = (emp_no,)
            cursor.execute(sql, values)
            self.db.commit()
           
   
    
    def __del__(self):
       self.db.close()     
            

    def convertToDict(self, result):
        colnames = ['dept_no','dept_name']
        department = {}

        if result:
            for i , colName in enumerate(colnames):
                value = result[i]
                department[colName] = value
        return department
       
departmentDAO = DepartmentDAO()
