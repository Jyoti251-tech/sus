from pymongo import MongoClient
try:
    MONGO_URI = "mongodb+srv://jyotigolya6_db_user:jiya8424@cluster0.0skqdyw.mongodb.net/?appName=Cluster0"

    client = MongoClient(MONGO_URI)

    client.admin.command("ping")

    db = client["SSUS"]

    Student_collection = db["student"]
    mark_collection = db ["marks"]
    attendance_collection = db["attendence"]
    bmi_collection = db["bmi reports"]


    print("mongodb succesfully connect")
except Exception as e:
    print("mongodb error",e)