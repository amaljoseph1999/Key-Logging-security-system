from flask import Flask,render_template,request, redirect,session
from DBConnection import Db
import datetime

import re
import hashlib
import boto3,botocore
import os
# import pyAesCrypt
import smtplib
import random
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import base64
import sys
import pyAesCrypt


app = Flask(__name__)
db=Db()
app.secret_key="abc"

# rpath="D:\\don\\keylogWeb\\"
rpath="E:\\progress\\keylogWeb\\"


@app.route('/forgot')
def forgot():
    return render_template("forget.html")


@app.route('/forgot1',methods=['post'])
def forgot1():
    email=request.form['name']
    qry=db.selectOne("select * from login where name='"+email+"' ")
    # print(qry)
    pswd=qry['passwd']
    # otpvalue=random.randint(0000,9999)
    if qry is not None:

        try:
            gmail = smtplib.SMTP('smtp.gmail.com', 587)

            gmail.ehlo()

            gmail.starttls()

            gmail.login('emailll', 'pswddd')

        except Exception as e:
            print("Couldn't setup email!!" + str(e))

        msg = MIMEText("Your Password is " + pswd)

        msg['Subject'] = 'Verification'

        msg['To'] = email

        msg['From'] = 'emailll'

        try:

            gmail.send_message(msg)

        except Exception as e:

            print("COULDN'T SEND EMAIL", str(e))
    return "Mail Send"




@app.route('/')
def log_in():
    return render_template("login.html")

@app.route('/qr',methods=['get','post'])
def qr():
# @app.route('/qr/<i>/<j>')
# def qr(i,j):
    s=session['lid']
    s=str(s)+"#"

    rs=[]

    z=""
    for x in range(0,6):
        p=random.randrange(x*6,(x+1)*6)
        rs.append(p)
        s+=str(p)+"-"
        z+=str(p)+"#"
        print(str(x)+"---"+str(p))

    s=s[:-1]
    z=z[:-1]
    session["rs"]=z

    print(s)
    encodedBytes = base64.b64encode(s.encode("utf-8"))
    encodedStr = str(encodedBytes, "utf-8")
    print(encodedStr)
    # return render_template("qr.html",data=encodedStr,data1=i,data2=j)
    return render_template("qr.html",data=encodedStr)

@app.route('/login',methods=['post'])
def login():
    userid = request.form['name']
    pw = request.form['passwd']
    qry = "select * from login where  name='"+userid+"' and passwd='"+pw+"'"
    res = db.selectOne(qry)

    if res==None:
         "<scirpt>alert('')</script>"
    else:
        print("success")
        tp=res['type']
        session['lid']=res['loginid']

        if tp=="admin":
            session['lg'] = "lin"
            return redirect("/admin_home")
        elif tp=="employee":
            session['lg'] = "lin"
            return redirect("/emp_home")
        elif tp == "department":
            session['lg'] = "lin"
            return redirect("/dep_home")
        else:
            return log_in()


@app.route('/checks',methods=['post'])
def checks():
    if session['lg']=='lin':
        dt = request.form['hd']
        pw = session["rs"]

        if(dt==pw):
            print("xxxx")
            ss=downfilCloud()
            tp=session['tp']
            if tp=="send":
                return redirect("/view_sendfile")
            elif tp=="rec":
                return redirect("/view_revfile")
            else:
                return "jjjj"
        else:
            return "Failed"
            # return redirect("/")

    else:
        return  redirect('/')


@app.route('/admin_home')
def hello_world():
    if session['lg'] == 'lin':
        return render_template("admin/admin_home.html")
    else:
        return redirect('/')





@app.route('/logout')
def logout():
    session["lg"]=" "
    return render_template("login.html")


@app.route('/add_dept')
def add_dept():
    if session['lg'] == 'lin':
        return render_template("admin/dep_mgnt.html")
    else:
        return redirect('/')


@app.route('/add_dept_post',methods=['post'])
def add_dept_post():
    if session['lg'] == 'lin':
        dept = request.form['department']
        passwd = request.form['email']
        import random
        pwd = random.randint(00000, 99999)
        qry2 = "insert into login(name,passwd,type) values('" + passwd + "','" + str(pwd) + "','department')"
        res1 = db.insert(qry2)
        qry = "insert into dept values('" + str(res1) + "','" + dept + "','" + passwd + "')"
        res = db.insert(qry)

        try:
            gmail = smtplib.SMTP('smtp.gmail.com', 587)

            gmail.ehlo()

            gmail.starttls()

            gmail.login('melbinkjoz@gmail.com', '123HipHop123')  # mail that send password

        except Exception as e:
            print("Couldn't setup email!!" + str(e))

        msg = MIMEText("Your Password is " + str(passwd))  # content

        msg['Subject'] = 'Verification'

        msg['To'] = passwd

        msg['From'] = 'melbinkjoz@gmail.com'

        try:

            gmail.send_message(msg)

        except Exception as e:

            print("COULDN'T SEND EMAIL", str(e))
        return '<script> alert("success");window.location="/add_dept"</script>'
    else:
        return redirect('/')


