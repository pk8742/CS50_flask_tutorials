# app.py
# python file to create database

from flask import Flask, render_template, request
from models import * # our file defined above to define the classes/tables

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://postgres:pk8742@localhost:5432/airline2'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app) # tie this database with this flask application

def main():
  db.create_all()

if __name__ == "__main__":
  with app.app_context(): # we need this to properly interact with flask-application
    main()
