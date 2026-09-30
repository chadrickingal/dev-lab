# import fastAPI framework
from fastapi import FastAPI

# I create fake users using dictionary list
fake_user_storage = [
    {"id": 1, "name": "Anna", "email": "anna@gmail.com"},
    {"id": 2, "name": "John", "email": "john@gmail.com"},
    {"id": 3, "name": "Jane", "email": "jane@gmail.com"},
]

# create instance 
app = FastAPI(title="Path Parameter", description="This server is for basic | multiple | validation path")

# create endpoint with basic path with validation
@app.get("/users/{user_id}")
def find_user(user_id):
    for user in fake_user_storage:
        if user["id"] == user_id:
            return {"User": user}
    return {"message":"User not found!"}

##########################################################
#      These are another fake storage
##########################################################

fake_school_storage = [
    {"id": 1, "school": "Harvard University"},
    {"id": 2, "school": "Stanford University"},
    {"id": 3, "school": "MIT"},
]

fake_course_storage = [
    {"id": 1, "school_id": 1, "course": "Computer Science"},
    {"id": 2, "school_id": 1, "course": "Business Administration"},
    {"id": 3, "school_id": 2, "course": "Information Technology"},
    {"id": 4, "school_id": 3, "course": "Artificial Intelligence"},
]


# This endpoint can handle multiple path with validation
@app.get("/user/{user_id}/school/{school_id}/course/{course_id}")
def find_student_school_info(use_id :int, school_id :int, course_id : int):
    fake_school_course_storage = []

    fake_school_course_storage.append(fake_user_storage[use_id])
    fake_school_course_storage.append(fake_school_storage[school_id])
    fake_school_course_storage.append(fake_course_storage[course_id])
    
    return fake_school_course_storage