@app.route('/add_imei/<i>')
def add_imei(i):
    if session['lg'] == 'lin':
        return render_template("admin/add_imei.html", data=i)
    else:
        return redirect('/')


@app.route('/add_imei_post/<data>',methods=['post'])
def add_imei_post(data):
    if session['lg'] == 'lin':
        imei1 = request.form['imei1']

        # import random
        # pwd=random.randint(00000,99999)
        # qry2 = "insert into login(name,passwd,type) values('" + passwd + "','"+str(pwd)+"','department')"
        # res1 = db.insert(qry2)
        # qry="insert into dept values('"+str(res1)+"','"+dept+"','"+passwd+"')"
        qry = "insert into imei(imei1,emp_id) values ('" + imei1 + "','" + data + "')"
        res = db.insert(qry)
        return '<script> alert("success");window.location="/add_imei"</script>'


    else:
        return redirect('/')

@app.route('/view_dept')
def view_dept():
    if session['lg'] == 'lin':
        qry = "select * from dept "
        res = db.select(qry)
        return render_template("admin/view_dep.html", data=res)


    else:
        return redirect('/')


@app.route('/dept_dlt/<i>')
def dept_dlt(i):
    if session['lg'] == 'lin':
        qry = "delete from dept where dept_id='" + i + "'"
        res = db.delete(qry)
        return view_dept()

    else:
        return redirect('/')



@app.route('/dep_edit/<i>')
def dep_edit(i):
    if session['lg'] == 'lin':
        qry = "select * from dept where dept_id='" + i + "'"
        res = db.selectOne(qry)
        return render_template("admin/dep_edit.html", data=res)

    else:
        return redirect('/')

@app.route('/dept_editb',methods=['post'])
def dept_editb():
    if session['lg'] == 'lin':
        deptname = request.form['dep_name']
        did = request.form['did']
        qry = "update dept set name='" + deptname + "' where dept_id='" + str(did) + "'"
        res = db.update(qry)
        return view_dept()

    else:
        return redirect('/')



@app.route('/add_work')
def add_work():
    if session['lg'] == 'lin':
        qry = "select * from dept"
        res = db.select(qry)
        return render_template("admin/add_work.html", data=res)
    else:
        return redirect('/')

@app.route('/add_work_post',methods=['post'])
def add_work_post():
    if session['lg'] == 'lin':
        work = request.form['work']
        dep_id = request.form['dep']
        qry = "insert into work (dep_id,w_work) values('" + dep_id + "','" + work + "')"
        res = db.insert(qry)
        return '<script> alert("success");window.location="/add_work"</script>'


    else:
        return redirect('/')

@app.route('/edit_work1/<i>')
def edit_work(i):
    if session['lg'] == 'lin':
        qry = "select * from work where workid='" + i + "'"
        res = db.selectOne(qry)
        return render_template("admin/edit_work1.html", data=res)


    else:
        return redirect('/')

@app.route('/work_editb/<a>',methods=['post'])
def work_editb(a):
    if session['lg'] == 'lin':
        type = request.form['worktype']
        work = request.form['work']

        qry = "update work set w_type='" + type + "',w_work='" + work + "' where workid='" + a + "'"
        res = db.update(qry)
        return '<scirpt>alert("updated")</script>'

    else:
        return redirect('/')


@app.route('/work_dlt/<i>')
def work_dlt(i):
    if session['lg'] == 'lin':
        qry = "delete from work where workid='" + i + "'"
        res = db.delete(qry)
        return view_work()

    else:
        return redirect('/')


@app.route('/view_work')
def view_work():
    if session['lg'] == 'lin':
        qry = "select * from work inner join emp group by workid "
        res = db.select(qry)
        return render_template("admin/view_work.html", data=res)

    else:
        return redirect('/')


@app.route('/add_emp')
def add_emp():
    if session['lg'] == 'lin':
        db = Db()
        qry = "select * from dept"
        res = db.select(qry)
        return render_template("admin/add_emp.html", data=res)

    else:
        return redirect('/')

