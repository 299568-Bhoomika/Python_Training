 #Q1) Create list called "even", store all the even numbers, in the range of 1 to 20.
even=[]
for i in range(1,21):
    if (i%2==0):
        even.append(i)
print(even)

# Q2)Create list called "odd", store all the even numbers, in the range of 1 to 20.
odd=[]
for i in range(1,21):
    if i%2!=0:
        odd.append(i)
print(odd)

# Q3) Take "even" and "odd" list  from previous solution, merge it in new list called "numbers" and sort it.
even=[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
odd=[1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
numbers=even+odd
numbers.sort()
print(numbers)


# Q4) Create a nested list for called "Students" for 5 student, each index store the student information. ex.. ["name",roll,marks].
students=[["abc",1,89],["def",2,66],["ghi",3,42],["jkl",4,90],["mno",5,88]]
print(students)

# Q5) Write a Python program to find the second largest number in a list
lis=[12,34,42,77,65]
large=max(lis)
lis.remove(large)
second_large=max(lis)
print(second_large)


# Q6)WAP to print unique element from list.
x=[1,3,2,5,1,3,6,]
y=[]
for i in x:
    if x.count(i)==1:
        y.append(i)
print(y)


# Q7) Given a tuple of numbers, find the max and min elements.
tup = (11,26,45,23,15,18)
x=max(tup)
y=min(tup)
print(x,y)


# Q8) Retrieve the 'G' from following list using positive indexing
L1 = [1, 2, 'hi', (21, 78, [-2, -4, ('Bahubali', 'KGF', 'RRR')])]
print(L1[3][2][2][1][1])

# Q9) WAP to retrieve the 'Sweet' string from the following nested list using Positive indexing
L2 = [21, ['Anil', 'Education', [['Java', 'Kova'], ['Programming', 'Sugar', 'Sweet','Wheat']]], 7065, 5, 2034, [1, 2]]
print(L2[1][2][1][2])

# Q10) WAP to extract 'Bengaluru' in reverse order using negative indexing from following string
s2 = 'Hello I am going to Bengaluru How are you doing?'
print(s2[-28:-19])
