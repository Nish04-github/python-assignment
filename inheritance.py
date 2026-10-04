class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student(Person):
    def __init__(self, name, age, course):
        super().__init__(name, age)
        self.course = course

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Course:", self.course)


s = Student("Nishitha", 22, "AIML")
s.display()



class Employee:
    def __init__(self, name, salary, department):
        self.name = name
        self.salary = salary
        self.department = department


class Manager(Employee):
    def __init__(self, name, salary, department, team_size):
        super().__init__(name, salary, department)
        self.team_size = team_size

    def display(self):
        print(self.name, self.salary, self.department, self.team_size)


m = Manager("Aparna", 60000, "IT", 10)
m.display()



class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model


class Car(Vehicle):
    def __init__(self, brand, model, fuel_type):
        super().__init__(brand, model)
        self.fuel_type = fuel_type

    def display(self):
        print(self.brand, self.model, self.fuel_type)


c = Car("Toyota", "Fortuner", "Diesel")
c.display()




class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance


class SavingsAccount(BankAccount):
    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def display(self):
        print("Account:", self.account_number)
        print("Balance:", self.balance)
        print("Interest:", self.interest_rate)


a = SavingsAccount(12345, 10000, 5)
a.display()



class Product:
    def __init__(self, product_name, price):
        self.product_name = product_name
        self.price = price


class ElectronicProduct(Product):
    def __init__(self, product_name, price, warranty_years):
        super().__init__(product_name, price)
        self.warranty_years = warranty_years

    def display(self):
        print(self.product_name, self.price, self.warranty_years)


p = ElectronicProduct("Laptop", 60000, 2)
p.display()



class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    def display(self):
        print(self.name, self.age, self.breed)


d = Dog("Tommy", 3, "Labrador")
d.display()




class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student(Person):
    def __init__(self, name, age, course, marks):
        super().__init__(name, age)
        self.course = course
        self.marks = marks

    def display(self):
        print(self.name, self.age, self.course, self.marks)


s = Student("Nishitha", 22, "AIML", 85)
s.display()



class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


class Developer(Employee):
    def __init__(self, name, salary, language, experience):
        super().__init__(name, salary)
        self.language = language
        self.experience = experience

    def display(self):
        print(self.name, self.salary, self.language, self.experience)


d = Developer("Rahul", 50000, "Python", 2)
d.display()




class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model


class Car(Vehicle):
    def __init__(self, brand, model, fuel_type, price):
        super().__init__(brand, model)
        self.fuel_type = fuel_type
        self.price = price

    def display(self):
        print(self.brand, self.model, self.fuel_type, self.price)


c = Car("Honda", "City", "Petrol", 1200000)
c.display()



class BankAccount:
    def __init__(self, holder_name, balance):
        self.holder_name = holder_name
        self.balance = balance


class SavingsAccount(BankAccount):
    def __init__(self, holder_name, balance, interest_rate):
        super().__init__(holder_name, balance)
        self.interest_rate = interest_rate

    def final_balance(self):
        interest = self.balance * self.interest_rate / 100
        return self.balance + interest


a = SavingsAccount("Nishitha", 10000, 5)

print("Final Balance:", a.final_balance())




class Company:
    def __init__(self, company_name):
        self.company_name = company_name


class Employee(Company):
    def __init__(self, company_name, employee_name, salary):
        super().__init__(company_name)
        self.employee_name = employee_name
        self.salary = salary

    def display(self):
        print(self.company_name)
        print(self.employee_name)
        print(self.salary)


e = Employee("Infosys", "Aparna", 40000)
e.display()




