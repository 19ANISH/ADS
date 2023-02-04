from flask import Flask, json,redirect,render_template,flash,request
from flask_sqlalchemy import SQLAlchemy
import time
local_server=True
app=Flask(__name__)
app.secret_key = "1907"
app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:@localhost/ads'
db=SQLAlchemy(app)

class Employee(db.Model):
    emp_id = db.Column(db.Integer,primary_key=True)
    first_name = db.Column(db.String(10))
    last_name = db.Column(db.String(12))
    birth_date = db.Column(db.Date)
    sex = db.Column(db.String(1))
    salary = db.Column(db.Integer)
    super_id = db.Column(db.Integer)
    branch_id = db.Column(db.Integer)

@app.route("/",methods=['POST','GET'])
def tables():
    query = Employee.query.all()
    return render_template("rangeHome.html", query=query)

@app.route("/range",methods=['POST','GET'])
def range():
    query = Employee.query.all()
    r1 = db.engine.execute("SELECT * FROM `employee` WHERE MOD(`emp_id`,5) = 0")
    r2 = db.engine.execute("SELECT * FROM `employee` WHERE MOD(`emp_id`,5) != 0")
if __name__ == '__main__':
    app.run(debug=True)