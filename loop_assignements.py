# 1)Iterate 0 to 10 using for loop, do the same using while loop. using for loop
x=[0,1,2,3,4,5,6,7,8,9,10]
for i in x:
    print(i,end=" ")

#using while loop
x=[0,1,2,3,4,5,6,7,8,9,10]
i=0
while i<=10:
    print(i,end=" ")
    i=i+1

 i=0
 while i<=10:
   print(i,end=" ")
  i=i+1


# 2)Iterate 10 to 0 using for loop, do the same using while loop.
for i in range(10,-1,-1):
    print(i,end=" ")


# using while loop
i=10
while i>=0:
    print(i,end=" ")
    i-=1


# 3)Write a loop that makes seven calls to print(),
# so we get on the output the following triangle:
for i in range(5):
    for j in range(5):
        print('*', end=" ")
    print()


# 4)Use nested loops to create the following:
for i in range(0,6):   
    for j in range(6-i):   
        print(" ",end='')
    for j in range(2*i+1):
        print("*",end='')
    print()


# 5.Print the following pattern using loops
for i in range(0,11):
    print(f"{i}*{i}={i*i}")



# 6.Iterate through the list, ['Python', 'Numpy','Pandas','Scikit', 'Pytorch']
# using a for loop and print out the items.
li=['Python', 'Numpy','Pandas','Scikit', 'Pytorch']
for i in li:
    print(i)

# 7.Use for loop to iterate from 0 to 100 and print only even numbers
for i in range(0,100):
    if (i%2==0):
        print(i,end=" ")


# 8.Use for loop to iterate from 0 to 100 and print only odd numbers
for i in range(0,100):
    if(i%2 != 0):
        print(i)

# 9.Use for loop to iterate from 0 to 100 and print the sum of all numbers.
num = 0
for i in range(0,101):
    num = num+i
print(num)

# 10.Use for loop to iterate from 0 to 100 and
# print the sum of all evens and the sum of all odds.
even=0
odd=0
for i in range(0,101):
    if i%2==0:
        even=even+i
    else:
        odd=odd+i
print(even,odd)

