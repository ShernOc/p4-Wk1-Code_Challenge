from flask import jsonify,request,Blueprint 
from datetime import datetime
from models import db,User
from werkzeug.security import check_password_hash
from flask_jwt_extended import create_access_token,jwt_required, get_jwt_identity

#blueprint
auth_bp = Blueprint('auth_bp', __name__)


#Login
@auth_bp.route('/login', methods = ['POST'])
def login():
    data = request.get_json()
    username = data["username"]
    password = data["password"]
    
    #check if the user with the email exist 
    user = User.query.filter_by(email = email).first()
    
    if user and check_password_hash(user.password,password):
        access_token = create_access_token(identity=user.id)
        return jsonify({"access_token":access_token})
        
    else: 
        return jsonify({"Error":"User/Email is incorrect"}), 404
    
    #get the current user
@auth_bp.route('/current_user', methods = ['GET'])
def current_user():
    current_user_id = get_jwt_identity()
    user = User.query.get(current_user_id)
    
    #get the user data 
    user_data = [{"id": user.id,
                "username":user.username,
                "email":user.email, 
                "is_approved":user.is_approved}]
    return jsonify({"Current_user": user_data})
    

#Logout
