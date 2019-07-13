from flask import Flask, request, render_template, redirect, flash, session
from flask_mysqldb import MySQL

app = Flask(__name__)
mysql = MySQL(app)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        det = request.form
        id = det['id']
        p = det['pass']


@app.route('/borrowersignup')
def borsign():
    return render_template('borSign.html')


@app.route('/lendersignup')
def lensign():
    return render_template('lendSign.html')