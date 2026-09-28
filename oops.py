class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Course:", self.course)


s1 = Student("Nishitha", 22, "AIML")
s1.display()


class Employee:
    def __init__(self, name, basic_salary):
        self.name = name
        self.basic_salary = basic_salary

    def display_salary(self):
        print("Name:", self.name)
        print("Salary:", self.basic_salary)


e1 = Employee("Aparna", 30000)
e1.display_salary()


class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient Balance")
        else:
            self.balance -= amount

    def display_balance(self):
        print("Balance:", self.balance)


a1 = BankAccount("Nishitha", 10000)

a1.deposit(5000)
a1.withdraw(3000)
a1.display_balance()


class Mobile:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def display(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Price:", self.price)
        print()


m1 = Mobile("Samsung", "S24", 70000)
m2 = Mobile("Apple", "iPhone 15", 60000)
m3 = Mobile("OnePlus", "12", 50000)

m1.display()
m2.display()
m3.display()


class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)


r = Rectangle(10, 5)

print("Area:", r.area())
print("Perimeter:", r.perimeter())


class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display_marks(self):
        print("Name:", self.name)
        print("Marks:", self.marks)

    def check_result(self):
        if self.marks >= 40:
            print("Pass")
        else:
            print("Fail")


s1 = Student("A", 80)
s2 = Student("B", 35)
s3 = Student("C", 65)
s4 = Student("D", 40)
s5 = Student("E", 25)

s1.display_marks()
s1.check_result()

s2.display_marks()
s2.check_result()


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def calculate_bonus(self):
        if self.salary >= 50000:
            bonus = self.salary * 10 / 100
        else:
            bonus = self.salary * 5 / 100

        print("Employee Name:", self.name)
        print("Salary:", self.salary)
        print("Bonus:", bonus)
        print("Total Salary:", self.salary + bonus)


e1 = Employee("Aparna", 60000)
e1.calculate_bonus()


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def calculate_bonus(self):
        if self.salary >= 50000:
            bonus = self.salary * 10 / 100
        else:
            bonus = self.salary * 5 / 100

        print("Employee Name:", self.name)
        print("Salary:", self.salary)
        print("Bonus:", bonus)
        print("Total Salary:", self.salary + bonus)


e1 = Employee("Aparna", 60000)
e1.calculate_bonus()



class Product:
    def __init__(self, product_name, price):
        self.product_name = product_name
        self.price = price

    def calculate_discount(self):
        if self.price >= 5000:
            discount = self.price * 20 / 100
        elif self.price >= 2000:
            discount = self.price * 10 / 100
        else:
            discount = self.price * 5 / 100

        final_price = self.price - discount

        print("Product:", self.product_name)
        print("Original Price:", self.price)
        print("Discount:", discount)
        print("Final Price:", final_price)


p1 = Product("Laptop", 60000)
p1.calculate_discount()


class ATM:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient Balance")

    def check_balance(self):
        print("Balance:", self.balance)


a1 = ATM(12345, 10000)

a1.deposit(5000)
a1.withdraw(3000)
a1.check_balance()


