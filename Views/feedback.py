from flask import jsonify,request,Blueprint 
from datetime import datetime
from models import db, Feedback
from flask_jwt_extended import jwt_required, get_jwt_identity

#blueprint
feed_bp = Blueprint('feed_bp', __name__)

#Fetch/Get Feedback
@feed_bp.route('/feeds')
@jwt_required()
def get_feed():
    current_user_id= get_jwt_identity()
    #get the feeds 
    feeds = Feedback.query.filter_by (user_id = current_user_id)
    
    #create an empty list to store the feedback
    feed_list = []
    #create a loop that will loop through feed 
    for feed in feeds: 
       
        feed_list.append({
            "id": feed.id,
            "title":feed.title,
            "description" :feed.description,
            #date formation 
            "date": feed.date,
            "user":{"id":feed.user.id, "username":feed.user.username, "email":feed.user.email},
            "staff":{"id":feed.staff.id, "department":feed.staff.department, "email":feed.staff.email}
        })
    return jsonify(feed_list)

#Add a feeds 
@feed_bp.route('/user_feeds', methods=["POST"])
@jwt_required()
def add_feed():
    #initialize data 
    data = request.get_json()
    current_user_id= get_jwt_identity()

    title = data['title']
    description = data['description']
    #dates 
    date= datetime(data['date'],'%Y-%m-%d') 
    staff_id = data['staff_id']
    
# Check if the feeds exists
    check_title = Feedback.query.filter_by(title=title).first() 

    #prints the output 
    print("Title", check_title)
    
    #check and create errors
    if check_title:
        return jsonify({"error":"User/title already exist"}),406
    else: 
        new_feed = Feedback(title = title, description = description, date = date, user_id = current_user_id)
        
        #call the function 
        db.session.add(new_feed)
        db.session.commit()
        return jsonify({"Success": "Feedback added successfully"})

#Update Feedback: 
@feed_bp.route('/user_feeds/<feed_id>', methods= ["PATCH"])
@jwt_required()
def update_feed(feed_id):
    current_user_id = get_jwt_identity()
    #check if feedback exist
    feed = Feedback.query.get(feed_id)
    
    if feed and feed.user_id == current_user_id: # if feed exist
        #get the data 
        data = request.get_json() 
        title = data.get('title', feed.title)
        description = data.get('description', feed.description)
        date= datetime.strptime(data.get['date'],'%Y-%m-%d') 
        user_id = data.get('user_id', feed.user_id)
        staff_id = data.get('staff_id', feed.staff_id)
        
        #Check the data 
        check_title = Feedback.query.filter_by(title=title and id!=feed.id).first() 
        check_user = User_Feed.query.filter_by(user_id=user_id and id!=feed.id).first()
    
        if check_title or check_user:
            feed.title = title
            feed.description = description
            feed.date= date
            feed.user_id = user_id
            feed.staff_id= staff_id
            
            #Call the functions 
            db.session.commit()
            return jsonify({"Success": "Feedback updated successfully"}), 201
        
    else:
        return jsonify({"error": "Feedback id does not exist"}), 406
    
#fetch one Feedback based on id 
@feed_bp.route('/user_feeds/<int:id>')
@jwt_required()
def fetch_one_user(id):
    current_user_id = get_jwt_identity()
    feed= Feedback.query.filter_by(id, user_id = current_user_id)
    
    if feed:
        return jsonify({
            "id":feed.id,
            "title":feed.title,
            "description":feed.description,
            "date":feed.date,
            "staff_id":feed.staff_id,
            "user":{"id":feed.user.id, "username":feed.user.username, "email":feed.user.email},
            "staff":{"id":feed.staff.id, "department":feed.staff.department, "email":feed.staff.email}
        })
    else: 
        return jsonify({"Error":"Feedback doesn't exist"})
    
#Delete Feedback
@feed_bp.route('/feeds/<int:feed_id>', methods=['DELETE'])
@jwt_required      
def delete_user(feed_id):
    #get the feeds
    current_user_id = get_jwt_identity()
    feed = Feedback.query.filter_by(feed_id, user_id = current_user_id)
    
    if feed:
        db.session.delete(feed)
        db.session.commit()
        return jsonify({"Success":"Feedback deleted successfully"})
    
    else:
         return jsonify({"Error": "Feedback does not exist"})
     
     