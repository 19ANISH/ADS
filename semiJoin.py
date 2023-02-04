from flask import Flask, json,redirect,render_template,flash,request
from flask_sqlalchemy import SQLAlchemy
import time
local_server=True
app=Flask(__name__)
app.secret_key = "1908"
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

class Branch(db.Model):
    branch_id = db.Column(db.Integer,primary_key=True)
    branch_name = db.Column(db.String(40))
    mgr_id = db.Column(db.Integer)
    mgr_start_date = db.Column(db.Date)



@app.route("/",methods=['POST','GET'])
def home():
    query = Branch.query.all()
    query2 = Employee.query.all()
    return render_template("semiHome.html", query=query,query2=query2)

@app.route("/semi",methods=['POST','GET'])
def hori():
    query = Branch.query.all()
    query2 = Employee.query.all()
    dis1 = db.engine.execute(f"SELECT * FROM `employee`")
    dis2 = db.engine.execute(f"SELECT `branch`.`branch_id`,`branch`.`branch_name`,`branch`.`mgr_id`,`branch`.`mgr_start_date` FROM `branch` INNER JOIN `employee` ON `branch`.`mgr_id` = `employee`.`emp_id` ORDER BY `employee`.`emp_id`")
    finalQ = db.engine.execute(f"CREATE TABLE `join1` SELECT `employee`.`emp_id`,`employee`.`first_name`,`employee`.`last_name`,`employee`.`birth_date`,`employee`.`sex`, `employee`.`salary`, `employee`.`super_id`, `employee`.`branch_id`,`branch`.`branch_name`,`branch`.`mgr_start_date` FROM `employee` INNER JOIN `branch` ON `employee`.`emp_id` = `branch`.`mgr_id` ORDER BY `employee`.`emp_id`")
    ans =  db.engine.execute(f"SELECT * FROM `join1`")
    return render_template("semi.html",query=query,query2=query2,dis1=dis1,dis2=dis2,finalQ=finalQ,ans=ans)

@app.route("/delS")
def delS():
    try:
        del1 = db.engine.execute("DROP TABLE `join1`")
    except Exception as e:
        #flash("No table found")
        return redirect("/semi")
    return redirect("/")

if __name__ == '__main__':
    app.run(debug=True)  # to run the flask app
