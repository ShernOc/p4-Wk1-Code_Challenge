from flask import jsonify,request,Blueprint
from models import db,Feed

#blueprint
feed_bp = Blueprint('feed_bp', __name__)

#Fetch/Get Staff  
@feed_bp.route('/feeds')
def get_feed():
    #get the feeds 
    feeds = Feed.query.all()
    #create an empty list to store the feedback
    feed_list = []
    
    #create a loop that will loop through feed 
    for staff in feeds: 
        #in the append pass it as an json objects
        feed_list.append({
            "id": feed.id
            "title" feed.title
            "user_id" feed.email,
            "description" feed.description, 
            "contact_m" feed.contact_method 
        })
    return jsonify(feed_list)

#Add a feeds 
@feed_bp.route('/feeds', methods=["POST"])
def add_staff():
    data = request.get_json() # This is an object in json 
    staff_name = data['staff_name']
    email = data['email']
    phone_number= data['phone_number']
    password = data['password']
    
#3. Check if the feeds exists
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
@feed_bp.route('/feeds/<staff_id>', methods= ["PATCH"])
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
@feed_bp.route('/feeds/<int:id>')
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
feed_bp.route('/feeds/<int:staff_id>',methods=['DELETE'])
           
def delete_user(staff_id):
    #get the feeds
    staff = Staff.query.get(staff_id)
    
    if staff:
        db.session.delete(staff)
        db.session.commit()
        return jsonify({"Success":"Staff Deleted Successfully"})

    else:
         return jsonify({"Error": "Staff does not exist"})