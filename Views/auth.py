from flask import jsonify,request,Blueprint 
from datetime import datetime
from models import db,User

#blueprint
auth_bp = Blueprint('auth_bp', __name__)


#Login
@auth_bp.route('/signin')
def login():
    data = request.get_json()
    email = data["email"]
    password = data["password"]
    
    #check if the user with the email exist 
    
    user = User.query.filter_by(email = email).first()
    
    if user:
        pass 
    else: 
        return jsonify({"Error":"User does not exist"})
    




#Logout
