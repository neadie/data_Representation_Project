from sqlalchemy import create_engine
import sqlalchemy 
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
engine = create_engine('mysql+mysqlconnector://root@localhost/data_representation_project?charset=utf8mb4')


class Employees(Base):
    __tablename__ = "employees"
    emp_no = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    first_name = sqlalchemy.Column(sqlalchemy.String(80), unique=True, nullable=False)
    last_name = sqlalchemy.Column(sqlalchemy.String(80), unique=True, nullable=False)
    dept_no = sqlalchemy.Column(sqlalchemy.Integer, unique=False, nullable=False)
    birth_date = sqlalchemy.Column(sqlalchemy.DateTime, unique=False, nullable=True)
    hire_date = sqlalchemy.Column(sqlalchemy.DateTime, unique=False, nullable=True)
    
    
    
        
        
class Departments(Base):
   __tablename__ = "departments"
   dept_no = sqlalchemy.Column(sqlalchemy.String(4), primary_key=True)
   dept_name = sqlalchemy.Column(sqlalchemy.String(80), unique=True, nullable=False)



Session = sessionmaker(bind=engine)

# create a Session
session = Session()
