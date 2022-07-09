from flask import (
    Flask, 
    request,
    Response
)
from datetime import datetime
from app.database import user, cars

app = Flask(__name__)
 
VERSION = "1.0.0"

# GET PONG
@app.get("/ping")
def ping():
    out = {
        "status":"ok",
        "message":"pong"
    }
    return out

# GET VERSION
@app.get("/version")
def get_version():
    out= {
        "status":"ok",
        "version":VERSION,
        "server_time":datetime.now().strftime("%F %H:%M:%S")
    }
    return out

# GET ALL USERS
@app.get("/users")
def get_all_users():
    user_list = user.scan()
    out= {
        "status":"ok",
        "users":user_list
    }
    return out

# GET SINGLE USER BY ID
@app.get("/users/<int:pk>")
def get_user_by_id(pk):
    record = user.select_by_id(pk)

    out = {
    "status":"ok",
    "user":record
    }
    return out

# CREATE USER
@app.post("/users")
def create_user():
    try:
        user_data = request.json
        errors = ""

        #validations
        if not "first_name" in user_data or type(user_data.get("first_name")) != str:
            errors += "First_name not included or it is a digit. Please verify your user input."
        
        elif not "last_name" in user_data or type(user_data.get("last_name")) != str:
            errors += "Last_name not included or it is a digit. Please verify your user input."
        
        elif not "hobbies" in user_data or type(user_data.get("hobbies")) != str:
            errors += "Hobbies not included or it is a digit. Please verify your user input."
        
        if errors:
            return Response(errors, status=400)

        user.insert(user_data)
        return "",204

    except Exception as ex:
        print(ex)
        return Response("Unexpected error", status=500)    

# UPDATE USER
@app.put("/users/<int:pk>")
def update_user(pk):
    try:
        user_data = request.json
        
        if len(user_data) == 0:
            return Response("Empty input. Nothing to update. Please enter update data", status=400)
        elif "first_name" not in user_data and "last_name" not in user_data and "hobbies" not in user_data:
            return Response("Invalid user property. Please make sure you enter 'first_name' or 'last_name' or 'hobbies'", status=400)
        user.update(user_data, pk)
        return "",204

    except Exception as ex:
        print(ex)
        return Response("Unexpected error", status=500) 
    

# DELETE USER
@app.delete("/users/<int:pk>")
def delete_user(pk):
    user.delete(pk)
    return "",204


#  ---------------- VEHICLES -------------------
# GET VEHICLES PER USER
@app.get("/reports/cars")
def get_all_vehicles_per_user():
    cars_list = cars.scan()
    out= {
        "status":"ok",
        "cars":cars_list
    }
    return out
