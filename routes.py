from flask import Flask
from flask_restful import Api, Resource
from db import app

from app import delEmp, getEmp, getEmpId, addEmp, updateEmp, delEmp, addUser





api = Api(app)

api.add_resource(getEmp, '/api/getemp')
api.add_resource(getEmpId, '/api/getemp/<id>')
api.add_resource(addEmp, '/api/addemp')
api.add_resource(updateEmp, '/api/updateemp')
api.add_resource(delEmp, '/api/delemp')
api.add_resource(addUser, '/api/adduser')


if __name__ == '__main__':
    app.run(debug=True)
