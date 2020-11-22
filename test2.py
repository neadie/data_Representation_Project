from daoDepartment import departmentDAO

dept1 = {   
    'dept_no': '0063',
    'dept_name': 'h'
}
dept2 = {  
   'dept_no': '0035',
    'dept_name': 'Medcial Physics'
}

departmentDAO.create(dept1)
returnValue = departmentDAO.getAll()
print(returnValue)
returnValue = departmentDAO.findByNo(2)
print("find By Id")
print(returnValue)
returnValue = departmentDAO.update(dept2)
print(returnValue)
returnValue = departmentDAO.delete('0093')
print(returnValue)

