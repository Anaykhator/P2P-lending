from flask import Flask, request, render_template, redirect, flash, session
from cs50 import SQL

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('signup.html')
    elif request.method == 'POST':
        det = request.form
        id = det['id']
        p = det['pass']
        # curr = mysql.connection.cursor()
        # resultSet = curr.execute("SELECT * FROM login WHERE id='" + id + "'")
        # if resultSet == 1:
        #     ad = curr.fetchall()
        #     if ad[0][2] == p:
        #         if ad[0][3] == 'b':
        #             return redirect("/borDash")
        #         elif ad[0][3] == 'l':
        #             return redirect("/lenDash")
        #     else:
        #         flash("Passwords do not match", "danger")
        #         return redirect("/home")
        return render_template('home.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        data = request.form
        name = data['name']
        phone = data['phone']
        email = data['email']
        aadhaar = data['aadhaar']
        pan = data['pan']
        dob = data['dob']
        ac = data['ac']
        ifsc = data['ifsc']
        userid = data['id']
        passw = data['pass']
        repass = data['repass']
        type = data['mode']
        if passw != repass:
            return('Passwords did not match')
        db = SQL("sqlite:///P2P.db")
        db.execute("INSERT INTO users VALUES("+name+", "+id+", "+passw+", "+type+", "+email+", "+phone+", "+aadhaar+", "+pan+", "+dob+", "+ac+", "+ifsc+")")