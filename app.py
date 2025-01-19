from flask import Flask, jsonify, request 
from flask_migrate import Migrate
from models import User,Staff,Feed, db

#create a flask class 
app = Flask(__name__)

# #create a migration. config parameters
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///customer.db'

# #initialize the router 
migrate = Migrate(app,db)
db.init_app(app)

#import all the functions in views 
from Views import * 

#register the blueprints 
app.register_blueprint(user_bp)
app.register_blueprint(feed_bp)
app.register_blueprint(staff_bp)

@app.route('/')
def index(): 
    return jsonify("<h1> Customer Service Management System </h1>")



