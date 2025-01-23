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
    feed = db.relationship("Feedback",back_populates="users", lazy = True)
    
    #repr methods returns a string
    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.phone_number}')"
    
# Staff Table
class Staff(db.Model):
    __tablename__ = "staff"
    
    id = db.Column(db.Integer,primary_key = True)
    staff_name = db.Column(db.String(128), nullable=False)
    is_admin = db.Column(db.Boolean, default = False)
    email = db.Column(db.String(120), nullable = False)
    department = db.Column(db.String(20), nullable=False)
    password= db.Column(db.String(120), nullable=False)
    
    #relationship between the Staff and feedback
    feed = db.relationship("Feedback",back_populates= "staff", lazy = True)
    
    def __repr__(self):
        return f"Staff('{self.staff_name},{self.is_admin}, {self.is_admin}, {self.email},{self.department}, {self.password}')"
    
# Feedback Table :  
class Feedback(db.Model):
    __tablename__ = "feedback"
    
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(128), nullable = False)
    description = db.Column(db.String(256))
    date= db.Column(db.DateTime, default = True)
    feedback_type = db.Column(db.Boolean(20), nullable=False)
    
    #create a relationship 
    staff_id = db.Column(db.Integer,db.ForeignKey("staff.id"))
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    
    # Relationship of Feedback with staff and users 
    user = db.relationship("User" ,back_populates="feedback")
    staff = db.relationship("Staff", back_populates="feedback")
    
    def __repr__(self):
        return f"Feedback('{self.title}', '{self.description}', '{self.date},{self.feedback_type}')"
    
    #Logout Revoke Class
class TokenBlocklist(db.Model):
    __tablename__ = "token_blocklist"
    
    id = db.Column(db.Integer, primary_key=True)
    jti = db.Column(db.String(36), nullable=False, index=True)
    created_at = db.Column(db.DateTime, nullable=False)
 
    
    
    

    
    

    
    
    
    
    


