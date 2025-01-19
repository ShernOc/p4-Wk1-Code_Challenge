from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

metadata = MetaData()
db = SQLAlchemy(metadata= metadata)

#User table:
#User: username, email, password, phone_number 
class User(db.Model):
    #named the table Users 
    __tablename__ = "Users"
    
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(128), nullable = False)
    email = db.Column(db.String(128),nullable =False)
    phone_number = db.Column(db.String(15))
    password = db.Column(db.String(120), nullable = False)

    #create a relationship with the Feedback
    feedback = db.relationship("Feed",back_populates="user", lazy =True)
    
    #repr methods returns a string
    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.phone_number}',{self.password} ,{self.feedback})" 
    
# Staff Table
class Staff(db.Model):
    __tablename__ = "Staff"
    
    id = db.Column(db.Integer,primary_key = True)
    staff_name = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(120),nullable = False)
    department = db.Column(db.String(20), nullable=False)
    password= db.Column(db.String(120), nullable=False)
    
    #relationship between the Staff and feedback
    feedback = db.relationship("Feed",back_populates="staff", lazy =True)
    
    def __repr__(self):
        return f"Staff('{self.feedback}')"
    
# Feedback Table :  
class Feed(db.Model):
    __tablename__ = "Todos"
    
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(128), nullable = False)
    description = db.Column(db.String(256))
    date= db.Column(db.DateTime, nullable=False)
    
    #create a relationship 
    user_id = db.Column(db.Integer,db.ForeignKey("Users.id"), nullable= False)
    staff_id = db.Column(db.Integer,db.ForeignKey("Staffs.id"), nullable= False)
    
    # Relationship of Feedback with staff and users 
    user = db.relationship("User", back_populates="feedback")
    tag = db.relationship("Staff", back_populates="feedback")
    
    def __repr__(self):
        return f"Feed('{self.title}', '{self.description}', '{self.date}',{self.staff_id} ,{self.user_id})"
    

    
    

    
    
    
    
    


