Create a Flask App with the following features;

Models:
Implement a User model for user management.
Create another model of your choice with at least three fields.

#Customer Management System 

User: username, email, phone_number,  contact_method 
CRUD: 
fetch, add, update, delete 

Staff: staff_name, staff_email, staff_phone_number, department,  ticket_no, 
fetch, add, update, delete 

Feedback: title, user_id, description,  date 
fetch, add, update, delete 

Staff-Feedback, title, staff_id, description, 
fetch, add, update, delete 

# Installations 
- Flask, Flask-SQLAlchemy, Flask-Migrate, 
- 


CRUD Operations:
Perform Create, Read, Update, and Delete (CRUD) operations for the additional model.
Ensure that some operations are protected with authentication(using @jwt_required() )
User Registration:
Allow users to register for an account.
Authentication with flask_jwt_extended:
Users should be able to log in and receive a JWT access token.
Provide a route to fetch the details of the currently logged-in user(/current_user).
Implement a logout feature to invalidate the user's token(/logout).
Allow users to update their profile information(/user/update).
Include functionality for users to update their password(/user/updatepassword).
Enable users to delete their own account (only self-deletion is allowed)(/user/delete_account)
All your routes(API endpoints) should be tested using Postman.


NB:
Understand your code for explanations during marking and all your endpoints should be created with Postman

