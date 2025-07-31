
# Q1) Create a dictionary named student_info with the following keys:
# student_name, age, roll_no, class, section, percentage, college_name

dict={"student_name":"max","age":16,"roll_no":22,"class":10,"section":"A","percentage":80,"college_name":"St.Josephs"}
print(dict)

# a) Print all the keys and values from the dictionary.
dict={"student_name":"max","age":16,"roll_no":22,"class":10,"section":"A","percentage":80,"college_name":"St.Josephs"}
print(dict)


# b) Add a new key - value pair: 'email': 'student@example.com' to the dictionary.
dict={"student_name":"max","age":16,"roll_no":22,"class":10,"section":"A","percentage":80,"college_name":"St.Josephs"}
dict['email']="student@example.com"
print(dict)

# c) Delete the section key from the dictionary.
dict={"student_name":"max","age":16,"roll_no":22,"class":10,"section":"A","percentage":80,"college_name":"St.Josephs"}
del dict["section"]
print(dict)

# d) Use a loop to print all key-value pairs in the dictionary in the format: Key --> Value
dict={"student_name":"max","age":16,"roll_no":22,"class":10,"section":"A","percentage":80,"college_name":"St.Josephs"}
for x,y in dict.items():
    print(x,y)

# e) Check if the key 'college_name' exists in the dictionary or not.
dict={"student_name":"max","age":16,"roll_no":22,"class":10,"section":"A","percentage":80,"college_name":"St.Josephs"}
if "college_name" in dict:
    print("yes")
else:
    print("no")


# Q2) You are given three sets representing students enrolled in different courses:
python_students = {"Alice", "Bob", "Charlie", "David"}
java_students = {"Bob", "Eve", "Frank", "David"}
cpp_students = {"Charlie", "George", "Eve", "Henry"}

# Find students who are enrolled in all three courses.
three_courses=python_students&java_students&cpp_students
print(three_courses)    ##no students are involved in all three courses

# Find students who are enrolled in only Python course.
print(python_students)

# Find students who are enrolled in both Python and Java.
stud=python_students&java_students
print(stud)

# Find students who are enrolled in either Python or Java but not both
stud=python_students^java_students
print(stud)

# Find the list of all unique students enrolled in any course.
stud=(python_students-java_students-cpp_students)|(java_students-cpp_students-python_students)|(cpp_students-python_students-java_students)
print(stud)

# Find students who are in Java or C++, but not in Python.
stud=java_students|cpp_students
x=stud-python_students
print(x)

# Check if all Python students are also Java students.
stud=python_students<=java_students ##stud=python_students.issubset(java_students)
print(stud)

# Add a new student "Jones" to the Python set.
py={"Jones"}
x=python_students|py
print(x)

# Remove "Frank" from the Java set.
java_students.remove("Frank")
print(java_students)

# Clear the cpp_students set.
cpp_students.clear()
print(cpp_students)
