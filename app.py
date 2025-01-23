from flask import Flask, jsonify, request 
from flask_migrate import Migrate
from models import db
from flask_jwt_extended import JWTManager
from datetime import timedelta
from flask_mail import Mail


#create a flask class 
app = Flask(__name__)

# #create a migration. config parameters
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///customer.db'

# #initialize the router 
migrate = Migrate(app,db)
db.init_app(app)

#import all the functions in views 
from Views import * 

#register all the  blueprints 
app.register_blueprint(user_bp)
app.register_blueprint(feed_bp)
app.register_blueprint(staff_bp)
app.register_blueprint(auth_bp)


@app.route('/')
def index(): 
    return ("<h1> Customer Service Management System </h1>")


#Authentication
app.config["JWT_SECRET_KEY"] = "Sherlyne-23456"  # Change this!
#Toke Expire in 2 hours 
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=2)

jwt = JWTManager(app)
jwt.init_app(app)




#Mail Credentials 
 
# # SMTP credentials
# app.config['MAIL_SERVER'] = 'smtp.gmail.com'
# app.config['MAIL_PORT'] = 587
# app.config['MAIL_USERNAME'] = 'sherlyne.ochieng@student.moringaschool.com'
# app.config['MAIL_PASSWORD'] = 'slim hbpc dwit bsli'
# app.config['MAIL_USE_TLS'] = True
# app.config['MAIL_USE_SSL'] = False

# mail = Mail(app)

# #create an instance of Message 
# @app.route('/')
# def email():
#     msg = Message(
#     subject = "First Email!",
#     sender = "sherlyne.ochieng@student.moringaschool.com",
#     recipients= ["sherlynea8622@gmail.com","ashley.natasha1@student.moringaschool.com", "antony.wambugu@student.moringaschool.com", "abdimalik.omar1@student.moringaschool.com" ],
#     #What the message body will send
#     body = "Hello,this is the first Flask email from the flask app. GROUP6")
#     mail.send(msg)
#     return "Message sent Successfully"

#     except 

# if __name__ == '__main__':
#     app.run(debug=True)
    
    





