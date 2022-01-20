from flask import Flask
from flask_restplus import Api


from .app import add_employee



app = Flask(__name__)
def generate_route(app):
    
    api = Api(app)
    
    api.add_resource(add_employee, '/api/employee')
