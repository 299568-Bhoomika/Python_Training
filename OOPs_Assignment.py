#Q1) Write a Python program to implement the following:
# Class: Person
# Attributes: Age, Name, Gender, Address
# Methods:
# Constructor to initialize attributes
# Display() to print details
# Class: Student (inherits from Person)
# Attributes: Roll, Marks, College
# Methods:
# Constructor to initialize both Person and Student attributes
# Display() to print all details
# Class: Intern (inherits from Person)
# Attributes: InternId, Company, Duration
# Methods:
# Constructor to initialize both Person and Intern attributes
# Display() to print all details
# Class: Employee (inherits from Student and Intern)
# Represents a diamond inheritance problem.
# Attributes: EmpId, Salary
# Methods:
# Constructor to initialize attributes of all parent classes (Person, Student, Intern) and Employee.
# Display() to print complete details (Person + Student + Intern + Employee).
# Create an object of Employee with sample data and:
# Call the Display() method.

class person:
    def __init__(self, name, age, gender, address):
        self.name = name
        self.age = age
        self.gender = gender
        self.address = address

    def display(self):
        print("name:", self.name, "age:", self.age, "gender:", self.gender, "address:", self.address)

class student(person):
    def __init__(self, name,age,gender,address,roll,marks,college):
        person.__init__(self,name, age, gender, address)
        self.roll = roll
        self.marks = marks
        self.college = college

    def display(self):
        print("roll:", self.roll, "marks:", self.marks, "college:", self.college)

class intern(person):
    def __init__(self, name,age,gender,address,internID,company,duration):
        person.__init__(self,name,age,gender,address)
        self.internID = internID
        self.company = company
        self.duration = duration

    def display(self):
        print("internID:", self.internID, "company:", self.company, "duration:", self.duration)

class employee(student,intern):
    def __init__(self,name,age,gender,address,roll,marks,college,internID,company,duration,empID,salary):
        student.__init__(self,name, age, gender, address, roll, marks, college)
        intern.__init__(self,name,age,gender,address,internID,company,duration)
        person.__init__(self,name,age,gender,address)

        self.empID = empID
        self.salary = salary

    def display(self):
        person.display(self)
        student.display(self)
        print("internID:",self.internID,"company:",self.company,"duration:",self.duration,"empID:", self.empID, "salary:", self.salary)

e=employee("bhoomika",24,"female","bangalore","223","85%","St.Jospeh's","23341","UST","3years","299568",30000)
e.display()


# Q2) Create a Python program to demonstrate polymorphism using the following classes:
# Class: Account
# Method: interest_rate() → (no implementation, just a placeholder).
# Class: SavingsAccount (inherits from Account)
# Method: interest_rate() → prints "Savings Account Interest Rate: 4%".
# Class: CurrentAccount (inherits from Account)
# Method: interest_rate() → prints "Current Account Interest Rate: 0%".
# Class: FixedDeposit (inherits from Account)
# Method: interest_rate() → prints "Fixed Deposit Interest Rate: 7%".
# Create a function show_interest(account_obj) that accepts an Account object and calls its interest_rate() method.
# Pass objects of SavingsAccount, CurrentAccount, and FixedDeposit to demonstrate polymorphism.


class account:
    def interest(self):
        pass
class savingaccount(account):
    def interest(self):
        print("Savings Account Interest Rate: 4%")
class CurrentAccount(account):
    def interest(self):
        print("Current Account Interest Rate:0%")
class FixedDeposite(account):
    def interest(self):
        print("Fixed Deposite Interest Rate: 7%")
def show_interest(account_obj):
    account_obj.interest()
savings=savingaccount()
savings.interest()
current=CurrentAccount()
current.interest()
fixed=FixedDeposite()
fixed.interest()


# Q3) Write a Python program to implement encapsulation using the following:
# Class: BankAccount
# Private Attributes:
# __account_number
# __balance
# Public Methods:
# Constructor to initialize account number and balance.
# deposit(amount) → increases balance.
# withdraw(amount) → decreases balance if sufficient funds exist.
# get_balance() → returns current balance.
# get_account_number() → safely access account number.
# Create an object of BankAccount and:
# Deposit some money.
# Withdraw some money.
# Try accessing the private attributes directly (should not be allowed).
# Use getter methods to access values.

class bank_account:
    def __init__(self,accountNo,balance):
        self.__accountNo = accountNo
        self.__balance = balance
    def deposit(self,amount):
        self.__balance += amount
        print("Deposit Successful")
    def withdraw(self,amount):
        self.__balance -= amount
        print("Withdraw Successful")
    def get_balance(self):
        return self.__balance
    def get_accountNo(self):
        return self.__accountNo
account=bank_account(1234567,25000)
account.deposit(5000)
account.withdraw(10000)

accountNo=getattr(account,"get_accountNo")()
balance=getattr(account,"get_balance")()
print(accountNo)
print(balance)


# Q4) Write a Python program to implement abstraction using the following:
# Abstract Class: Shape (use ABC from abc module)
# Abstract Methods:
# area() → calculates the area of the shape
# perimeter() → calculates the perimeter of the shape
# Class: Circle (inherits from Shape)
# Attribute: radius
# Implements area() → returns π × radius²
# Implements perimeter() → returns 2 × π × radius
# Class: Rectangle (inherits from Shape)
# Attributes: length, width
# Implements area() → returns length × width
# Implements perimeter() → returns 2 × (length + width)
# Create objects of Circle, Rectangle and print their area and perimeter.
# Demonstrate abstraction because Shape cannot be instantiated directly, but all derived classes implement the abstract methods.


from abc import ABC,abstractmethod
class shape:
    def __init__(self):
        print("this is shape constructor")
    @abstractmethod
    def area(self):
        pass
    def perimeter(self):
        pass
class circle(shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * (self.radius ** 2)
    def perimeter(self):
        return 3.14 * 2 * self.radius
class rectangle(shape):
    def __init__(self, length, width):
        # shape().__init__()
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
    def perimeter(self):
        return 2 * (self.length + self.width)

c=circle(3)
print("area of the circle:",c.area())
print("perimeter of the circle:",c.perimeter())
r=rectangle(3,4)
print("area of the rectangle:",r.area())
print("perimeter of the rectangle:",r.perimeter())