@app.route('/add_emp_post',methods=['post'])
def add_emp_post():
    if session['lg'] == 'lin':
        emp_name = request.form['names']
        emp_lastname = request.form['lastname']
        emp_post = request.form['posts']
        emp_house = request.form['house']
        emp_street = request.form['street']
        emp_place = request.form['place']
        emp_dis = request.form['dis']
        emp_pin = request.form['pin']
        emp_mob = request.form['mob']
        emp_gender = request.form['genter']
        emp_date = request.form['date1']
        emp_email = request.form['email1']
        dept = request.form['dept']
        photo = request.files['image1']
        data = datetime.datetime.now().strftime("%y%m%d-%H%M%S")
        photo.save(rpath + "static\\employee\\" + data + ".jpg")
        path = "static/employee/" + data + '.jpg'
        print(photo)
        pwd=random.randint(0000,9999)
        qry1=db.selectOne("select * from login where name='"+emp_email+"'")
        if qry1 is None:
            qry2 = "insert into login(name,passwd,type) values('" + emp_email + "','emp','employee')"
            res1 = db.insert(qry2)
            print(res1)
            qry = "insert into emp(emp_id,first_name,last_name,post,house,street,Place,district,pin_code,mob_no,email,gender,DOB,dept_id,photo,login_id) values('" + str(
                res1) + "','" + emp_name + "','" + emp_lastname + "','" + emp_post + "','" + emp_house + "','" + emp_street + "','" + emp_place + "','" + emp_dis + "','" + emp_pin + "','" + emp_mob + "','" + emp_email + "','" + emp_gender + "','" + emp_date + "','" + path + "','" + dept + "','" + str(
                res1) + "')"
            res = db.insert(qry)

            try:
                gmail = smtplib.SMTP('smtp.gmail.com', 587)

                gmail.ehlo()

                gmail.starttls()

                gmail.login('melbinkjoz@gmail.com', '123HipHop123')  # mail that send password

            except Exception as e:
                print("Couldn't setup email!!" + str(e))

            msg = MIMEText("Your Password is " + str(pwd))  # content

            msg['Subject'] = 'Verification'

            msg['To'] = emp_email

            msg['From'] = 'melbinkjoz@gmail.com'

            try:

                gmail.send_message(msg)

            except Exception as e:

                print("COULDN'T SEND EMAIL", str(e))

            return '<script> alert("success");window.location="/add_emp"</script>'
        else:
            return '<script> alert("The User Already Exsisting............");window.location="/add_emp"</script>'



    else:
        return redirect('/')

@app.route('/view_emp')
def view_emp():
    if session['lg'] == 'lin':
        db = Db()
        qry = "select * from emp"
        res = db.select(qry)
        return render_template("admin/view_emp.html", data=res)


    else:
        return redirect('/')


@app.route('/edit_emp/<i>')
def edit_emp(i):
    if session['lg'] == 'lin':
        qry = "select * from dept"
        res1 = db.select(qry)

        qry = "select * from emp where login_id='" + i + "'"
        res = db.selectOne(qry)
        return render_template("admin/edit_emp.html", i=res, data=res1)


    else:
        return redirect('/')


@app.route('/edit_emp_post/<i>',methods=['post'])
def edit_emp_post(i):
    if session['lg'] == 'lin':
        emp_name = request.form['name']
        emp_lastname = request.form['lastname']
        emp_post = request.form['post']
        emp_house = request.form['house']
        emp_street = request.form['street']
        emp_place = request.form['place']
        emp_dis = request.form['dis']
        emp_pin = request.form['pin']
        emp_mob = request.form['mob']
        emp_dept = request.form['dept']
        emp_gender = request.form['gender']
        # print(emp_gender)
        emp_date = request.form['date']
        emp_email = request.form['email']
        photo = request.files['image']
        ss = photo.filename
        if ss == '':
            qry = "update emp set first_name='" + emp_name + "',last_name='" + emp_lastname + "',post='" + emp_post + "',house='" + emp_house + "',street='" + emp_street + "',Place='" + emp_place + "',district='" + emp_dis + "',pin_code='" + emp_pin + "',mob_no='" + emp_mob + "',email='" + emp_email + "',gender='" + emp_gender + "',DOB='" + emp_date + "',dept_id='" + emp_dept + "' where emp_id='" + i + "'"
            res = db.update(qry)
        else:

            data = datetime.datetime.now().strftime("%y%m%d-%H%M%S")
            photo.save(rpath + "static\\employee\\" + data + ".jpg")
            path = "static/employee/" + data + '.jpg'
            print(path)
            qry = "update emp set first_name='" + emp_name + "',last_name='" + emp_lastname + "',post='" + emp_post + "',house='" + emp_house + "',street='" + emp_street + "',Place='" + emp_place + "',district='" + emp_dis + "',pin_code='" + emp_pin + "',mob_no='" + emp_mob + "',email='" + emp_email + "',gender='" + emp_gender + "',DOB='" + emp_date + "',dept_id='" + emp_dept + "',photo='" + path + "' where login_id='" + i + "'"
            res = db.update(qry)
        return view_emp()


    else:
        return redirect('/')



@app.route('/emp_dlt/<i>')
def emp_dlt(i):
    if session['lg'] == 'lin':
        qry = "delete from emp where login_id='" + i + "'"
        res = db.delete(qry)
        return view_emp()

    else:
        return redirect('/')


