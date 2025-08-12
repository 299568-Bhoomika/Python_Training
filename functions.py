######Exercises -> Level 1#######

# 1)Area of a circle is calculated as follows: area = π x r x r and perimeter = 2 x π x r.
# Write a function that calculates area_of_circle and perimeter_of_circle

def area(radius):
    if r>0:
        return 3.142*r*r
    else:
        return 0
def perimeter(r):
    if r>0:
        return 2*3.142*r
    else:
        return 0
r=5
ar=area(r)
per=perimeter(r)
print(ar)
print(per)



# 2 Write a function called add_all_nums which takes arbitrary number of arguments
# and sums all the arguments.Check if all the list items are number types.
# If not do give a reasonable feedback

def add_all_nums(numbers):
    if not isinstance(numbers, list):
        return "allows only list of numbers"
    for i in numbers:
        if not isinstance(i, int):
            return "allows only int"
    return sum(numbers)
print(add_all_nums([1, 2, 3]))
print(add_all_nums([1, 2, "abcd"]))
print(add_all_nums([]))
print(add_all_nums(("bchd","abcd")))



# 3. Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32.
# Write a function which converts °C to °F, convert_celsius_2_fahrenheit.

def celsius_2_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32
celsius=12
print(f"the temperature is {celsius_2_fahrenheit(celsius)} degree fahrenheit")



# 4.Write a function called check_season, it takes a month parameter and returns the season:
# Autumn, Winter, Spring or Summer

def check_season(season):
    if season in ["september","october","november"]:
        return "Autumn"
    elif season in ["december","january","febraury","march"]:
        return "winter"
    elif season in ["april","may","june"]:
        return "Spring"
    elif season in ["july","august","september"]:
        return "Summer"
    else:
        print("no season entered")
season=input("enter months: ")
print(check_season(season))




# 5.Write a function called calculate_slope which return the slope of a linear equation

def calculate_slope(x1, y1, x2, y2):
    x = x2 - x1
    y = y2 - y1
    if x != 0:
        return y / x
    else:
        return "Undefined"
print(calculate_slope(1,2,3,4))
print(calculate_slope(4,5,3,2))



# 7.Declare a function named print_list.
# It takes a list as a parameter and it prints out each element of the list

def print_list(list):
    for i in list:
        print(i)
print_list([23,54,234,2,3])



# 8. Declare a function named reverse_list.
# It takes an array as a parameter and it returns the reverse of the array (use loops).
# print(reverse_list([1, 2, 3, 4, 5]))=[5, 4, 3, 2, 1] print(reverse_list1(["A", "B", "C"])) ["C", "B", "A"] ``

def reverse_list(ar):
    reversed_ar = []
    for i in range(len(ar) -1, -1, -1):
        reversed_ar.append(ar[i])
    return reversed_ar
print(reverse_list([1,2,3,4,5]))
print(reverse_list(["A","B","C"]))



# 9.Declare a function named capitalize_list_items.
# It takes a list as a parameter and it returns a capitalized list of items

def capitalize_list_items(li):
    capital=[]
    for i in li:
        capital.append(i.capitalize())
    return capital
print(capitalize_list_items(["cat","dog","rat"]))



# 10. Declare a function named add_item. It takes a list and an item parameters.
# It returns a list with the item added at the end.
# food_staff = ['Potato', 'Tomato', 'Mango', 'Milk'] print(add_item(food_staff, 'Fungi'))
# ['Potato', 'Tomato', 'Mango', 'Milk', 'Fungi']
# numbers = [2, 3, 7, 9] print(add_item(numbers, 5)) =[2, 3, 7, 9, 5]

def add_item(li,item):
    li.append(item)
    return li
food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(add_item(food_staff, 'Fungi'))
numbers = [2, 3, 7, 9]
print(add_item(numbers, 5))




# 11.Declare a function named remove_item. It takes a list and an item parameters.
# It returns a list with the item removed from it.
# food_staff = ['Potato', 'Tomato', 'Mango', 'Milk'] print(remove_item(food_staff, 'Mango'))
# ['Potato', 'Tomato', 'Milk'] numbers = [2, 3, 7, 9] print(remove_item(numbers, 3))=[2, 7, 9]

def remove_item(li, item):
    if item in li:
        li.remove(item)
        return li
food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(remove_item(food_staff, 'Mango'))
numbers = [2, 3, 7, 9]
print(remove_item(numbers, 3))



# 12. Declare a function named sum_of_numbers.
# It takes a number parameter and it adds all the numbers in that range.
# print(sum_of_numbers(5)) = 15 print(sum_all_numbers(10))= 55
# print(sum_all_numbers(100)) = 5050

def sum_of_numbers(num):
    total=0
    for i in range(1,num+1):
        total=total+i
    return total
print(sum_of_numbers(5))
print(sum_of_numbers(10))
print(sum_of_numbers(100))




# 13. Declare a function named sum_of_odds.
# It takes a number parameter and it adds all the odd numbers in that range.

def sum_of_odds(num):
    li=[]
    for i in range(1,num+1):
        if i%2!=0:
            li.append(i)
    return sum(li)
print(sum_of_odds(19))




# 14. Declare a function named sum_of_even.
# It takes a number parameter and it adds all the even numbers in that range.

def sum_of_even(num):
    li=[]
    for i in range(1,num+1):
        if i % 2 == 0:
            li.append(i)
    return sum(li)
print(sum_of_even(10))

########Exercises ➞ Level 2######

# 1. Declare a function named evens_and_odds. It takes a positive integer as parameter
# and it counts number of evens and odds in the number

def even_and_odds(positive):
    even=0
    odd=0
    for i in str(positive):
        if int(i)%2==0:
            even+=1
        else:
            odd+=1
    print(f"Even: {even}, Odd: {odd}")
even_and_odds(12345642)



# 2. Call your function factorial,
# it takes a whole number as a parameter and it return a factorial of the number

def factorial(n):
    if n==1:
        return 1
    else:
        return n * factorial(n-1)
n=5
print(factorial(n))



# 3.Call your function is_empty, it takes a parameter and it checks if it is empty or not
def is_empty(item):
        return not item
print(is_empty(""))
print(is_empty(None))
print(is_empty(False))
print(is_empty({}))
print(is_empty("hello"))
print(is_empty([1,2,3]))



#####Level ->#####

# 1. Write a function called is_prime, which checks if a number is prime.

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    else:
        return True
print(is_prime(4))




# 2. Write a functions which checks if all items are unique in the list
def unique(items):
    li = []
    for i in items:
        if i in li:
            return False
        li.append(i)
    return True
print(unique([1,2,3,4,5,5,6]))




# 3.Write a function which checks if all the items of the list are of the same data type

def datatype(li):
    for i in li:
        if type(i) != type(li[0]):
            return False
    return True
print(datatype([1,2,3]))
print(datatype([1,"2",3]))
print(datatype(["a","b"]))



# 5.Write a function which check if provided variable is a valid python variable
def variable(name):
    if name[0].isalpha() or name[0]=='_':
        return True
    else:
        return False
print(variable('Abhjdh'))
print(variable('12345'))
print(variable('_bchac'))
