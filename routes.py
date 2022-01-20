from flask import Flask
from flask_restful import Api
from db import app

from services.views import delEmp, getEmp, getEmpId, addEmp, updateEmp, delEmp, addUser, login


def view_routes(app):
    api = Api(app)

    api.add_resource(getEmp, '/api/Getemployee')
    api.add_resource(getEmpId, '/api/Getemployee/<id>')
    api.add_resource(addEmp, '/api/Postemployee')
    api.add_resource(updateEmp, '/api/Upemployee/<id>')
    api.add_resource(delEmp, '/api/Delemployee/<id>')
    api.add_resource(addUser, '/api/users')
    api.add_resource(login, '/api/login')
    