@app.route('/view_comp')
def view_comp():
    if session['lg'] == 'lin':
        qry = "select complaint.comp_id,complaint.emp_id,complaint.complaint1,complaint.cdate,emp.first_name,emp.photo,emp.last_name from emp inner join complaint  on complaint.emp_id=emp.login_id"
        res = db.select(qry)
        return render_template("admin/view_complaint.html", data=res)


    else:
        return redirect('/')


@app.route('/reply/<i>')
def reply(i):
    if session['lg'] == 'lin':
        return render_template("admin/reply_complaint.html", data=i)

    else:
        return redirect('/')



@app.route('/reply1',methods=["post"])
def reply1():
    if session['lg'] == 'lin':
        rp = request.form["textarea"]
        cid = request.form["cid"]
        qry = "update  complaint set  reply='" + rp + "',reply_date=now() where comp_id='" + cid + "' "
        res = db.update(qry)
        qry = "select complaint.comp_id,complaint.emp_id,complaint.complaint1,complaint.cdate,emp.first_name,emp.photo,emp.last_name from emp inner join complaint  on complaint.emp_id=emp.login_id"
        rs = db.select(qry)
        return '<script> alert("success");window.location="/reply"</script>'

    else:
        return redirect('/')


@app.route('/view_feedback')
def view_feedback():
    if session['lg'] == 'lin':
        qry = "select emp.first_name,emp.last_name,emp.photo,feedback.* from feedback inner join emp on emp.login_id=feedback.userid"
        res = db.select(qry)
        return render_template("admin/view_feedback.html", data=res)


    else:
        return redirect('/')


# ===============================================================================================
@app.route('/emp_home')
def emp_home():
    if session['lg'] == 'lin':
        return render_template("employee/emp_home.html")

    else:
        return redirect('/')



@app.route('/myprofile')
def myprofile():
    if session['lg'] == 'lin':
        id = session['lid']
        qry = "select * from emp,dept where dept.dept_id=emp.dept_id and  emp_id='" + str(id) + "'"
        print(id)
        res = db.selectOne(qry)
        return render_template("employee/profile.html", i=res)

    else:
        return redirect('/')

@app.route('/check_in',methods=['post'])
def check_in():
    if session['lg'] == 'lin':
        id = session['lid']
        btn = request.form['checkin1']
        if btn == 'CheckIn':
            qry2 = db.selectOne("select * from attendance where   emp_id='" + str(id) + "'  and adate=curdate()")
            if qry2 is None:
                qry = "insert into attendance(emp_id,checkin,adate,checkout) values('" + str(id) + "',now(),curdate(),'00:00:00')"
                res = db.insert(qry)
                return myprofile()
            else:
                return "<script>alert('Already check in.....');window.location='/myprofile'</script>"
        if btn == 'CheckOut':
            qry23 = db.selectOne(
                "select * from attendance where checkout='00:00:00' and  emp_id='" + str(id) + "'  and adate=curdate()")
            print('mmmmmmmmmmmmmmmmmmmmmmmmmm', qry23)
            if qry23 is not None:

                print("kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk")
                qry = "update  attendance set  checkout=now() where emp_id='" + str(id) + "' and adate=curdate()"
                res = db.update(qry)
                print(res)
                return myprofile()
            else:
                print("llllllllllllllllllllllllllll")
                return "<script>alert('Already check out.....');window.location='/myprofile'</script>"

    else:
        return redirect('/')

@app.route('/check_out',methods=['post'])
def check_out():
    if session['lg'] == 'lin':
        id = session['lid']
        qry1 = "select * from attendance where emp_id='" + str(id) + "' and adate=curdate()"
        d = db.selectOne(qry1)
        if d == None:
            print("please checkIn")
        else:
            qry = "update  attendance set  checkout=now() where emp_id='" + str(id) + "' and adate=curdate()"
            res = db.insert(qry)
        return render_template("employee/profile.html")

    else:
        return redirect('/')


# @app.route('/myprofile_post',methods=['post'])
# def myprofile_post():
#     att= request.form['in']
#     id = session['lid']
#     if att=='in':
#        qry="insert into attendance(emp_id,checkin,adate) values('"+str(id)+"',now(),curdate())"
#        res=db.insert(qry)
#     elif att=='out':
#        qry1 = "select * from attendance where emp_id='"+str(id)+"' and adate=curdate()"
#        d=db.select(qry1)
#        if d==None:
#            print("please checkIn")
#        else:
#            qry = "update  attendance set  checkout=now() where emp_id='"+str(id)+"' and adate=curdate()"
#            res = db.insert(qry)
#     else:
#         return emp_home()
#
#     return emp_home()

@app.route('/view_assign_work')
def view_assign_work():
    if session['lg'] == 'lin':
        db = Db();
        id = session['lid']
        # print(str(id)+"=================")
        qry = "select * from workassign,work where workassign.emp_id='" + str(
            id) + "' AND work.workid=workassign.workid"
        res = db.select(qry)
        return render_template("employee/view_assign_work.html", data=res)


    else:
        return redirect('/')


