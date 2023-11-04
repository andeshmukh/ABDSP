from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate  

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello world"
  
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True )