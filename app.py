from flask import Flask, url_for, request, redirect, abort, jsonify  ,session,render_template

from daoDepartment import departmentDAO
from daoEmployee import employeeDAO
from GoogleDriveAPI import googleDriveAPI
from flask_cors import CORS
app = Flask(__name__, static_url_path='', static_folder='staticpages')
CORS(app)
app.secret_key = 'someSecrtetasdrgsadfgsdfg3ko'
from daoDepartment import departmentDAO


@app.route('/')
def index():
    if not 'username' in session:
        return redirect(url_for('login'))
    return render_template('index.html')


@app.route('/employeesUI')
def employeesUI():
    if not 'username' in session:
        return redirect(url_for('login'))
    return render_template('employeesUI.html')

@app.route('/departmentsUI')
def departmentsUI():
    if not 'username' in session:
        return redirect(url_for('login'))
    return render_template('departmentsUI.html')

@app.route('/filesUI')
def filesUI():
    if not 'username' in session:
        return redirect(url_for('login'))
    return render_template('filesUI.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            session['username']=request.form['username']
            return redirect(url_for('index'))
    return render_template('login.html', error=error)




    
@app.route("/employees")
def getAllEmployees():
    if not 'username' in session:
        abort(401)
    return jsonify(employeeDAO.getAll())


@app.route('/employees/<int:emp_no>')
def findByNo(emp_no):
    if not 'username' in session:
        abort(401)
    return jsonify(employeeDAO.findByNo(emp_no))


@app.route('/employees', methods=['POST'])
def create():
   if not 'username' in session:
        abort(401)
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


@app.route('/department', methods=['POST'])
def createDepartment():
   if not 'username' in session:
        abort(401)
   if not request.json:
        abort(400)

   department = {
        
        "dept_no": request.json["dept_no"],
        "dept_name": request.json["dept_name"]
        
   }
   return jsonify(departmentDAO.create(department))

   return "served by Create "
    


@app.route("/department")
def alldepartments():
    if not 'username' in session:
        abort(401)
    return jsonify(departmentDAO.getAll())


@app.route('/department/<int:dept_no>')
def findByDeptNo(dept_no):
    if not 'username' in session:
        abort(401)
    return jsonify(departmentDAO.findByNo(dept_no))



@app.route('/employees/<int:emp_no>', methods=['PUT'])
def update(emp_no):
    if not 'username' in session:
        abort(401)
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

@app.route('/department/<int:dept_no>', methods=['PUT'])
def updateDept(dept_no):
    if not 'username' in session:
        abort(401)
    foundDepartment=departmentDAO.findByNo(dept_no)
    if foundDepartment == {}:
        return jsonify({}), 404
    currentDepartment = foundDepartment
    if 'dept_no' in request.json:
        currentDepartment['dept_no'] = request.json['dept_no']
    if 'dept_name' in request.json:
        currentDepartment['dept_name'] = request.json['dept_name']
   
    departmentDAO.update(currentDepartment)

    return jsonify(currentDepartment)

@app.route('/employees/<int:emp_no>', methods=['DELETE'])
def delete(emp_no):
    if not 'username' in session:
        abort(401)
    employeeDAO.delete(emp_no)

    return jsonify({"done": True})


@app.route('/department/<int:dept_no>', methods=['DELETE'])
def deleteDepartment(dept_no):
    if not 'username' in session:
        abort(401)
    departmentDAO.delete(dept_no)
    return jsonify({"done": True})


@app.route("/files")
def allfilesINGoogleDrive():
    if not 'username' in session:
        abort(401)
    return jsonify(googleDriveAPI.getAllFiles())


@app.route('/logout')
def logout():
   # if not 'username' in session:
    #    abort(401)
    session.pop('username',None)
    return redirect(url_for('login'))
    
if __name__ == "__main__":
    app.run(debug=True)
   