@app.route('/work_status')
def work_status():
    if session['lg'] == 'lin':
        id = session['lid']
        qry = "select distinct work.workid as id,work.w_work as nm from work_status,work where work.workid=work_status.work_id and emp_id='" + str(
            id) + "'"
        res = db.select(qry)
        return render_template("employee/work_status.html", data=res)


    else:
        return redirect('/')

@app.route('/work_status_post',methods=['post'])
def work_status_post():
    if session['lg'] == 'lin':
        workid = request.form["work"]
        status = request.form["status"]
        qry = "update work_status set status='" + workid + "',date=curdate() where work_id='" + workid + "'"
        res = db.update(qry)
        return '<script> alert("success");window.location="/work_status"</script>'
    else:
        return redirect('/')

@app.route('/file_sharing')
def file_sharing():
    if session['lg'] == 'lin':
        id = session['lid']
        qry = "select * from emp where login_id = '" + str(id) + "'"
        res = db.selectOne(qry)
        # print(qry)
        dept = res['dept_id']
        # print(dept)
        qry1 = "select * from emp where dept_id='" + str(dept) + "' and login_id!='" + str(id) + "'"
        # print(qry1)
        res1 = db.select(qry1)
        print(res1)
        return render_template("employee/file_sharing.html", data=res1)
    else:
        return redirect('/')

@app.route('/view_attendance')
def view_attendance():
    if session['lg'] == 'lin':
        id = session['lid']
        print(str(id) + "=================")
        qry = "select * from attendance where emp_id='" + str(id) + "'  "
        res = db.select(qry)
        return render_template("employee/view_attendance.html", data=res)


    else:
        return redirect('/')

@app.route('/send_leave_request')
def send_leave_request():
    if session['lg'] == 'lin':
        return render_template("employee/send_leave_request.html")

    else:
        return redirect('/')


@app.route('/leave_request_post',methods=['post'])
def leave_request_post():
    if session['lg'] == 'lin':
        dt = request.form['date']
        re = request.form['reason']
        id = session['lid']
        qry = "insert into leave1(emp_id,ldate,lreason) values('" + str(id) + "','" + dt + "','" + re + "')"
        res = db.insert(qry)
        return '<script> alert("success");window.location="/send_leave_request"</script>'


    else:
        return redirect('/')

@app.route('/send_workfile/<i>')
def send_workfile(i):
    if session['lg'] == 'lin':
        return render_template("employee/send_work.html", data=i)


    else:
        return redirect('/')

@app.route('/send_work_post/<i>',methods=['post'])
def send_work_post(i):
    if session['lg'] == 'lin':
        file = request.files['work']
        des = request.form['des']
        sts = request.form['sts']
        id = session['lid']
        data = datetime.datetime.now().strftime("%y%m%d-%H%M%S")
        file.save(rpath + "static\\employee\\" + data + file.filename)
        path = "static/employee/" + data + file.filename

        qry = "insert into file(ffile,description,fdate,workid,emp_id) values('" + path + "','" + des + "',curdate(),'" + i + "','" + str(
            id) + "') "
        res = db.insert(qry)

        qry = "insert into work_status values(null,'" + str(id) + "','" + i + "','" + sts + "',now()) "
        res = db.insert(qry)
        return '<script> alert("success");window.location="/send_workfile"</script>'


    else:
        return redirect('/')


@app.route('/share_files',methods=['post'])
def share_files():
    if session['lg'] == 'lin':
        files = request.files['work']
        rid = request.form['employee']
        lid = session['lid']
        qry = "select max(file_id) as max_id from fileshare"
        res = db.selectOne(qry)
        fid = 1
        if res:
            if res['max_id']:
                fid = res['max_id'] + 1

        pname1 = files.filename
        # print("//////", files)
        data = " "
        ext = str.split(files.filename, '.')
        print(ext[1])

        contentType = files.content_type
        files.save(rpath + "static\\file_shares\\" + str(fid) + "." + ext[1])

        hash = md5(rpath + "static\\file_shares\\" + str(fid) + "." + ext[1])
        # size = len(data)
        import os
        size = os.stat(rpath + "static\\file_shares\\" + str(fid) + "." + ext[1]).st_size
        # ======================================================================================================================

        filename = str(fid) + ".txt"
        buffersize = 64 * 1024
        password = "12345678910"
        pyAesCrypt.encryptFile(rpath + "static\\file_shares\\" + str(fid) + "." + ext[1],
                               rpath + "static\\file_enc\\" + filename, password, buffersize)
        # =======================================================================================================================

        acl = "public-read"
        s3 = boto3.client("s3",
                          aws_access_key_id="AKIA55LSJ44TTRI2WWSZ",
                          aws_secret_access_key="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")
        m = s3.list_buckets()
        print(m)
        s3.upload_file(rpath + "static\\file_enc\\" + filename, 'keylog1', filename)
        # =======================================================================================================================

        qry12 = "insert into fileshare values(null,'" + pname1 + "','" + filename + "','" + str(
            lid) + "','" + rid + "',now(),'" + hash + "','" + str(size) + "')"
        db.insert(qry12)

        return ''' <script> alert("Upload successfull"); window.location='/view_sendfile' </script>  '''
    else:
        return redirect('/')

