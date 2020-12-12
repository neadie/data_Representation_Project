from sqlconnect import session,Employees

class EmployeeDAO:
    

    def create(self, employee):
            emp = Employees(first_name=employee['first_name'],last_name = employee['last_name'],dept_no=employee['dept_no'],birth_date=employee['birth_date'],hire_date=employee['hire_date'])
            session.add(emp)
            session.commit()
          
           
            


    def getAll(self):
            results = session.query(Employees).all()
            returnArray = []
            for result in results:
                resultAsDict = self.to_dict(result)
                returnArray.append(resultAsDict)
            
            return returnArray

    def findByNo(self, emp_no):
            results = session.query(Employees).filter(Employees.emp_no==emp_no).all()
            for result in results:
                emp = self.to_dict(result)
            return emp


    def update(self, employee):
            session.query(Employees).filter(Employees.emp_no == employee['emp_no']).update({Employees.first_name:employee['first_name'],Employees.last_name:employee['last_name'],Employees.dept_no:employee['dept_no'],Employees.birth_date:employee['birth_date'],Employees.hire_date:employee['hire_date']}, synchronize_session = False)
            session.commit()
            return employee

    
    def delete(self, emp_no):
         session.query(Employees).filter(Employees.emp_no==emp_no).delete()
         session.commit()
  
        


    def to_dict(self,row):
         return {column.name: getattr(row, row.__mapper__.get_property_by_column(column).key) for column in row.__table__.columns}
 


    

employeeDAO = EmployeeDAO()
