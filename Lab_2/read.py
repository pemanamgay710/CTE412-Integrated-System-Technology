import json

def load_data():
    with open("student.json", "r") as f:
        return json.load(f)

def read_student(id):
    data = load_data()
    student = next((stu for stu in data["students"] if stu["id"] == id), None)
    if student:
        print("Student details: \n", student)
    else:
        print("Student not found!")

read_student(2)

# how to validate a json file against a schema
# schema verification and also for xml