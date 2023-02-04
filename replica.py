from flask import Flask, json,redirect,render_template,flash,request
from flask_sqlalchemy import SQLAlchemy
import time
local_server=True
app=Flask(__name__)
app.secret_key = "1907"
app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:@localhost/ads'
db=SQLAlchemy(app)
#
# CREATE TABLE replication.rep1
# AS
# SELECT * FROM ads.employee;

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
    return render_template("table.html", query=query)


@app.route("/rep1",methods=['POST','GET'])
def rep1():
    query = Employee.query.all()
    if request.method == 'POST':
        value = request.form.get('value')
        horiQuery = db.engine.execute(f"CREATE TABLE `horizontal` AS SELECT `emp_id`,`salary` FROM `employee` WHERE `salary` >= '{value}'")
    return  render_template("rep1.html",query=query)

@app.route("/rep",methods=['POST','GET'])
def rep():
    horiQuery = db.engine.execute(f"CREATE TABLE `replication`.`horizontal` ( `emp_id` int(11) NOT NULL, `first_name` varchar(10) NOT NULL, `last_name` varchar(12) NOT NULL, `birth_date` date NOT NULL, `sex` varchar(1) NOT NULL, `salary` int(11) NOT NULL, `super_id` int(11) NOT NULL, `branch_id` int(11) NOT NULL ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4; SET SQL_MODE='NO_AUTO_VALUE_ON_ZERO'; INSERT INTO `replication`.`horizontal`(`emp_id`, `first_name`, `last_name`, `birth_date`, `sex`, `salary`, `super_id`, `branch_id`) SELECT `emp_id`, `first_name`, `last_name`, `birth_date`, `sex`, `salary`, `super_id`, `branch_id` FROM `ads`.`horizontal`")
    horiQueryO = db.engine.execute(f"CREATE TABLE `replication`.`horizontalother` ( `emp_id` int(11) NOT NULL, `first_name` varchar(10) NOT NULL, `last_name` varchar(12) NOT NULL, `birth_date` date NOT NULL, `sex` varchar(1) NOT NULL, `salary` int(11) NOT NULL, `super_id` int(11) NOT NULL, `branch_id` int(11) NOT NULL ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4; SET SQL_MODE='NO_AUTO_VALUE_ON_ZERO'; INSERT INTO `replication`.`horizontalother`(`emp_id`, `first_name`, `last_name`, `birth_date`, `sex`, `salary`, `super_id`, `branch_id`) SELECT `emp_id`, `first_name`, `last_name`, `birth_date`, `sex`, `salary`, `super_id`, `branch_id` FROM `ads`.`horizontalother`")
    horiQuery1 = db.engine.execute(f"CREATE TABLE `replication1`.`horizontal` ( `emp_id` int(11) NOT NULL, `first_name` varchar(10) NOT NULL, `last_name` varchar(12) NOT NULL, `birth_date` date NOT NULL, `sex` varchar(1) NOT NULL, `salary` int(11) NOT NULL, `super_id` int(11) NOT NULL, `branch_id` int(11) NOT NULL ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4; SET SQL_MODE='NO_AUTO_VALUE_ON_ZERO'; INSERT INTO `replication1`.`horizontal`(`emp_id`, `first_name`, `last_name`, `birth_date`, `sex`, `salary`, `super_id`, `branch_id`) SELECT `emp_id`, `first_name`, `last_name`, `birth_date`, `sex`, `salary`, `super_id`, `branch_id` FROM `ads`.`horizontal`")
    horiQueryO1 = db.engine.execute(f"CREATE TABLE `replication1`.`horizontalother` ( `emp_id` int(11) NOT NULL, `first_name` varchar(10) NOT NULL, `last_name` varchar(12) NOT NULL, `birth_date` date NOT NULL, `sex` varchar(1) NOT NULL, `salary` int(11) NOT NULL, `super_id` int(11) NOT NULL, `branch_id` int(11) NOT NULL ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4; SET SQL_MODE='NO_AUTO_VALUE_ON_ZERO'; INSERT INTO `replication1`.`horizontalother`(`emp_id`, `first_name`, `last_name`, `birth_date`, `sex`, `salary`, `super_id`, `branch_id`) SELECT `emp_id`, `first_name`, `last_name`, `birth_date`, `sex`, `salary`, `super_id`, `branch_id` FROM `ads`.`horizontalother`")
    return  render_template("rep.html")

if __name__ == '__main__':
    app.run(debug=True)  # to run the flask app
