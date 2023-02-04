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

class Branch(db.Model):
    branch_id = db.Column(db.Integer,primary_key=True)
    branch_name = db.Column(db.String(40))
    mgr_id = db.Column(db.Integer)
    mgr_start_date = db.Column(db.Date)


@app.route("/",methods=['POST','GET'])
def hashjoin():
    query = Employee.query.all()
    query2 = Branch.query.all()
    return render_template('hashjoin.html',query=query,query2=query2)
@app.route("/hashjoin1",methods=['POST','GET'])
def hash1():
    part1 = db.engine.execute(f"CREATE TABLE `ta1` SELECT * FROM `employee` WHERE MOD(`branch_id`,2) = 0")
    dis1 = db.engine.execute(f"SELECT * FROM `ta1`")
    part2 = db.engine.execute(f"CREATE TABLE `ta2` SELECT * FROM `employee` WHERE MOD(`branch_id`,2) != 0")
    dis2 = db.engine.execute(f"SELECT * FROM `ta2`")
    bpart1 = db.engine.execute(f"CREATE TABLE `bta1` SELECT * FROM `branch` WHERE MOD(`branch_id`,2) = 0")
    bdis1 = db.engine.execute(f"SELECT * FROM `bta1`")
    bpart2 = db.engine.execute(f"CREATE TABLE `bta2` SELECT * FROM `branch` WHERE MOD(`branch_id`,2) != 0")
    bdis2 = db.engine.execute(f"SELECT * FROM `bta2`")
    return render_template("hashjoin1.html",part1=part1,part2=part2,bpart1=bpart1,bpart2=bpart2,dis1=dis1,dis2=dis2,bdis1=bdis1,bdis2=bdis2)

@app.route("/hashjoin2",methods=['POST','GET'])
def hash2():
    j1 = db.engine.execute(f"CREATE TABLE `join1` SELECT `ta1`.`emp_id`,`ta1`.`first_name`,`ta1`.`last_name`,`ta1`.`birth_date`,`ta1`.`sex`,`ta1`.`salary`,`ta1`.`super_id`,`ta1`.`branch_id`,`bta1`.`branch_name`,`bta1`.`mgr_id`,`bta1`.`mgr_start_date` FROM `ta1` INNER JOIN `bta1` WHERE `ta1`.`branch_id` = `bta1`.`branch_id`")
    disJ1 = db.engine.execute(f"SELECT * FROM `join1`")
    j2 = db.engine.execute(f"CREATE TABLE `join2` SELECT `ta2`.`emp_id`,`ta2`.`first_name`,`ta2`.`last_name`,`ta2`.`birth_date`,`ta2`.`sex`,`ta2`.`salary`,`ta2`.`super_id`,`ta2`.`branch_id`,`bta2`.`branch_name`,`bta2`.`mgr_id`,`bta2`.`mgr_start_date` FROM `ta2` INNER JOIN `bta2` WHERE `ta2`.`branch_id` = `bta2`.`branch_id`")
    disJ2 = db.engine.execute(f"SELECT * FROM `join2`")
    disF = db.engine.execute(f"SELECT * FROM `join1` UNION SELECT * FROM `join2`")
    return render_template("hashjoin2.html",j1=j1,j2=j2,disJ1=disJ1,disJ2=disJ2,disF=disF)


@app.route("/delHJ")
def delhj():
    try:
        del1 = db.engine.execute("DROP TABLE `join1`")
        del2 = db.engine.execute("DROP TABLE `join2`")
        del3 = db.engine.execute("DROP TABLE `bta1`")
        del4 = db.engine.execute("DROP TABLE `bta2`")
        del5 = db.engine.execute("DROP TABLE `ta1`")
        del6 = db.engine.execute("DROP TABLE `ta2`")
    except Exception as e:
        #flash("No table found")
        return redirect("/hashjoin2")
    return redirect("/")
if __name__ == '__main__':
    app.run(debug=True)