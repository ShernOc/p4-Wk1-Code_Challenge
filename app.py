from flask import Flask, jsonify, request 
from flask_migrate import Migrate
from models import db
from flask_jwt_extended import JWTManager
from datetime import timedelta
from flask_mail import Mail,Message


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



# Mail Credentials 
# SMTP credentials
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'sherlyne.ochieng@student.moringaschool.com'
app.config['MAIL_DEFAULT_SENDER'] = 'sherlyne.ochieng@student.moringaschool.com'
app.config['MAIL_PASSWORD'] = 'slim hbpc dwit bsli'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

#initialize 
mail = Mail(app)

#create an instance of Message 
@app.route('/send_email')
def email():
    try: 
        msg = Message(
        subject = "First Email!",
        sender = ['MAIL_DEFAULT_SENDER'],
        recipients= ["sherlynea8622@gmail.com","sherlyne.ochieng@student.moringaschool.com","david.kakhayanga@student.moringaschool.com" ],
        #What the message body will send
        body = "Did you get the email, Lol Hope You did : Flask Application")
        
        mail.send(msg)
        return jsonify({"Success": "Message sent Successfully"
            })

    except Exception as e: 
        return jsonify({"Error" :"Message sent Successfully"})

#run the app.py 
if __name__ == '__main__':
    app.run(debug=True, port= 5555)
    
    





