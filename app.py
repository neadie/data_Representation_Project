from flask import Flask, url_for, request, redirect, abort, jsonify  
from employeeAndDept import employeeDept
from daoDepartment import departmentDAO
from daoEmployee import employeeDAO

app = Flask(__name__, static_url_path='', static_folder='staticpages')

from daoDepartment import departmentDAO


@app.route("/")
def index():
 return ""
    
@app.route("/employees")
def getAllEmployees():
    return jsonify(employeeDAO.getAll())


@app.route('/employees/<int:emp_no>')
def findByNo(emp_no):
    return jsonify(employeeDAO.findByNo(emp_no))


@app.route('/employees', methods=['POST'])
def create():
   
    if not request.json:
        abort(400)

    employee = {
        
        "first_name": request.json["first_name"],
        "last_name": request.json["last_name"],
        "dept_no": request.json["dept_no"],
        "birth_date": request.json["birth_date"],
        "hire_date": request.json["hire_date"]
    }
    return jsonify(employeeDAO.create(employee))

    return "served by Create "
    


@app.route("/department")
def alldepartments():
    return jsonify(departmentDAO.getAll())



@app.route('/employees/<int:emp_no>', methods=['PUT'])
def update(emp_no):
    foundEmployee=employeeDAO.findByNo(emp_no)
    print (foundEmployee)
    if foundEmployee == {}:
        return jsonify({}), 404
    currentEmployee = foundEmployee
    if 'first_name' in request.json:
        currentEmployee['first_name'] = request.json['first_name']
    if 'last_name' in request.json:
        currentEmployee['last_name'] = request.json['last_name']
    if 'dept_no' in request.json:
        currentEmployee['dept_no'] = request.json['dept_no']
    if 'birth_date' in request.json:
        currentEmployee['birth_date'] = request.json['birth_date']
    if 'hire_date' in request.json:
        currentEmployee['hire_date'] = request.json['hire_date']
    employeeDAO.update(currentEmployee)

    return jsonify(currentEmployee)

#delete
# curl -X DELETE http://127.0.0.1:5000/employees/1


@app.route('/employees/<int:emp_no>', methods=['DELETE'])
def delete(emp_no):
    employeeDAO.delete(emp_no)

    return jsonify({"done": True})

    
if __name__ == "__main__":
    app.run(debug=True)
   
