from flask import Flask
from flask_restful import Api
from db import app

from services.views import delEmp, getEmp, getEmpId, addEmp, updateEmp, delEmp, addUser


def view_routes(app):
    api = Api(app)

    api.add_resource(getEmp, '/api/getemp')
    api.add_resource(getEmpId, '/api/getemp/<id>')
    api.add_resource(addEmp, '/api/addemp')
    api.add_resource(updateEmp, '/api/updateemp')
    api.add_resource(delEmp, '/api/delemp')
    api.add_resource(addUser, '/api/adduser')

