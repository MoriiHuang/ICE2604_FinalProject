from flask import Flask,render_template,request,redirect,url_for
import pymysql
import json
import requests
app=Flask(__name__)
app.jinja_env.variable_start_string = '{['
app.jinja_env.variable_end_string = ']}'
@app.route('/')
def vue():
    return render_template('final_project1.html')
app.run(host='0.0.0.0',debug=True);