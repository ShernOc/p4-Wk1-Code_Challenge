from flask import jsonify,request,Blueprint
from models import db,User

#blueprint
user_bp = Blueprint('user_bp', __name__)

#Fetch/Get Users 
@user_bp.route('/users')
def get_users():
    #get the users 
    users = User.query.all()
    #create an empty list to store the users
    user_list = []
    
    #create a loop that will loop through users 
    for user in users: 
        #in the append pass it as an json objects
        user_list.append({
            "id": user.id,
            "username":user.username,
            "email":user.email,
            "phone_number":user.is_approved, 
        })
    return jsonify(user_list)

#Add a users 
@user_bp.route('/users', methods=["POST"])
def add_users():
    data = request.get_json() # This is an object in json 
    username = data['username']
    email = data['email']
    phone_number= data['phone_number']
    password = data['password']
    
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
        new_user = User(username = username, email = email,
        password = password,
        phone_number = phone_number )
        
        #call the function 
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"Success": "Users added successfully"})

#UPDATE USER: 
#you can update the name, password,email .. 
@user_bp.route('/users/<user_id>', methods= ["PATCH"])
def update_username(user_id):
    #check if user exist
    user = User.query.get(user_id)
    
    if user: # if user exist
        #get the data 
        data = request.get_json()
        username = data['username']
        email = data['email']
        phone_number = data['phone_number']
        password = data['password']
    
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
def fetch_one_user(id):
    user= User.query.get(id)
    
    if user:
        return jsonify({
            "id":user.id,
            "username":user.username,
            "email":user.email,
            "phone_number":user.is_complete,
            "password":user.password
        })
    else: 
        return jsonify({"Error":"User doesn't exist"})
    
#Delete Users 
user_bp.route('/users/<int:user_id>',methods=['DELETE'])
           
def delete_user(user_id):
    #get the users
    user = User.query.get(user_id)
    
    if user:
        db.session.delete(user)
        db.session.commit()
        return jsonify({"Success":"User Deleted Successfully"})

    else:
         return jsonify({"Error": "User does not exist"})
     
     