class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Employee(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary


class Manager(Employee):
    def __init__(self, name, age, salary, team_size):
        super().__init__(name, age, salary)
        self.team_size = team_size

    def display(self):
        print(self.name, self.age, self.salary, self.team_size)


m = Manager("Aparna", 30, 60000, 10)
m.display()



class Vehicle:
    def __init__(self, brand):
        self.brand = brand


class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model


class ElectricCar(Car):
    def __init__(self, brand, model, battery):
        super().__init__(brand, model)
        self.battery = battery

    def display(self):
        print(self.brand, self.model, self.battery)


e = ElectricCar("Tesla", "Model 3", "75 kWh")
e.display()




class Student:
    def __init__(self, name, course):
        self.name = name
        self.course = course


class GraduateStudent(Student):
    def __init__(self, name, course, degree):
        super().__init__(name, course)
        self.degree = degree


class ResearchStudent(GraduateStudent):
    def __init__(self, name, course, degree, topic):
        super().__init__(name, course, degree)
        self.topic = topic

    def display(self):
        print(self.name, self.course, self.degree, self.topic)


r = ResearchStudent("Nishitha", "AIML", "MTech", "Machine Learning")
r.display()




class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print("Animal eats")


class Mammal(Animal):
    def __init__(self, name, hair):
        super().__init__(name)
        self.hair = hair


class Dog(Mammal):
    def __init__(self, name, hair, breed):
        super().__init__(name, hair)
        self.breed = breed

    def bark(self):
        print("Dog barks")


d = Dog("Tommy", True, "Labrador")

print(d.name)
print(d.breed)
d.eat()
d.bark()




class Father:
    def __init__(self, father_name):
        self.father_name = father_name


class Mother:
    def __init__(self, mother_name):
        self.mother_name = mother_name


class Child(Father, Mother):
    def __init__(self, father_name, mother_name, child_name):
        Father.__init__(self, father_name)
        Mother.__init__(self, mother_name)
        self.child_name = child_name

    def display(self):
        print(self.father_name)
        print(self.mother_name)
        print(self.child_name)


c = Child("Ravi", "Lakshmi", "Anu")
c.display()




class Printer:
    def print_document(self):
        print("Printing document")


class Scanner:
    def scan_document(self):
        print("Scanning document")


class Machine(Printer, Scanner):
    pass


m = Machine()
m.print_document()
m.scan_document()




class Teacher:
    def teach(self):
        print("Teaching students")


class Researcher:
    def research(self):
        print("Doing research")


class Professor(Teacher, Researcher):
    pass


p = Professor()
p.teach()
p.research()




class Developer:
    def develop(self):
        print("Developing application")


class Designer:
    def design(self):
        print("Designing UI")


class UIDeveloper(Developer, Designer):
    pass


u = UIDeveloper()
u.develop()
u.design()





class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


class Developer(Employee):
    def __init__(self, name, salary, language):
        super().__init__(name, salary)
        self.language = language

    def display(self):
        print(self.name, self.salary, self.language)


class Tester(Employee):
    def __init__(self, name, salary, tool):
        super().__init__(name, salary)
        self.tool = tool

    def display(self):
        print(self.name, self.salary, self.tool)


d = Developer("Rahul", 50000, "Python")
t = Tester("Anu", 45000, "Selenium")

d.display()
t.display()





class Animal:
    def __init__(self, name):
        self.name = name


class Dog(Animal):
    def sound(self):
        print(self.name, "Barks")


class Cat(Animal):
    def sound(self):
        print(self.name, "Meows")


class Cow(Animal):
    def sound(self):
        print(self.name, "Moos")


Dog("Tommy").sound()
Cat("Kitty").sound()
Cow("Ganga").sound()





class Vehicle:
    def __init__(self, brand):
        self.brand = brand


class Car(Vehicle):
    def display(self):
        print("Car:", self.brand)


class Bike(Vehicle):
    def display(self):
        print("Bike:", self.brand)


class Bus(Vehicle):
    def display(self):
        print("Bus:", self.brand)


Car("Toyota").display()
Bike("Honda").display()
Bus("Volvo").display()




class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


class Developer(Employee):
    def develop(self):
        print("Developer")


class Tester(Employee):
    def test(self):
        print("Tester")


class TeamLead(Developer, Tester):
    def __init__(self, name, salary, team_size):
        Employee.__init__(self, name, salary)
        self.team_size = team_size

    def display(self):
        print(self.name)
        print(self.salary)
        print(self.team_size)
        self.develop()
        self.test()


t = TeamLead("Nishitha", 70000, 8)
t.display()




class Device:
    def __init__(self, brand):
        self.brand = brand


class Phone(Device):
    def call(self):
        print("Making a call")


class Camera(Device):
    def take_photo(self):
        print("Taking photo")


class Smartphone(Phone, Camera):
    def __init__(self, brand, model):
        Device.__init__(self, brand)
        self.model = model

    def display(self):
        print(self.brand, self.model)


s = Smartphone("Samsung", "S23")

s.display()
s.call()
s.take_photo()





class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student(Person):
    def __init__(self, name, age, course):
        super().__init__(name, age)
        self.course = course


class Employee(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary


class Intern(Student, Employee):
    def __init__(self, name, age, course, salary, duration):
        Person.__init__(self, name, age)
        self.course = course
        self.salary = salary
        self.duration = duration

    def display(self):
        print(self.name)
        print(self.age)
        print(self.course)
        print(self.salary)
        print(self.duration)


i = Intern("Nishitha", 22, "AIML", 15000, "6 Months")
i.display()





class Library:
    def __init__(self, library_name):
        self.library_name = library_name


class Book(Library):
    def __init__(self, library_name, title, author, price):
        super().__init__(library_name)
        self.title = title
        self.author = author
        self.price = price


class EBook(Book):
    def __init__(self, library_name, title, author, price, file_size):
        super().__init__(library_name, title, author, price)
        self.file_size = file_size

    def display(self):
        print("Library:", self.library_name)
        print("Title:", self.title)
        print("Author:", self.author)
        print("Price:", self.price)
        print("File Size:", self.file_size)


b = EBook("City Library", "Python", "Guido", 500, "10 MB")
b.display()





class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email


class Customer(User):
    def __init__(self, name, email, address):
        super().__init__(name, email)
        self.address = address


class Seller(User):
    def __init__(self, name, email, shop):
        super().__init__(name, email)
        self.shop = shop


class Marketplace(Customer, Seller):
    def __init__(self, name, email, address, shop):
        User.__init__(self, name, email)
        self.address = address
        self.shop = shop

    def display(self):
        print("Name:", self.name)
        print("Email:", self.email)
        print("Address:", self.address)
        print("Shop:", self.shop)


m = Marketplace("Nishitha", "n@example.com", "Hyderabad", "Tech Store")
m.display()





class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student(Person):
    def __init__(self, name, age, course):
        super().__init__(name, age)
        self.course = course


class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject


class Assistant(Student, Teacher):
    def __init__(self, name, age, course, subject):
        Person.__init__(self, name, age)
        self.course = course
        self.subject = subject

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Course:", self.course)
        print("Subject:", self.subject)


a = Assistant("Nishitha", 22, "AIML", "Python")
a.display()




class Account:
    def __init__(self, holder, number, balance):
        self.holder = holder
        self.number = number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient Balance")

    def display(self):
        print(self.holder, self.number, self.balance)


class Savings(Account):
    def interest(self):
        print("Savings account")


class Current(Account):
    def overdraft(self):
        print("Current account")


s = Savings("Nishitha", 12345, 10000)
s.deposit(5000)
s.withdraw(2000)
s.display()
s.interest()

c = Current("Aparna", 67890, 20000)
c.display()
c.overdraft()




class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print("Name:", self.name)
        print("Salary:", self.salary)


class Developer(Employee):
    def __init__(self, name, salary, language):
        super().__init__(name, salary)
        self.language = language

    def develop(self):
        print("Language:", self.language)


class Tester(Employee):
    def __init__(self, name, salary, tool):
        super().__init__(name, salary)
        self.tool = tool

    def test(self):
        print("Testing Tool:", self.tool)


class TeamLead(Developer, Tester):
    def __init__(self, name, salary, language, tool, team_size):
        Employee.__init__(self, name, salary)
        self.language = language
        self.tool = tool
        self.team_size = team_size

    def display(self):
        print("Name:", self.name)
        print("Salary:", self.salary)
        print("Language:", self.language)
        print("Tool:", self.tool)
        print("Team Size:", self.team_size)


t = TeamLead("Nishitha", 80000, "Python", "Selenium", 10)
t.display()





