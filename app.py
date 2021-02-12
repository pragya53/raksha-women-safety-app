from flask import Flask,render_template,request,redirect,session
import mysql.connector
import os
import sms

app = Flask(__name__)

app.secret_key=os.urandom(24)

conn = mysql.connector.connect(
    host="sql12.freesqldatabase.com",
    user="",
    password="",
    database=""
)

cursor=conn.cursor()

@app.route('/')
def login():    
    return render_template('login.html')

@app.route('/login_validation', methods=['POST'])
def login_validation():
    uemail = request.form.get('uemail')
    upassword = request.form.get('upassword') 
    cursor.execute("""SELECT * FROM `users` WHERE `email` LIKE '{}' AND `password` LIKE '{}'""".format(uemail,upassword))    
    users = cursor.fetchall()
    if len(users)>0:
        session['userid'] = users[0][0]
        return redirect('/home')
    else:
        return redirect('/')


@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/add_user', methods=['POST'])
def add_user():
    name = request.form.get('uname')
    email = request.form.get('uemail')
    phone = request.form.get('uphone')
    ec1 = request.form.get('ec1')
    ec2 = request.form.get('ec2')
    password = request.form.get('upassword')

    cursor.execute("""INSERT INTO `users` (`userid`,`name`,`email`,`phone`,`ec1`,`ec2`,`password`) VALUES (NULL,'{}','{}','{}','{}','{}','{}')""".format(name,email,phone,ec1,ec2,password))
    conn.commit()

    cursor.execute("""SELECT * FROM `users` WHERE `email` LIKE '{}'""".format(email))
    myuser = cursor.fetchall()
    session['userid']=myuser[0][0]

    return redirect("/home")

@app.route('/home')
def home():
    if 'userid' in session:
        return render_template('index.html')
    else:
        return redirect('/')

@app.route('/logout')
def logout():
    session.pop('userid')
    return redirect('/')

@app.route('/sendsms')
def sos():
    if 'userid' in session:
        
        userid = session.get('userid')
        cursor.execute("""SELECT `name` FROM `users` WHERE `userid` = '{}'""".format(userid))
        name = cursor.fetchall()
        name = name[0][0]
        cursor.execute("""SELECT `ec1` FROM `users` WHERE `userid` = '{}'""".format(userid))
        ec1 = cursor.fetchall()
        number1 = ec1[0][0]
        cursor.execute("""SELECT `ec2` FROM `users` WHERE `userid` = '{}'""".format(userid))
        ec2 = cursor.fetchall()
        number2 = ec2[0][0]
        #print(number1)
        sms.sendSMS(number1,number2,name)
        #sms.sendSMS(number2,name)
        return redirect('/home')

    else:
        print('failed')

if __name__=="__main__":
    app.run(debug=True)
