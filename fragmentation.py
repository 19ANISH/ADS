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


#vertical fragmentation
#CREATE TABLE BRANCH AS SELECT emp_id,branch_id FROM employee WHERE;

#horizontal fragmentation
#CREATE TABLE Salary AS SELECT salary,emp_id FROM employee WHERE salary=;

@app.route("/",methods=['POST','GET'])
def tables():
    query = Employee.query.all()
        # horiQuery = db.engine.execute(f"CREATE TABLE `Salary` AS SELECT `emp_id`,`{attribute1}` FROM `employee` WHERE `{attribute1}`>='{vattribute1}'")
        # verQuery = db.engine.execute(f"CREATE TABLE `BRANCH` AS SELECT `emp_id`,`{attribute2}` FROM `employee` WHERE `{attribute2}` <= '{vattribute2}'")
    return render_template("tables.html", query=query)

@app.route("/hori",methods=['POST','GET'])
def hori():
    query = Employee.query.all()
    if request.method == 'POST':
        # attribute1 = request.form.get('attribute1')
        # attribute2 = request.form.get('attribute2')
        # vattribute1 = request.form.get('vattribute1')
        # vattribute2 = request.form.get('vattribute2')
        value = request.form.get('value')
        #horiQuery = db.engine.execute(f"CREATE TABLE `horizontal` AS SELECT `{attribute1}`,`{attribute2}` FROM `employee` WHERE `{attribute1}` >='{vattribute1}' AND `{attribute2}` >= '{vattribute2}'")
        horiQuery = db.engine.execute(f"CREATE TABLE `horizontal` AS SELECT * FROM `employee` WHERE `salary` >= '{value}'")
        horiQuery1 = db.engine.execute(f"CREATE TABLE `horizontalOther` AS SELECT * FROM `employee` WHERE `salary` < '{value}'")
    return  render_template("hori.html",query=query)
@app.route("/verti",methods=['POST','GET'])
def verti():
    query= Employee.query.all()
    if request.method == 'POST':
        attribute1 = request.form.get('attribute1')
        attribute2 = request.form.get('attribute2')
        vertiQuery = db.engine.execute(f"CREATE TABLE `vertical` AS SELECT `emp_id`,`{attribute1}`,`{attribute2}` FROM `employee`")
    return render_template("verti.html", query=query)
@app.route("/delH")
def delH():
    try:
        del1 = db.engine.execute("DROP TABLE `horizontal`")
        del1 = db.engine.execute("DROP TABLE `horizontalOther`")
    except Exception as e:
        #flash("No table found")
        return redirect("/hori")
    return redirect("/")
@app.route("/delV")
def delv():
    try:
        del1 = db.engine.execute("DROP TABLE `vertical`")
    except Exception as e:
        #flash("No table found")
        return redirect("/verti")
    return redirect("/")

@app.route("/mixF",methods=['POST','GET'])
def mixF():
    query = Employee.query.all()
    if request.method == 'POST':
        attributeM = request.form.get('attributeM')
        attributeV = request.form.get('attributeV')
        value = request.form.get('value')
        mixQuery = db.engine.execute(f"CREATE TABLE `mix1` AS SELECT `emp_id`,`{attributeM}`,`{attributeV}` FROM `employee`")
        finalQuery = db.engine.execute(f"CREATE TABLE `finalMix` AS SELECT `emp_id`,`{attributeM}`,`{attributeV}` FROM `mix1` WHERE `{attributeM}` = '{value}' ")
    return render_template("mixF.html",query=query)

@app.route("/delM")
def delm():
    try:
        del1 = db.engine.execute("DROP TABLE `finalMix`")
        del2 = db.engine.execute("DROP TABLE `mix1`")
    except Exception as e:
        #flash("No table found")
        return redirect("/mixF")
    return redirect("/")

if __name__ == '__main__':
    app.run(debug=True)  # to run the flask app
