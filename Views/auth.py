from flask import jsonify,request,Blueprint 
from models import db,User, Staff
from werkzeug.security import check_password_hash
from flask_jwt_extended import create_access_token,jwt_required, get_jwt_identity

#blueprint
auth_bp = Blueprint('auth_bp', __name__)

#Login User 
@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data["email"]
    password = data["password"]
    
    #check if the user with the email exist (if)
    user = User.query.filter_by(email= email).first()
    
    if user and check_password_hash(user.password,password):
        access_token = create_access_token(identity=user.id)
        
        return jsonify({"access_token":access_token}), 200
        
    # pass an error
    else: 
        return jsonify({"Error":"What is going on? "}), 404
    
    
#get the current user functions
@auth_bp.route('/current_user', methods = ['GET'])
@jwt_required()
def current_user():
    current_user_id = get_jwt_identity()
    print(current_user_id)
    #fetch the user
    user = User.query.get(current_user_id)
    
    #get the user data object 
    user_data = [{"id": user.id,
                "username":user.username,
                "email":user.email, 
                "is_approved":user.is_approved}]
    
    return jsonify(user_data)


# #Login Staff 
# @auth_bp.route('/staff', methods=['POST'])
# def login():
#     data = request.get_json()
#     email = data["email"]
#     password = data["password"]
    
#     #check if the staff with the email exist (if)
#     staff = Staff.query.filter_by(email= email).first()
    
#     if staff and check_password_hash(staff.password, password):
#         access_token = create_access_token(identity= str(staff.id))
        
#         return jsonify({"access_token":access_token}), 208
        
#     # pass an error
#     else: 
#         return jsonify({"Error":"Email/password is incorrect"}), 404
    
# #get the current user functions
# @auth_bp.route('/current_staff', methods = ['GET'])
# @jwt_required()
# def current_staff():
#     current_staff_id = get_jwt_identity()
    
#     #fetch the user
#     staff = Staff.query.get(current_staff_id)
    
#     #get the user data object 
#     staff_data = [{"id": staff.id,
#                 "staff_name":staff.staff_name,
#                 "email":staff.email, 
#                 "department":staff.department}]
    
#     return jsonify({"Current_staff": staff_data})
    
    
    
# #Logout