def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

@app.route('/view_revfile')
def view_revfile():
    db=Db()
    if session['lg'] == 'lin':
        id = session['lid']
        qry = "select * from fileshare,emp where emp_id=send_id and rec_id='" + str(id) + "'"
        res = db.select(qry)
        return render_template("employee/view_rev.html", data=res)

    else:
        return redirect('/')


@app.route('/view_sendfile')
def view_sendfile():
    if session['lg'] == 'lin':
        id = session['lid']
        qry = "select * from fileshare,emp where emp_id=send_id and send_id='" + str(id) + "'"
        res = db.select(qry)
        return render_template("employee/view_send.html", data=res)

    else:
        return redirect('/')


@app.route('/my_downfile/<i>/<j>')
def my_downfile(i,j):
    if session['lg'] == 'lin':
        id = session['lid']
        # qry = "select * from fileshare where send_id='" + str(id) + "'"
        qry = "select * from fileshare where file_id='" + str(j) + "'"
        res = db.selectOne(qry)

        if res is not None:
            session['cfile']=i
            session['dfile']=res["fname"]
            session['hash']=res["hashvalue"]
            session['tp']="send"

            return redirect("/qr")
        else:
            return redirect('/')
    else:
        return redirect('/')


@app.route('/rec_downfile/<i>/<j>')
def rec_downfile(i,j):
    if session['lg'] == 'lin':
        id = session['lid']
        # qry = "select * from fileshare where rec_id='" + str(id) + "'"
        qry = "select * from fileshare where file_id='" + str(j) + "'"
        res = db.selectOne(qry)

        if res is not None:
            print("innnnnnnnnn")
            session['cfile'] = i
            session['dfile'] = res["fname"]
            session['hash'] = res["hashvalue"]
            session['tp'] = "rec"

            return redirect("/qr")
        else:
            return redirect('/')
    else:
        return redirect('/')

def downfilCloud():
    i=session['cfile']
    fname=session['dfile']
    hashvalue=session['hash']

    print("innnnnnnnnn")
    s3 = boto3.client("s3",
                      aws_access_key_id="AKIA55LSJ44TTRI2WWSZ",
                      aws_secret_access_key="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")
    BUCKET_NAME = 'keylog1'
    KEY = i
    print("haiiii")
    print(".....", KEY)

    dpth = rpath + "static\\file_cld\\" + i;
    s3.download_file(BUCKET_NAME, i, dpth)

    # ================================================================================================
    buffersize = 64 * 1024
    password = "12345678910"
    pyAesCrypt.decryptFile(dpth, rpath + "static\\file_dec\\" + fname, password, buffersize)
    # ================================================================================================

    hash = md5(rpath + "static\\file_dec\\" + fname)
    # size = len(data)
    import os
    size = os.stat(rpath + "static\\file_dec\\" + fname).st_size

    if hash == hashvalue:
        print("no corruption")
        return "ok"
    else:
        print("failed")
        return "failed"

#
# @app.route('/rec_downfile/<i>/<j>')
# def rec_downfile(i,j):
#     if session['lg'] == 'lin':
#         id = session['lid']
#         qry = "select * from fileshare where rec_id='" + str(id) + "'"
#         res = db.selectOne(qry)
#
#         if res is not None:
#             print("innnnnnnnnn")
#             s3 = boto3.client("s3",
#                               aws_access_key_id="AKIA55LSJ44TTRI2WWSZ",
#                               aws_secret_access_key="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")
#             BUCKET_NAME = 'keylog1'
#             KEY = i
#             print("haiiii")
#             print(".....", KEY)
#
#             dpth = rpath + "static\\file_cld\\" + i;
#             s3.download_file(BUCKET_NAME, i, dpth)
#
#             # ================================================================================================
#             buffersize = 64 * 1024
#             password = "12345678910"
#             pyAesCrypt.decryptFile(dpth, rpath + "static\\file_dec\\" + res["fname"], password, buffersize)
#             # ================================================================================================
#
#             hash = md5(rpath + "static\\file_dec\\" + res["fname"])
#             # size = len(data)
#             import os
#             size = os.stat(rpath + "static\\file_dec\\" + res["fname"]).st_size
#
#             if hash == res["hashvalue"]:
#                 print("no corruption")
#             else:
#                 print("failed")
#
#         return render_template("employee/view_send.html", data=res)
#
#     else:
#         return redirect('/')
#

