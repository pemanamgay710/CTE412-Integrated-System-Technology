import json

def load_data():
    with open("student.json", "r") as f:
        return json.load(f)

def save_data(data):
    with open("student.json", "w") as f:
        json.dump(data, f, indent=4)

# Updating student by ID
def update_student(id, new_details):
    data = load_data()
    for stu in data["students"]:
        if stu["id"] == id:
            stu.update(new_details)
            save_data(data)
            print(" Updated student:\n", stu)
            return
    print("Student not found!")

# Example run
update_student(3, {"age": 34, "course": "Civil"})
