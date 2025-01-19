from flask import jsonify,request,Blueprint
from models import db,Staff

#blueprint
staff_bp = Blueprint('staff_bp', __name__)

#Fetch/Get Staff  
@staff_bp.route('/staffs')
def get_staff():
    #get the staffs 
    staffs = Staff.query.all()
    #create an empty list to store the staffs
    staff_list = []
    
    #create a loop that will loop through staffs 
    for staff in staffs: 
        #in the append pass it as an json objects
        staff_list.append({
            "id": staff.id,
            "staff_name":staff.staff_name,
            "email":staff.email,
            "phone_number":staff.is_approved, 
            "contact_method":staff.contact_method 
        })
    return jsonify(staff_list)

#Add a staffs 
@staff_bp.route('/staffs', methods=["POST"])
def add_staff():
    data = request.get_json() # This is an object in json 
    staff_name = data['staff_name']
    email = data['email']
    phone_number= data['phone_number']
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
        password = password,
        phone_number = phone_number)
        
        #call the function 
        db.session.add(new_staff)
        db.session.commit()
        return jsonify({"Success": "Staff added successfully"})

#UPDATE USER: 
#you can update the name, password,email .. 
@staff_bp.route('/staffs/<staff_id>', methods= ["PATCH"])
def update_staff_name(staff_id):
    #check if staff exist
    staff = Staff.query.get(staff_id)
    
    if staff: # if staff exist
        #get the data 
        data = request.get_json()
        staff_name = data['staff_name']
        email = data['email']
        phone_number = data['phone_number']
        #what connects them
        password = data['password']
        department = data['department']
    

        check_name= Staff.query.filter_by(email = email and id!=staff.id).first()
        check_email= Staff.query.filter_by(email = email and id!=staff.id).first()
        check_phone = Staff.query.filter_by(phone_number = phone_number and id!=staff.id).first()
        
        if check_name or check_email or check_phone:
            return jsonify({"error": "Staff-name/Email/phone_number already exist"}), 406
         
        else: 
            staff.staff_name = staff_name
            staff.email = email
            staff.password = password 
            staff.phone_number = phone_number
            staff.department = department
            staff.password 
        
        #Just commit no adding. 
            db.session.commit()
            return jsonify({"Success": "Staff updated successfully"}), 201
#if the staff does not exist? 
    else:
        return jsonify({"error": "Staff does not exist"}), 406
    
#fetch one Staff based on id 
@staff_bp.route('/staffs/<int:id>')
def fetch_one_user(id):
    staff= Staff.query.get(id)
    
    if staff:
        return jsonify({
            "id":staff.id,
            "staff_name":staff.staff_name,
            "email":staff.email,
            "phone_number":staff.is_complete,
            "department":staff.department,
            "staff_id":staff.staff_id,
            "password":staff.password
        })
    else: 
        return jsonify({"Error":"Staff doesn't exist"})
    
#Delete Staff
staff_bp.route('/staffs/<int:staff_id>',methods=['DELETE'])
           
def delete_user(staff_id):
    #get the staffs
    staff = Staff.query.get(staff_id)
    
    if staff:
        db.session.delete(staff)
        db.session.commit()
        return jsonify({"Success":"Staff Deleted Successfully"})

    else:
         return jsonify({"Error": "Staff does not exist"})