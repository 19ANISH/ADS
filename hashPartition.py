from flask import Flask, json,redirect,render_template,flash,request
from flask_sqlalchemy import SQLAlchemy
import time
local_server=True
app=Flask(__name__)
app.secret_key = "1909"
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
def home():
    query = Employee.query.all()
    return render_template("hashHome.html", query=query)

@app.route("/hash1",methods=['POST','GET'])
def hash1():
    query = db.engine.execute(f"CREATE TABLE ta1 (SELECT * FROM `employee` WHERE MOD(`emp_id`,2)+5 != 5)")
    query2 = db.engine.execute(f"CREATE TABLE ta2 (SELECT * FROM `employee` WHERE MOD(`emp_id`,2)+5 = 5)")
    try:
        dis1 = db.engine.execute(f"SELECT * FROM `ta1`")
        dis2 = db.engine.execute(f"SELECT * FROM `ta2`")
    except Exception as e:
        return redirect("/")
    return render_template("hash1.html",query=query,query2=query2,dis1=dis1,dis2=dis2)

@app.route("/dropH")
def dropH():
    try:
        query = db.engine.execute(f"DROP TABLE ta1")
        query2 = db.engine.execute(f"DROP TABLE ta2")
    except Exception as e:
        return redirect("/hash1")
    return redirect("/")

if __name__ == '__main__':
    app.run(debug=True)  # to run the flask app
