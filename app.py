from flask import Flask, request, render_template, redirect, flash, session, g
from flask_mysqldb import MySQL

app = Flask(__name__)
mysql = MySQL(app)

@app.route('/')
def home():
    return render_template('home.html')