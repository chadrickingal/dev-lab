# import fastapi framework for creating endpoints
from fastapi import FastAPI

# initialize the instance of fastapi
app = FastAPI(title="Routing", description="This server created for understanding basic routing")

# I create fake users using dictionary list
fake_user_storage = [
    {"id": 1, "name": "Anna", "email": "anna@gmail.com"},
    {"id": 2, "name": "John", "email": "john@gmail.com"},
    {"id": 3, "name": "Jane", "email": "jane@gmail.com"},
]

# example Homepage Endpoint
@app.get("/")
def home():
    return {"message" : "Welcome to basic routing API"}


# get all users using GET HTTP method
@app.get("/users")
def get_users():
    return fake_user_storage

# add user using POST HTTP method
@app.post("/users")
def add_user():
    return {"message": "add user successfully!"}


# delete user using DELETE HTTP method 
@app.delete("/users")
def remove_user():
    return {"message":"1 user deleted!"}