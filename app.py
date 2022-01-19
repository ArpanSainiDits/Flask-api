
from passlib.apps import custom_app_context as pwd_context
from enum import unique
from flask import Flask, request, jsonify, make_response, abort
from flask_sqlalchemy import SQLAlchemy
from marshmallow import fields
# from marshmallow_sqlalchemy import ModelSchema
import datetime
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate

import Models.employee as foo
import Models.user as U

import schema as e


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost:3306/flask'
db = SQLAlchemy(app)
migrate = Migrate(app, db)
ma = Marshmallow(app)


# employee post 

@app.route('/api/employee', methods=['POST'])
def add_employee():
    #get data from request
    name = request.json['name']
    email = request.json['email']
    mobile = request.json['mobile']
    department = request.json['department']
    joining_date = request.json['joining_date']
    designation = request.json['designation']
    experience = request.json['experience']
    level = request.json['level']
    left_date = request.json['left_date']
    dob = request.json['dob']
    

    employee = foo.Employee(name, email, mobile, department,
                        joining_date, designation, experience, level, left_date, dob)
    
    db.session.add(employee)
    db.session.commit()
    return e.employeeSchema.jsonify(employee)


@app.route('/api/employee', methods=['GET'])
def index():
   get_employee = foo.Employee.query.all()
   employee_schema = e.employeeSchema(many=True)
   employee = employee_schema.dump(get_employee)
   return make_response(jsonify({"employee": employee}))


@app.route('/api/employee/<id>', methods=['GET'])
def get_employee_by_id(id):
   get_employee = foo.Employee.query.get(id)
   todo_schema = e.employeeSchema()
   employee = todo_schema.dump(get_employee)
   return make_response(jsonify({"employee": employee}))


@app.route('/api/employee/<id>', methods=['PUT'])
def update_employee_by_id(id):
   data = request.get_json()
   get_employee = foo.Employee.query.get(id)
   if data.get('name'):
       get_employee.name = data['name']
   if data.get('mobile'):
       get_employee.mobile = data['mobile']
       
   if data.get('department'):
       get_employee.department = data['department']
   if data.get('joining_date'):
       get_employee.joining_date = data['joining_date']
   if data.get('designation'):
       get_employee.designation = data['designation']
   if data.get('experience'):
       get_employee.experience = data['experience']
   if data.get('level'):
       get_employee.level = data['level']
   if data.get('left_date'):
       get_employee.left_date = data['left_date']
   if data.get('dob'):
       get_employee.dob = data['dob']
       
       
   db.session.add(get_employee)
   db.session.commit()
   employee_schema = e.employeeSchema(
       only=['id', 'name', 'mobile', 'department', 'joining_date', 'designation', 'experience', 'level', 'left_date', 'dob'])
   employee = employee_schema.dump(get_employee)

   return make_response(jsonify({"employee": employee}))


@app.route('/api/employee/<id>', methods=['DELETE'])
def delete_employee_by_id(id):
   get_employee = foo.Employee.query.get(id)
   db.session.delete(get_employee)
   db.session.commit()
   return make_response("", 204)

   
    
@app.route('/api/users', methods=['POST'])
def new_user():
    email = request.json.get('email')
    password = request.json.get('password')
    if email is None or password is None:
        abort(400)  # missing arguments
    if U.User.query.filter_by(email=email).first() is not None:
        abort(400)  # existing user
    user = U.User(email=email)
    user.hash_password(password)
    db.session.add(user)
    db.session.commit()
    return jsonify({'email': user.email, 'status':'successfully registered'}), 201, 


# {'Location': url_for('get_user', id=user.id, _external=True)}

    
@app.route('/api/login', methods=['POST'])    
def login_user():
    email = request.json.get('email')
    password = request.json.get('password')
    
    user = U.User.query.filter_by(email=email).first()
    
    passs = (pwd_context.verify(password, user.password_hash))
    
    if passs == True:
        
        
        
        return jsonify({'User': user.email, 'status':'successfully logged In'}), 201, 
    else:
        return jsonify({'status': 'Incorrect email or password'})
    


if __name__ == '__main__':
    app.run(debug=True)
