
# Task Tracker CLI using JSON as Database
#-------------------------------------------

from datetime import datetime
import json, shlex


class DateTimeFromatted:

    # Get a Date and Time Realtime and formatted
    @staticmethod
    def currentDate():
        return datetime.now().strftime("%B %d, %Y")

    @staticmethod
    def currentTime():
        return datetime.now().strftime("%H:%M:%S %p")

def generatedID():
    db = DataBase()
    users = db.load_db()

    if not users:
        return 1

    return max(user["id"] for user in users) + 1


class DataBase:

    def load_db(self):
        with open("users.json", "r") as file:
            users = json.load(file)
            return users

    def addToDatabase(self, item):
        with open("users.json", "w") as file:
            json.dump(item, file, indent=4)

class Task:
    # CREATE A INSTANCE ATTRIBUTE
    def __init__(self):
        self.storage = DataBase()
        self.tasks = self.storage.load_db()

#---------------------------------------------------------------------
# Create a New Task
#---------------------------------------------------------------------
    def addTask(self, desc, status = "Todo"):

        task = {
            "id": generatedID(),
            "description": desc,
            "status" : status,
            "created_at" : {
                "date" : f"Date: {DateTimeFromatted.currentDate()}",
                "time" : f"Time: {DateTimeFromatted.currentTime()}"
            },
            "updated_at" :{
                "date" : f"Date: {DateTimeFromatted.currentDate()}",
                "time" : f"Time: {DateTimeFromatted.currentTime()}"
            },
        }
        
        self.tasks.append(task)
        self.storage.addToDatabase(self.tasks)


#---------------------------------------------------------------------
# UPDATE TASK USING ID 
#---------------------------------------------------------------------
    def updateTask(self, id, desc):

        for task in self.tasks:
            if task["id"] == id:

                task["updated_at"] = {
                    "date" : f"Date: {DateTimeFromatted.currentDate()}",
                    "time" : f"Time: {DateTimeFromatted.currentTime()}"
                    }
                task["description"] = desc
                break
        self.storage.addToDatabase(self.tasks)

#---------------------------------------------------------------------
# UPDATE TASK STATUS USING ID 
#---------------------------------------------------------------------
    def updateStatusTask(self, id, status):

        for task in self.tasks:
            if task["id"] == id:
    
                task["updated_at"] = {
                    "date" : f"Date: {DateTimeFromatted.currentDate()}",
                    "time" : f"Time: {DateTimeFromatted.currentTime()}"
                    }
                task["status"] = status
                break

        self.storage.addToDatabase(self.tasks)

#---------------------------------------------------------------------
# DELETE TASK USING ID 
#---------------------------------------------------------------------
    def deleteTask(self, id):

        # Modify (Edit)
        self.tasks = [task for task in self.tasks if task["id"] != id]
        # Save
        self.storage.addToDatabase(self.tasks)

#---------------------------------------------------------------------
# SHOW ALL TASK
#---------------------------------------------------------------------
    def show(self, ):
        for task in self.tasks:    
            print(f"""------------------------------------------------------------------------
  Task {task["id"]}: {task["status"]}                                                  
    Description: {task["description"]}                                                 
    Created At: {task["created_at"]["date"]} | {task["created_at"]["time"]}             
    Update At: {task["updated_at"]["date"]}  | {task["updated_at"]["time"]}             """)
            print("------------------------------------------------------------------------")


#---------------------------------------------------------------------
# SHOW ALL TASK BASED ON STATUS INPUT
#---------------------------------------------------------------------
    def showTaskByStatus(self, status):
        for task in self.tasks:  
            if task["status"] == status:  
                print(f"""------------------------------------------------------------------------
  Task {task["id"]}: {task["status"]}                                                  
    Description: {task["description"]}                                                 
    Created At: {task["created_at"]["date"]} | {task["created_at"]["time"]}             
    Update At: {task["updated_at"]["date"]}  | {task["updated_at"]["time"]}             """)
                print("------------------------------------------------------------------------")


task = Task()
while True:
    userInput = input("task-cli: ")
    splitUser = shlex.split(userInput)

    if not splitUser:
        print("[Result] : Invalid Action")

    elif splitUser[0].lower() == "update":
        if len(splitUser) < 3:
            print("[Result] : Usage: update <id> <description>")
        else:
            task.updateTask(int(splitUser[1]), splitUser[2])

    elif splitUser[0].lower() == "add":
        if len(splitUser) < 2:
            print("[Result] : Usage: add <description>")
        else:
            task.addTask(splitUser[1])

    elif splitUser[0].lower() == "list":
        if len(splitUser) == 1:
            task.show()
        elif splitUser[1].lower() in ["done", "in-progress", "to-do"]:
            task.showTaskByStatus(splitUser[1])
        else:
            print("[Result] : Invalid list option")

    else:
        print("[Result] : Invalid Action")


