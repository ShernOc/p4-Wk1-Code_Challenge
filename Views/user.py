from flask import jsonify,request,Blueprint
from models import User,db
from werkzeug.security import generate_password_hash
from flask_jwt_extended import jwt_required, get_jwt_identity

#blueprint
user_bp = Blueprint('user_bp', __name__)

#Fetch/Get Users 
@user_bp.route('/users')
@jwt_required()
def get_users():
    current_user_id = get_jwt_identity()
    #get the users 
    users = User.query.filter_by(user_id = current_user_id).first()
    #create an empty list to store the users
    user_list = []
    
    #create a loop that will loop through users 
    for user in users: 
        #in the append pass it as an json objects
        user_list.append({
            "id": user.id,
            "username":user.username,
            "email":user.email,
            "phone_number":user.phone_number,
            #fetch user based on there feedback 
            "feed":[
                {
                    "id":feed.id,
                    "title":feed.title,
                    "description":feed.description,
    
                } for feed in user.feed
            ] 
        })
        
    return jsonify(user_list)

#Add a users 
@user_bp.route('/users', methods=["POST"])
def add_users():
    data = request.get_json()
    username =data['username']
    email = data['email']
    phone_number= data['phone_number']
    password = generate_password_hash(data['password'])
    
#3. Check if the users exists
    check_username = User.query.filter_by(username=username).first() 
    check_email= User.query.filter_by(email=email).first()

    #prints the output 
    print("Username", check_username)
    print("Email", check_email)
    
    #check and create errors
    if check_username or check_email: 
        return jsonify({"error":"username/email already exist"}),406
    
    else: 
        new_user = User(
        username = username, 
        email = email,
        password = password,
        phone_number = phone_number )
        
        #call the function 
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"Success": "Users added successfully"})

#UPDATE USER: 

@user_bp.route('/users/<user_id>', methods= ["PATCH"])
@jwt_required()
def update_username(user_id):
    current_user_id = get_jwt_identity()
    #check if user exist
    user = User.query.get(user_id)
    
    if user and user.user_id== current_user_id: # if user exist
        #get the data 
        data = request.get_json()
        username = data.get('username' , user.username)
        email = data.get('email', user.email)
        phone_number = data.get('phone_number', user.phone_number)
        password = data.get('password', user.password)
    
    #continue to check 
        check_username = User.query.filter_by(username=username and id!=user.id).first()
        check_email = User.query.filter_by(email = email and id!=user.id).first()
       
        if check_username or check_email:
            return jsonify({"error": "Username/Email already exist"}), 406
         
        else: 
            user.username = username
            user.email = email
            user.password = password 
            user.phone_number = phone_number
        
        #Just commit no adding. 
            db.session.commit()
            return jsonify({"Success": "Users updated successfully"}), 201
#if the user does not exist? 
    else:
        return jsonify({"error": "User does not exist"}), 406
    
#fetch one User based on id 
@user_bp.route('/users/<int:id>')
@jwt_required()
def fetch_one_user(id):
    current_user_id = get_jwt_identity()
    user= User.query.filter_by(id, user_id = current_user_id).first()
    
    if user:
        return jsonify({
            "id":user.id,
            "username":user.username,
            "email":user.email,
            "phone_number":user.phone_number,
            "password":user.password
        })
    else: 
        return jsonify({"Error":"User doesn't exist"})
    
#Delete Users 
@user_bp.route('/users/<int:user_id>', methods=['DELETE'])
@jwt_required()
def delete_user(user_id):
    #get the users
    current_user_id = get_jwt_identity()
    user = User.query.filter_by(id = user_id, user_id= current_user_id)
    
    if user:
        db.session.delete(user)
        db.session.commit()
        return jsonify({"Success":"User Deleted Successfully"})

    else:
        return jsonify({"Error": "User does not exist"})
     
     
