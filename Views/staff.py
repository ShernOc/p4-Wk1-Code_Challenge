from flask import jsonify,request,Blueprint
from models import db,Staff
from flask_jwt_extended import jwt_required, get_jwt_identity
from  flask_mail import Mail 

#blueprint
staff_bp = Blueprint('staff_bp', __name__)

#Fetch/Get Staff  
@staff_bp.route('/staffs')
@jwt_required()
def get_staff():
    current_user_id = get_jwt_identity()
    #get the staffs 
    staffs = Staff.query.filter_by(staff_id=current_user_id)
    # empty list to store the staffs
    staff_list = []
    for staff in staffs: 
        #in the append pass it as an json objects
        staff_list.append({
            "id": staff.id,
            "staff_name":staff.staff_name,
            "is_admin":staff.is_admin,
            "email":staff.email, 
            "department":staff.department,
            "password":staff.password
        })
    return jsonify(staff_list)


#Add a staffs 
@staff_bp.route('/staffs', methods=["POST"])
@jwt_required()
def add_staff():
    data = request.get_json() # This is an object in json 
    staff_name = data['staff_name']
    email = data['email']
    department= data['department']
    password = data['password']
    
#3. Check if the staffs exists
    check_staff_name = Staff.query.filter_by(staff_name=staff_name).first() 
    check_email= Staff.query.filter_by(email=email).first()

    #prints the output 
    print("Name", check_staff_name)
    print("Email", check_email)
    
    #check and create errors
    if check_staff_name or check_email:
        return jsonify({"error":"staff_name/email already exist"}),406
    else: 
        new_staff = Staff(staff_name = staff_name, email = email,
        department = department, password = password)
        #call the function 
        db.session.add(new_staff)
        db.session.commit()
        return jsonify({"Success": "Staff added successfully"})

#UPDATE USER: 

@staff_bp.route('/staffs/<staff_id>', methods= ["PATCH"])
@jwt_required()
def update_staff_name(staff_id):
    #check if staff exist
    current_user_id = get_jwt_identity()
    staff = Staff.query.filter_by(staff_id, user_id = current_user_id)
    
    if staff : 
        data = request.get_json()
        staff_name = data.get('staff_name', staff.staff_name)
        email = data.get('email', staff.email)
        department = data.get('department', staff.department)
        password= data.get('password' , staff.password)
        #what connects them? 

        check_name= Staff.query.filter_by(email = email and id!=staff.id).first()
        check_email= Staff.query.filter_by(email = email and id!=staff.id).first()
        
        if check_name or check_email:
            return jsonify({"error": "Staff-name/Email already exist"}), 406
         
        else: 
            staff.staff_name = staff_name
            staff.email = email
            staff.department = department
            staff.password = password
        
        #Just commit no adding. 
            db.session.commit()
            return jsonify({"Success": "Staff updated successfully"}), 201
#if the staff does not exist? 
    else:
        return jsonify({"error":"Staff does not exist"}), 406
    
#fetch one Staff based on id 
@staff_bp.route('/staffs/<int:id>')
def fetch_one_user(id):
    staff= Staff.query.get(id)
    
    if staff:
        return jsonify({
            "id":staff.id,
            "staff_name":staff.staff_name,
            "email":staff.email,
            "department":staff.department,
            "password":staff.password
        })
    else: 
        return jsonify({"Error":"Staff does not exist"}),406
    
#Delete Staff
@staff_bp.route('/staffs/<int:staff_id>',methods=['DELETE'])          
def delete_user(staff_id):
    #get the staffs
    staff = Staff.query.get(staff_id)
    
    if staff:
        db.session.delete(staff)
        db.session.commit()
        return jsonify({"Success":"Staff Deleted Successfully"})

    else:
         return jsonify({"Error": "Staff does not exist"})