from flask import Flask, jsonify, 
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///customers.db'



db = SQLAlchemy()
migrate = Migrate(app, db)
