import mysql.connector
import dbconfig as cfg
class DepartmentDAO:
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
        
    def create(self, department):
        db = self.getConnection()
        cursor = db.cursor()
        sql="insert into departments (dept_no,dept_name) VALUES (%s,%s)"
        values = [
            department['dept_no'],
            department['dept_name']    
        ]
        cursor.execute(sql, values)
        self.db.commit()
        db.close()
        return cursor.lastrowid


    def getAll(self):
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
       return returnArray

    def findByNo(self, dept_no):
       db = self.getConnection()
       cursor = db.cursor()
       sql="select * from departments where dept_no = %s"
       values = [dept_no]
       cursor.execute(sql, values)
       result = cursor.fetchone()
       db.close()
       return self.convertToDict(result)


    def update(self, department):
       db = self.getConnection()
       cursor = db.cursor()
       sql="update departments set dept_name= %s where dept_no = %s"
       print(sql)
       values =[
             department['dept_name'],
             department['dept_no']
             
           ]
       cursor.execute(sql, values)
       self.db.commit()
       db.close()
       return department

    
    def delete(self, emp_no):
       db = self.getConnection()
       cursor = db.cursor()
       sql="delete from departments where dept_no = %s"
       values = (emp_no,)
       cursor.execute(sql, values)
       db.close()
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
