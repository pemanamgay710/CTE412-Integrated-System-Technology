import json

def load_data():
    with open("student.json", "r") as f:
        return json.load(f)

def save_data(data):
    with open("student.json", "w") as f:
        json.dump(data, f, indent=4)

# Delete student by ID
def delete_student(id):
    data = load_data()
    new_list = [stu for stu in data["students"] if stu["id"] != id]
    if len(new_list) != len(data["students"]):
        data["students"] = new_list
        save_data(data)
        print(f" Student with ID {id} deleted.\n")
    else:
        print(" Student not found!")

# Example run
delete_student(3)
