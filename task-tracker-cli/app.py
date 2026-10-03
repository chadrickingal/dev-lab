
# Task Tracker CLI using JSON as Database
#-------------------------------------------

from datetime import datetime, date
import json 

# Generated ID function
def idGenerated():

    # Load the users json file get it using the variable users
    with open("users.json", "r") as file:
        users = json.load(file)

    # Check if users is empty
    if not users:
        return 1

    # Get the highest number using max and add into 1
    return max(user["id"] for user in users) + 1 


# Create Task and Insert it in JSON file
def createTask(desc, status = "todo"):

    # Get a Date and Time Realtime and formatted
    dateTimeNow = datetime.now()
    dateNow = dateTimeNow.strftime("%B %d, %Y")
    timeNow = dateTimeNow.strftime("%H-%M-%S %p")

    # Create a dictionary as insert to JSON containing data 
    task = {
        "id" :  idGenerated(),
        "description" : desc,
        "status" : status,
        "created_at" : f"{dateNow} | Time: {timeNow}",
        "updated_at" : f"{dateNow} | Time: {timeNow}",
    } 

    # Load JSON to get the data in JSON file 
    with open("users.json", "r") as file:
        users = json.load(file)

    # insert new task on users using append and containing data from task dictionary
    users.append(task)

    # write the python data to JSON file
    with open("users.json", "w") as file:
        json.dump(users, file, indent=4)

# Delete Task in JSON file
def deleteTask(id):

    with open("users.json", "r") as file: 
        users = json.load(file)

    users = [user for user in users if user["id"] != id]

    # with open("users.json", )

createTask(2, "hello ")

