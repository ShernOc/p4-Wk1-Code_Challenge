from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from datetime import datetime

metadata = MetaData()
db = SQLAlchemy(metadata= metadata)

#User table:
#User: username, email, password, phone_number 
class User(db.Model):
    #named the table Users 
    __tablename__ = "users"
    
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(128), nullable = False)
    email = db.Column(db.String(128),nullable =False)
    phone_number = db.Column(db.String(120), nullable = False)
    password = db.Column(db.String(120), nullable = False)

    #create a relationship with the Feedback
    feedback = db.relationship("Feed",back_populates="user", lazy = True)
    
    #repr methods returns a string
    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.phone_number}')"
    
# Staff Table
class Staff(db.Model):
    __tablename__ = "staff"
    
    id = db.Column(db.Integer,primary_key = True)
    staff_name = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(120), nullable = False)
    department = db.Column(db.String(20), nullable=False)
    password= db.Column(db.String(120), nullable=False)
    
    #relationship between the Staff and feedback
    feedback = db.relationship("Feed",back_populates= "user", lazy = True)
    
    def __repr__(self):
        return f"Staff('{self.feedback}')"
    
# Feedback Table :  
class Feed(db.Model):
    __tablename__ = "feed"
    
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(128), nullable = False)
    description = db.Column(db.String(256))
    date= db.Column(db.DateTime, default = True)
    
    #create a relationship 
    user_id = db.Column(db.Integer,db.ForeignKey("user.id"), nullable= False)
    staff_id = db.Column(db.Integer,db.ForeignKey("staff.id"), nullable= False)
    
    # Relationship of Feedback with staff and users 
    user = db.relationship("User" ,back_populates="feed")
    tag = db.relationship("Staff", back_populates="feed")
    
    def __repr__(self):
        return f"Feed('{self.title}', '{self.description}', '{self.date}')"
    

    
    

    
    
    
    
    