@app.route('/view_leave_request')
def view_leave_request():
    if session['lg'] == 'lin':
        id = session['lid']
        print(str(id) + "=================")
        qry = "select * from leave1 where emp_id='" + str(id) + "'  "
        res = db.select(qry)
        return render_template("employee/view_leave.html", data=res)

    else:
        return redirect('/')


@app.route('/send_complaint')
def send_complaint():
    if session['lg'] == 'lin':
        return render_template("employee/send_complaint.html")

    else:
        return redirect('/')


@app.route('/send_comp_post',methods=['post'])
def send_comp_post():
    if session['lg'] == 'lin':
        id = session['lid']
        com = request.form['complaint']
        qry = "insert into complaint (emp_id,complaint1,cdate) values('" + str(id) + "','" + com + "',curdate())"
        res = db.insert(qry)
        return '<scirpt>alert("Send")</script>'


    else:
        return redirect('/')

@app.route('/view_comp1')
def view_comp1():
    if session['lg'] == 'lin':
        id = session['lid']
        print(str(id) + "=================")
        qry = "select * from complaint where emp_id='" + str(id) + "'  "
        res = db.select(qry)
        return render_template("employee/view_complaints.html", data=res)


    else:
        return redirect('/')


@app.route('/send_feedback/<a>')
def send_feedback(a):
    if session['lg'] == 'lin':
        return render_template("employee/send_feedback.html", data=a)

    else:
        return redirect('/')


@app.route('/send_feedback_post/<i>',methods=['post'])
def send_feedback_post(i):
    if session['lg'] == 'lin':

        db = Db()
        feedback = request.form['feedback']
        # date=datetime.datetime.now()
        id = session['lid']
        qry = "insert into feedback(ftype,fdate,userid,workid) values('" + feedback + "',curdate(),'" + str(
            id) + "','" + i + "')"
        res = db.insert(qry)
        return '<script> alert("send");</script>'


    else:
        return redirect('/')

@app.route('/emp_edit_work')
def emp_edit_work():
    if session['lg'] == 'lin':
        return render_template("employee/edit_work.html")

    else:
        return redirect('/')






##-----------------------------------------------------------------------------------------

@app.route('/dep_home')
def dep_home():
    if session['lg'] == 'lin':
        return render_template("department/view_dep_profile.html")
    else:
        return redirect('/')



@app.route('/dep_home_view')
def dep_home_view():
    if session['lg'] == 'lin':
        db = Db()
        lid = session['lid']
        qry = "select * from emp where dept_id='" + str(lid) + "'"
        res = db.select(qry)
        return render_template("department/dep_profile.html", data=res)


    else:
        return redirect('/')


@app.route('/dep_assign_work')
def dep_assign_work():
    if session['lg'] == 'lin':
        lid = session['lid']
        qry = "select * from work where dep_id='" + str(lid) + "'"
        res = db.select(qry)
        print(lid)
        return render_template("department/dep_assign_work.html", data=res)


    else:
        return redirect('/')


@app.route('/dep_status')
def dep_status():
    if session['lg'] == 'lin':
        return render_template("department/dep_status.html")


    else:
        return redirect('/')


@app.route('/leave_status')
def leave_status():
    if session['lg'] == 'lin':
        lid = session['lid']
        qry = "select * from leave1,emp where leave1.emp_id=emp.emp_id and emp.dept_id='" + str(lid) + "'"
        print(lid)
        res = db.select(qry)
        return render_template("department/leave_status.html", data=res)


    else:
        return redirect('/')

@app.route('/leave_approve/<n>')
def leave_approve(n):
    if session['lg'] == 'lin':
        qry = "update leave1 set lstatus='approved' where emp_id='" + n + "'"
        res = db.update(qry)
        return '<script> alert("Set");window.location="/leave_status"</script>'


    else:
        return redirect('/')

@app.route('/leave_reject/<n>')
def leave_reject(n):
    if session['lg'] == 'lin':
        qry = "update leave1 set lstatus='reject' where emp_id='" + n + "'"
        res = db.update(qry)
        return '<script> alert("Set");window.location="/leave_status"</script>'


    else:
        return redirect('/')

@app.route('/date')
def date():
    if session['lg'] == 'lin':
        lid = session['lid']

        qry = db.select('select * from attendance,emp where attendance.emp_id=emp.emp_id and emp.dept_id="' + str(
            lid) + '" order by adate')
        print(qry)
        return render_template('department/date.html', data=qry)


    else:
        return redirect('/')


@app.route('/view_emp_attend',methods=['post'])
def view_emp_attend():
    if session['lg'] == 'lin':
        lid = session['lid']
        adate = request.form['date']
        qry = db.select(
            'select * from attendance,emp where attendance.emp_id=emp.emp_id and adate="' + adate + '"and emp.dept_id="' + str(
                lid) + '" order by adate')
        return render_template("department/date.html", data=qry)


    else:
        return redirect('/')

