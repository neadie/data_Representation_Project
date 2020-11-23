from daoDepartment import departmentDAO

dept1 = {   
    'dept_no': '0010',
    'dept_name': 'Physiocs'
}
dept2 = {  
   'dept_no': '0035',
    'dept_name': 'Medcial Physics'
}

#departmentDAO.create(dept1)
#returnValue = departmentDAO.getAll()
#print(returnValue)
#returnValue = departmentDAO.findByNo(2)
#print("find By Id")
#print(returnValue)
returnValue = departmentDAO.update(dept1)
print(returnValue)
#returnValue = departmentDAO.delete('0093')
#print(returnValue)

