"""
  This new update when the basic router turning in to new router using the features of fastapi (APIRouter)
  This APIRouter is use to group and arrange the routes of api in the application
"""
# import fastapi framework and user from router to register the user routes in application
from fastapi import FastAPI
from router import user

# initialize the instance of fastapi
app = FastAPI(title="Routing", description="This server created for understanding basic routing")



# example Homepage Endpoint
@app.get("/")
def home():
    return {"message" : "Welcome to basic routing API"}

# register the user router using include_router() method in application
app.include_router(user.route)