@app.route('/work_assign/<n>')
def work_assign(n):
    if session['lg'] == 'lin':
        lid = session['lid']
        work_id = n;
        print(work_id)
        qry = "select * from emp where dept_id='" + str(lid) + "'"
        res = db.select(qry)
        return render_template("department/emp_display.html", data=res, wid=n)


    else:
        return redirect('/')

@app.route('/work_assiqn_post/<id>',methods=['post'])
def work_assiqn_post(id):
    if session['lg'] == 'lin':
        emp_id = request.form['emp']
        qry = "insert into workassign(workid,emp_id,date) values('" + id + "','" + emp_id + "',curdate())"
        res = db.insert(qry)
        return '<script> alert("Success");window.location="/dep_assign_work"</script>'


    else:
        return redirect('/')


@app.route('/work_view')
def work_view():
    if session['lg'] == 'lin':
        lid = session['lid']
        print(str(lid))
        qry = db.select("select * from emp where dept_id='"+str(lid)+"'")
        # print('mmmm', qry)
        return render_template('department/view_work.html', data1=qry)


    else:
        return redirect('/')

@app.route('/view_work_emp',methods=['post'])
def view_work_emp():
    if session['lg'] == 'lin':
        lid = session['lid']
        empid = request.form['emp']
        print(empid)
        qry = db.select("select * from file where emp_id='"+str(empid)+"'")
        return render_template("department/view_work.html", data=qry)


    else:
        return redirect('/')


# @app.route('/dep_assign_work')
# def dep_assign_work():
#     return render_template("department/assign_work.html")











@app.route('/file_sharing1')
def file_sharing1():
    if session['lg'] == 'lin':
        id = session['lid']
        # qry = "select * from emp where login_id = '" + str(id) + "'"
        # res = db.selectOne(qry)
        # print(qry)
        # dept = res['dept_id']
        # print(dept)
        qry1 = "select * from emp where dept_id='" + str(id) + "'"
        # print(qry1)
        res1 = db.select(qry1)
        print(res1)
        return render_template("department/file_sharing.html", data=res1)
    else:
        return redirect('/')




@app.route('/share_files1',methods=['post'])
def share_files1():
    if session['lg'] == 'lin':
        files = request.files['work'] #wid
        rid = request.form['employee'] #empip
        lid = session['lid'] #depid
        qry = "select max(file_id) as max_id from file"
        res = db.selectOne(qry)
        fid = 1
        if res:
            if res['max_id']:
                fid = res['max_id'] + 1

        pname1 = files.filename #filename
        print("//////", files)
        data = " "
        ext = str.split(files.filename, '.')
        print("nnnn",ext[1])

        contentType = files.content_type
        files.save(rpath + "static\\file_shares\\" + str(fid) + "." + ext[1])

        hash = md5(rpath + "static\\file_shares\\" + str(fid) + "." + ext[1])
        # size = len(data)
        import os
        size = os.stat(rpath + "static\\file_shares\\" + str(fid) + "." + ext[1]).st_size
        # ======================================================================================================================

        filename = "x_"+str(fid) + ".txt"
        buffersize = 64 * 1024
        password = "12345678910"
        pyAesCrypt.encryptFile(rpath + "static\\file_shares\\" + str(fid) + "." + ext[1],
                               rpath + "static\\file_enc\\" + filename, password, buffersize)
        # =======================================================================================================================

        acl = "public-read"
        s3 = boto3.client("s3",
                          aws_access_key_id="AKIA55LSJ44TTRI2WWSZ",
                          aws_secret_access_key="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")
        m = s3.list_buckets()
        print(m)
        s3.upload_file(rpath + "static\\file_enc\\" + filename, 'keylog1', filename)
        # =======================================================================================================================

        qry12 = "insert into file values(null,'" + pname1 + "','curdate()','" + rid + "','" + hash + "','"+filename+"','" + str(size) + "','"+str(lid)+"')"
        db.insert(qry12)

        return ''' <script> alert("Upload successfull"); window.location='/view_sendfile' </script>  '''
    else:
        return redirect('/')



@app.route('/rec_downfile1/<i>/<j>')
def rec_downfile1(i,j):
    if session['lg'] == 'lin':
        id = session['lid']
        # qry = "select * from fileshare where rec_id='" + str(id) + "'"
        qry = "select * from file where file_id='" + str(j) + "'"
        res = db.selectOne(qry)

        if res is not None:
            print("rec____doww")
            session['cfile'] = i
            session['dfile'] = res["ffile"]
            session['hash'] = res["hashvalue"]
            session['tp'] = "work"

            return redirect("/qr")
        else:
            return redirect('/')
    else:
        return redirect('/')







if __name__ == '__main__':
    app.run(debug=True)
