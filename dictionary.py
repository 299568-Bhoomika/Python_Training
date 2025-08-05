# 1 Create an empty dictionary called bird:
bird={}

# 2 Add name, color, breed, legs, age to the bird dictionary
bird['name']='cuco'
bird['color']='white'
bird['breed']='sparrow'
bird['legs']=2
bird['age']=2
print(bird)

# 3 Create a student dictionary and add first_name, last_name, gender,
# age, marital_status, skills, country, city and address as keys for the dictionary
student={'first_name':'John','last_name':'Martin','gender':'male','age':18,
         'marital_status':'unmarried','skills':['python','c++'],'country':'India','city':'Bangalore',
         'address':'richmond circle'}
print(student)

# 4 Get the length of the student dictionary
print(len(student))

# 5 Get the value of skills and check the data type, it should be a list
 x=student['skills']
 print(x)
 print(type(x))


# 6 Modify the skills values by adding one or two skills
 student['skills']=["java","C programming"]
 print(student)

# 7 Get the dictionary keys as a list:
 x=[]
 x=list(student.keys())
 print(x)

# 8 Get the dictionary values as a list
 a=[]
 a=list(student.values())
 print(a)

# 9 Change the dictionary to a list of tuples using items() method
 x=student.items()
 print(x)

# 10 Delete one of the items in the dictionary
 student['skills'].remove('python')
 print(student)

# 11 Delete one of the dictionaries
 del student['address']
 print(student)
