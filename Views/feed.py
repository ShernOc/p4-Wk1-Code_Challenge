from flask import jsonify,request,Blueprint 
from datetime import datetime
from models import db,Feed

#blueprint
feed_bp = Blueprint('feed_bp', __name__)

#Fetch/Get Feedback
@feed_bp.route('/feeds')
def get_feed():
    #get the feeds 
    feeds = Feed.query.all()
    #create an empty list to store the feedback
    feed_list = []
    
    #create a loop that will loop through feed 
    for feed in feeds: 
        #in the append pass it as an json objects
        feed_list.append({
            "id": feed.id,
            "title":feed.title,
            "description" :feed.description,
            #date formation 
            "date": feed.date,
            "user_id":feed.user_id,
            "staff_id":feed.staff_id,
            "user":{"id":feed.user.id, "username":feed.user.username, "email":feed.user.email},
            "staff":{"id":feed.staff.id, "department":feed.staff.department, "email":feed.staff.email}
        })
    return jsonify(feed_list)

#Add a feeds 
@feed_bp.route('/feeds', methods=["POST"])
def add_feed():
    #initialize data 
    data = request.get_json() 
    title = data['title']
    description = data['description']
    #dates 
    date= datetime.strptime(data['date'],'%Y-%m-%d') 
    user_id = data['user_id']
    staff_id = data['staff_id']
    
#3. Check if the feeds exists
    check_title = Feed.query.filter_by(title=title).first() 
    check_user = Feed.query.filter_by(user_id=user_id).first()

    #prints the output 
    print("Title", check_title)
    print("User_id", check_user)
    
    #check and create errors
    if check_title:
        return jsonify({"error":"User/title already exist"}),406
    else: 
        new_feed = Feed(title = title, description = description, date = date, user_id = user_id, staff_id = staff_id)
        
        #call the function 
        db.session.add(new_feed)
        db.session.commit()
        return jsonify({"Success": "Feedback added successfully"})

#Update Feedback: 
#you can update the name, password,email .. 
@feed_bp.route('/feeds/<feed_id>', methods= ["PATCH"])
def update_feed(feed_id):
    #check if feedback exist
    feed = Feed.query.get(feed_id)
    
    if feed: # if feed exist
        #get the data 
        data = request.get_json() 
        title = data.get('title', feed.title)
        description = data.get('description', feed.description)
        date= datetime.strptime(data.get['date'],'%Y-%m-%d') 
        user_id = data.get('user_id', feed.user_id)
        staff_id = data.get('staff_id', feed.staff_id)
        
        #Check the data 
        check_title = Feed.query.filter_by(title=title and id!=feed.id).first() 
        check_user = Feed.query.filter_by(user_id=user_id and id!=feed.id).first()
    
        if check_title or check_user:
            feed.title = title
            feed.description = description
            feed.date= date
            feed.user_id = user_id
            feed.staff_id= staff_id
            
            
            #Just commit no adding. 
            db.session.commit()
            return jsonify({"Success": "Feedback updated successfully"}), 201
#if the Feedback does not exist? 
    else:
        return jsonify({"error": "Feedback id does not exist"}), 406
    
#fetch one Feedback based on id 
@feed_bp.route('/feeds/<int:id>')
def fetch_one_user(id):
    feed= Feed.query.get(id)
    
    if feed:
        return jsonify({
            "id":feed.id,
            "title":feed.title,
            "description":feed.description,
            "date":feed.date,
            "user_id":feed.user_id,
            "staff_id":feed.staff_id,
            "user":{"id":feed.user.id, "username":feed.user.username, "email":feed.user.email},
            "staff":{"id":feed.staff.id, "department":feed.staff.department, "email":feed.staff.email}
        })
    else: 
        return jsonify({"Error":"Feedback doesn't exist"})
    
#Delete Feedback
@feed_bp.route('/feeds/<int:feed_id>', methods=['DELETE'])
           
def delete_user(feed_id):
    #get the feeds
    feed = Feed.query.get(feed_id)
    
    if feed:
        db.session.delete(feed)
        db.session.commit()
        return jsonify({"Success":"Feedback deleted successfully"})
    
    else:
         return jsonify({"Error": "Feedback does not exist"})
     
     