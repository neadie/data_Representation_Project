from sqlconnect import session,Departments

class DepartmentDAO:
    
        
    def create(self, department):
            dept = Departments(dept_no=department['dept_no'],dept_name = department['dept_name'])
            session.add(dept)
            session.commit()
            


    def getAll(self):
            results = session.query(Departments).all()
            returnArray = []
            for result in results:
                resultAsDict = self.to_dict(result)
                returnArray.append(resultAsDict)
            
            return returnArray

    def findByNo(self, dept_no):
            results = session.query(Departments).filter(Departments.dept_no==dept_no).all()
            for result in results:
                dept = self.to_dict(result)
            return dept


    def update(self, department):
            session.query(Departments).filter(Departments.dept_no == department['dept_no']).update({Departments.dept_name:department['dept_name']}, synchronize_session = False)
            session.commit()
            return department

    
    def delete(self, emp_no):
            session.query(Departments).filter(Departments.dept_no==emp_no).delete()
            session.commit()
    
        
            

       
       
       
    def to_dict(self,row):
         return {column.name: getattr(row, row.__mapper__.get_property_by_column(column).key) for column in row.__table__.columns}

departmentDAO = DepartmentDAO()
