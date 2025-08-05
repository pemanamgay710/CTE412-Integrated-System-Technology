import xml.etree.ElementTree as ET

# Load and parse the XML file
tree = ET.parse('students.xml')
root = tree.getroot()

print("Student Details:\n")
for student in root.findall('Student'):
    student_id = student.find('ID').text
    name = student.find('Name').text
    age = student.find('Age').text
    department = student.find('Department').text

    print(f"ID: {student_id}")
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Department: {department}")
    print("-" * 30)
