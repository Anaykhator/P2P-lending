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
        return render_template('home.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    # if request.method == 'POST':
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
        return sorry("invalid username and/or password")
    return sorry("Successful")
        # db = SQL("sqlite:///P2P.db")
        # db.execute("INSERT INTO users VALUES('"+name+"','"+userid+"','"+passw+"','"+type+"','"+email+"','"+phone+"','"+aadhaar+"','"+pan+"','"+dob+"','"+ac+"','"+ifsc+"')")

def sorry(message):
    flash(message)
    return render_template("sorry.html")
