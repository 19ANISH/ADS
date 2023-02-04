from flask import Flask, json,redirect,render_template,flash,request
from flask_sqlalchemy import SQLAlchemy
import time
local_server=True
app=Flask(__name__)
app.secret_key = "1907"
app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:@localhost/ads'
db=SQLAlchemy(app)

# CREATE TABLE `part1` SELECT * FROM `employee` WHERE MOD(`emp_id`,2)=0
# CREATE TABLE `part2` SELECT * FROM `employee` WHERE MOD(`emp_id`,2)!=0
# SELECT * FROM `part1` ORDER BY `salary`
# SELECT * FROM `part2` ORDER BY `salary`
# SELECT * FROM part1 UNION ALL SELECT * FROM part2 ORDER BY salary

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
    return render_template("ex.html", query=query)
@app.route("/ex1",methods=['POST','GET'])
def ex1():
    query = Employee.query.all()
    # try:
    p1 = db.engine.execute(f"CREATE TABLE `part1` SELECT * FROM `employee` WHERE MOD(`emp_id`,2)=0")
    s1 = db.engine.execute(f"SELECT * FROM `part1`")
    p2 = db.engine.execute(f"CREATE TABLE `part2` SELECT * FROM `employee` WHERE MOD(`emp_id`,2)!=0")
    s2 = db.engine.execute(f"SELECT * FROM `part2`")
    p3 = db.engine.execute(f"SELECT * FROM `part1` ORDER BY `salary`")
    p4 = db.engine.execute(f"SELECT * FROM `part2` ORDER BY `salary`")
    fi = db.engine.execute(f"SELECT * FROM part1 UNION ALL SELECT * FROM part2 ORDER BY salary")
    return render_template("ex1.html",query=query,s1=s1,s2=s2,p3=p3,p4=p4,fi=fi)
    # except Exception as e:
    #     return redirect("/")

@app.route("/delE")
def delE():
    try:
        del1 = db.engine.execute("DROP TABLE `part1`")
        del2 = db.engine.execute("DROP TABLE `part2` ")
    except Exception as e:
        #flash("No table found")
        return redirect("/ex1")
    return redirect("/")

if __name__ == '__main__':
    app.run(debug=True)