class Car:
    def __init__(self, brand, model, price, fuel_type):
        self.brand = brand
        self.model = model
        self.price = price
        self.fuel_type = fuel_type

    def display(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Price:", self.price)
        print("Fuel:", self.fuel_type)

    def check_price(self):
        if self.price > 1000000:
            print("Premium Car")
        else:
            print("Normal Car")


c1 = Car("Toyota", "Fortuner", 3500000, "Diesel")
c1.display()
c1.check_price()


class ElectricityBill:
    def __init__(self, customer_name, units):
        self.customer_name = customer_name
        self.units = units

    def calculate_bill(self):
        if self.units <= 100:
            self.bill = self.units * 2
        elif self.units <= 200:
            self.bill = self.units * 3
        elif self.units <= 300:
            self.bill = self.units * 5
        else:
            self.bill = self.units * 7

    def display_bill(self):
        print("Customer:", self.customer_name)
        print("Units:", self.units)
        print("Bill:", self.bill)


e = ElectricityBill("Nishitha", 250)
e.calculate_bill()
e.display_bill()



class Book:
    def __init__(self, title, author, price, available):
        self.title = title
        self.author = author
        self.price = price
        self.available = available

    def display_book(self):
        print("Title:", self.title)
        print("Author:", self.author)
        print("Price:", self.price)
        print("Available:", self.available)

    def borrow_book(self):
        if self.available:
            self.available = False
            print("Book Borrowed")
        else:
            print("Book Not Available")

    def return_book(self):
        self.available = True
        print("Book Returned")


b = Book("Python", "Guido", 500, True)

b.display_book()
b.borrow_book()
b.display_book()
b.return_book()


class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total(self):
        return self.price * self.quantity

    def display_product(self):
        print(self.name, self.price, self.quantity)


p1 = Product("Laptop", 50000, 1)
p2 = Product("Mouse", 500, 2)
p3 = Product("Keyboard", 1000, 1)

total = p1.calculate_total() + p2.calculate_total() + p3.calculate_total()

p1.display_product()
p2.display_product()
p3.display_product()

print("Total:", total)



class Employee:
    def __init__(self, name, salary, rating):
        self.name = name
        self.salary = salary
        self.rating = rating

    def display(self):
        print("Name:", self.name)
        print("Salary:", self.salary)
        print("Rating:", self.rating)

    def calculate_increment(self):
        if self.rating >= 4.5:
            increment = self.salary * 20 / 100
        elif self.rating >= 3.5:
            increment = self.salary * 10 / 100
        else:
            increment = self.salary * 5 / 100

        print("Increment:", increment)
        print("New Salary:", self.salary + increment)


e = Employee("Aparna", 50000, 4.6)
e.display()
e.calculate_increment()



class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance - amount >= 1000:
            self.balance -= amount
        else:
            print("Minimum balance of 1000 must be maintained")

    def check_balance(self):
        print("Balance:", self.balance)


a = BankAccount("Nishitha", 5000)

a.deposit(2000)
a.withdraw(5500)
a.check_balance()


class FoodOrder:
    def __init__(self, customer_name, food_name, price, quantity):
        self.customer_name = customer_name
        self.food_name = food_name
        self.price = price
        self.quantity = quantity

    def calculate_total(self):
        self.total = self.price * self.quantity

    def apply_discount(self):
        if self.total >= 2000:
            self.discount = self.total * 20 / 100
        elif self.total >= 1000:
            self.discount = self.total * 10 / 100
        else:
            self.discount = 0

        self.final_price = self.total - self.discount

    def display_order(self):
        print("Customer:", self.customer_name)
        print("Food:", self.food_name)
        print("Total:", self.total)
        print("Discount:", self.discount)
        print("Final Price:", self.final_price)


f = FoodOrder("Nishitha", "Pizza", 800, 3)

f.calculate_total()
f.apply_discount()
f.display_order()


class Patient:
    def __init__(self, name, age, disease, bill):
        self.name = name
        self.age = age
        self.disease = disease
        self.bill = bill

    def display_patient(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Disease:", self.disease)
        print("Bill:", self.bill)

    def add_bill(self, amount):
        self.bill += amount

    def check_bill(self):
        print("Total Bill:", self.bill)


p1 = Patient("Ravi", 45, "Fever", 5000)

p1.add_bill(2000)
p1.display_patient()
p1.check_bill()


class Employee:
    def __init__(self, name, total_days, present_days):
        self.name = name
        self.total_days = total_days
        self.present_days = present_days

    def attendance_percentage(self):
        return (self.present_days / self.total_days) * 100

    def check_attendance(self):
        percentage = self.attendance_percentage()

        print("Attendance:", percentage, "%")

        if percentage >= 75:
            print("Eligible")
        else:
            print("Not Eligible")


e = Employee("Aparna", 100, 80)

e.check_attendance()


class MovieTicket:
    def __init__(self, movie_name, ticket_price, number_of_tickets):
        self.movie_name = movie_name
        self.ticket_price = ticket_price
        self.number_of_tickets = number_of_tickets

    def calculate_total(self):
        self.total = self.ticket_price * self.number_of_tickets

    def apply_discount(self):
        if self.number_of_tickets >= 5:
            self.discount = self.total * 10 / 100
        else:
            self.discount = 0

        self.final_price = self.total - self.discount

    def display_ticket(self):
        print("Movie:", self.movie_name)
        print("Tickets:", self.number_of_tickets)
        print("Total:", self.total)
        print("Discount:", self.discount)
        print("Final Price:", self.final_price)


m = MovieTicket("Avatar", 300, 5)

m.calculate_total()
m.apply_discount()
m.display_ticket()


class Student:
    def __init__(self, name, roll_no, python, sql, powerbi):
        self.name = name
        self.roll_no = roll_no
        self.python = python
        self.sql = sql
        self.powerbi = powerbi

    def calculate_total(self):
        return self.python + self.sql + self.powerbi

    def calculate_average(self):
        return self.calculate_total() / 3

    def calculate_grade(self):
        avg = self.calculate_average()

        if avg >= 90:
            return "A"
        elif avg >= 75:
            return "B"
        elif avg >= 60:
            return "C"
        elif avg >= 40:
            return "D"
        else:
            return "Fail"

    def display_report(self):
        print("Name:", self.name)
        print("Roll No:", self.roll_no)
        print("Python:", self.python)
        print("SQL:", self.sql)
        print("Power BI:", self.powerbi)
        print("Total:", self.calculate_total())
        print("Average:", self.calculate_average())
        print("Grade:", self.calculate_grade())


s = Student("Nishitha", 101, 90, 85, 95)
s.display_report()

