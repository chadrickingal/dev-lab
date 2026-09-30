# importing fastapi feature APIRouter to organize endpoints
from fastapi import APIRouter

# Initialize the instance of APIRouter with prefix and tags
# prefix is common starting path of all routes to make more clean the routes path if add multiple path
# tags is to group the all routs in Swagger/OpenAPI 
route = APIRouter(prefix="/users", tags=["Users"])

# I create fake users using dictionary list
fake_user_storage = [
    {"id": 1, "name": "Anna", "email": "anna@gmail.com"},
    {"id": 2, "name": "John", "email": "john@gmail.com"},
    {"id": 3, "name": "Jane", "email": "jane@gmail.com"},
]

# create routes
@route.get("/")  # this route path is --> /users/
def get_user():
    return fake_user_storage

@route.get("/{user_id}")  # this path is --> /users/{user_id}
def get_user(user_id : int):
    for user in fake_user_storage:
        if user["id"] == user_id:
            return user
    return {"message":"User not found"}

@route.post("/")
def add_user():
    return {"message":"User successfully added"}


@route.delete("/")
def remove_user():
    return {"message":"User successfully remove"}