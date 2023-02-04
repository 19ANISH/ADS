from flask import Flask, json,redirect,render_template,flash,request
from flask_sqlalchemy import SQLAlchemy
import time
local_server=True
app=Flask(__name__)
app.secret_key = "1907"
app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:@localhost/'
db=SQLAlchemy(app)

@app.route("/",methods=['POST','GET'])
def home():
    dis1 = db.engine.execute(f"SELECT * FROM `site1`.`branch`")
    dis2 = db.engine.execute(f"SELECT * FROM `site1`.`branch supplier`")
    dis3 = db.engine.execute(f"SELECT * FROM `site2`.`client`")
    dis4 = db.engine.execute(f"SELECT * FROM `site2`.`employee`")
    return render_template("phome.html",dis1=dis1,dis2=dis2,dis3=dis3,dis4=dis4)
@app.route("/p2",methods=['POST','GET'])
def p2():
    site1 = db.engine.execute (f"CREATE TABLE `site3`.`temp1` SELECT `site1`.`branch supplier`.`branch_id`, `site1`.`branch supplier`.`supplier_name`, `site1`.`branch supplier`.`supply_type`,`site1`.`branch`.`branch_name`,`site1`.`branch`.`mgr_id`,`site1`.`branch`.`mgr_start_date` FROM `site1`.`branch` INNER JOIN  `site1`.`branch supplier` ON `site1`.`branch supplier`.`branch_id` =  `site1`.`branch`.`branch_id`")
    sdis1 = db.engine.execute(f"SELECT * FROM `site3`.`temp1`")
    site2 = db.engine.execute(f"CREATE TABLE `site3`.`temp2` SELECT `site2`.`client`.`client_id`,`site2`.`client`.`client_name`,`site2`.`client`.`branch_id`,`site2`.`employee`.`emp_id`,`site2`.`employee`.`first_name`,`site2`.`employee`.`last_name`,`site2`.`employee`.`birth_date`,`site2`.`employee`.`sex`,`site2`.`employee`.`salary`,`site2`.`employee`.`super_id` FROM `site2`.`employee` INNER JOIN `site2`.`client` ON  `site2`.`client`.`branch_id` = `site2`.`employee`.`branch_id`")
    sdis2 = db.engine.execute(f"SELECT * FROM `site3`.`temp2`")
    return render_template("p2.html",site1=site1,sdis1=sdis1,site2=site2,sdis2=sdis2)
@app.route("/pfinal",methods=['POST','GET'])
def pfinal():
    fin = db.engine.execute(f"CREATE TABLE `site3`.`final` SELECT `site3`.`temp1`.`branch_id`,`site3`.`temp1`.`branch_name`,`site3`.`temp1`.`supplier_name`,`site3`.`temp1`.`supply_type`,`site3`.`temp1`.`mgr_id`,`site3`.`temp1`.`mgr_start_date`,`site3`.`temp2`.`client_id`,`site3`.`temp2`.`client_name`,`site3`.`temp2`.`emp_id`,`site3`.`temp2`.`first_name`,`site3`.`temp2`.`last_name`,`site3`.`temp2`.`birth_date`,`site3`.`temp2`.`sex`,`site3`.`temp2`.`salary`,`site3`.`temp2`.`super_id` FROM `site3`.`temp1` INNER JOIN `site3`.`temp2` ON `site3`.`temp1`.`branch_id` = `site3`.`temp2`.`branch_id`")
    fdis = db.engine.execute(f"SELECT * FROM `site3`.`final`")
    return render_template("pfinal.html",fin=fin,fdis=fdis)
@app.route("/delSite")
def delSite():
    try:
        d1 = db.engine.execute(f"DROP TABLE `site3`.`final`")
        d2 = db.engine.execute(f"DROP TABLE `site3`.`temp1`")
        d3 = db.engine.execute(f"DROP TABLE `site3`.`temp2`")
    except Exception as e:
        return redirect("/pfinal")
    return redirect("/")
if __name__ == '__main__':
    app.run(debug=True)
