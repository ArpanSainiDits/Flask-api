from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost:3306/flask'
db = SQLAlchemy(app)
migrate = Migrate(app, db)
ma = Marshmallow(app)


class Employee(db.Model):
   __tablename__ = "employee"
   id = db.Column(db.Integer, primary_key=True)
   name = db.Column(db.String(20))
   email = db.Column(db.String(50), nullable= False)
   mobile = db.Column(db.Integer)
   department = db.Column(db.String(20))
   joining_date = db.Column(db.Date)
   designation = db.Column(db.String(50))
   experience = db.Column(db.String(100))
   level = db.Column(db.Integer)
   left_date = db.Column(db.Date)
   dob = db.Column(db.Date)
   created = db.Column(db.DateTime)
   updated = db.Column(db.DateTime)

   def create(self):
       db.session.add(self)
       db.session.commit()
       return self

   def __init__(self, name, email, mobile, department, joining_date, designation, experience, level, left_date, dob):
       self.name = name
       self.email = email
       self.mobile = mobile
       self.department = department
       self.joining_date = joining_date
       self.designation = designation
       self.experience = experience
       self.level = level
       self.left_date = left_date
       self.dob = dob

   def __repr__(self):
       return f"{self.id}"


db.create_all()
