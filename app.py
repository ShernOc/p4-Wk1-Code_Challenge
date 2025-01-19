from flask import Flask, jsonify, request 
from flask_migrate import Migrate
from models import User,Staff,Feed, db

#create a flask class 
app = Flask(__name__)

# #create a migration. config parameters
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///customer.db'