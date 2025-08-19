import json

# Load and save helpers
def load_data():
    with open("student.json", "r") as f:
        return json.load(f)

def save_data(data):
    with open("student.json", "w") as f:
        json.dump(data, f, indent=4)

# Create new student
def create_student(id, name, age, email, course):
    data = load_data()
    new_student = {"id": id, "name": name, "age": age, "email": email, "course": course}
    data["students"].append(new_student)
    save_data(data)
    print(" Student added:\n", new_student)


create_student(3, "Dorji", 23, "dorji@gmail.com", "AI")
