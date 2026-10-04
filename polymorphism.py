class Animal:
    def sound(self):
        print("Animal makes sound")


class Dog(Animal):
    def sound(self):
        print("Dog barks")


class Cat(Animal):
    def sound(self):
        print("Cat meows")


class Cow(Animal):
    def sound(self):
        print("Cow moos")


Dog().sound()
Cat().sound()
Cow().sound()




class Payment:
    def pay(self):
        print("Payment")


class UPI(Payment):
    def pay(self):
        print("Payment through UPI")


class CreditCard(Payment):
    def pay(self):
        print("Payment through Credit Card")


class Cash(Payment):
    def pay(self):
        print("Payment through Cash")


UPI().pay()
CreditCard().pay()
Cash().pay()




class Employee:
    def calculate_salary(self):
        pass


class FullTimeEmployee(Employee):
    def calculate_salary(self):
        print("Full-time Salary:", 30000)


class PartTimeEmployee(Employee):
    def calculate_salary(self):
        hours = 80
        rate = 200
        print("Part-time Salary:", hours * rate)


FullTimeEmployee().calculate_salary()
PartTimeEmployee().calculate_salary()




class Employee:
    def calculate_salary(self):
        pass


class FullTimeEmployee(Employee):
    def calculate_salary(self):
        print("Full-time Salary:", 30000)


class PartTimeEmployee(Employee):
    def calculate_salary(self):
        hours = 80
        rate = 200
        print("Part-time Salary:", hours * rate)


FullTimeEmployee().calculate_salary()
PartTimeEmployee().calculate_salary()





class Shape:
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        print("Circle Area:", 3.14 * self.radius * self.radius)


class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        print("Rectangle Area:", self.length * self.breadth)


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        print("Square Area:", self.side * self.side)


Circle(5).area()
Rectangle(10, 5).area()
Square(4).area()




class Vehicle:
    def start(self):
        pass


class Car(Vehicle):
    def start(self):
        print("Car starts with key")


class Bike(Vehicle):
    def start(self):
        print("Bike starts with button")


class Bus(Vehicle):
    def start(self):
        print("Bus starts with engine")


vehicles = [Car(), Bike(), Bus()]

for v in vehicles:
    v.start()




class Calculator:
    def add(self, a, b, c=0):
        return a + b + c


c = Calculator()

print(c.add(5, 10))
print(c.add(10, 10, 10))
print(c.add(20, 20, 20))




class EmailNotification:
    def send(self):
        print("Sending Email")


class SMSNotification:
    def send(self):
        print("Sending SMS")


class WhatsAppNotification:
    def send(self):
        print("Sending WhatsApp Message")


def notify_user(notification):
    notification.send()


notify_user(EmailNotification())
notify_user(SMSNotification())
notify_user(WhatsAppNotification())




class Bank:
    def interest_rate(self):
        pass


class SBI(Bank):
    def interest_rate(self):
        return 7


class HDFC(Bank):
    def interest_rate(self):
        return 7.5


class ICICI(Bank):
    def interest_rate(self):
        return 8


def display_rate(bank):
    print("Interest Rate:", bank.interest_rate(), "%")


display_rate(SBI())
display_rate(HDFC())
display_rate(ICICI())




a = [1, 2, 3]
b = (1, 2, 3)
c = "Python"
d = {"name": "Nishitha"}

print(len(a))
print(len(b))
print(len(c))
print(len(d))

print(type(a))
print(type(b))
print(type(c))
print(type(d))





class Food:
    def prepare(self):
        pass


class Pizza(Food):
    def prepare(self):
        print("Preparing Pizza")


class Burger(Food):
    def prepare(self):
        print("Preparing Burger")


class Biryani(Food):
    def prepare(self):
        print("Preparing Biryani")


def order_food(food):
    food.prepare()


order_food(Pizza())
order_food(Burger())
order_food(Biryani())




class Book:
    def __init__(self, pages):
        self.pages = pages

    def __add__(self, other):
        return self.pages + other.pages


book1 = Book(150)
book2 = Book(200)

print("Book 1 pages:", book1.pages)
print("Book 2 pages:", book2.pages)
print("Total pages:", book1 + book2)




class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __gt__(self, other):
        return self.price > other.price


p1 = Product("Laptop", 60000)
p2 = Product("Mobile", 40000)

if p1 > p2:
    print(p1.name, "has higher price")
else:
    print(p2.name, "has higher price")





class Audio:
    def play(self):
        print("Playing Audio")


class Video:
    def play(self):
        print("Playing Video")


class Podcast:
    def play(self):
        print("Playing Podcast")


def play_media(media):
    media.play()


play_media(Audio())
play_media(Video())
play_media(Podcast())





class Employee:

    @classmethod
    def company_info(cls):
        print("Employee works in a company")


class Developer(Employee):

    @classmethod
    def company_info(cls):
        print("Developer works in an IT company")


class DataAnalyst(Employee):

    @classmethod
    def company_info(cls):
        print("Data Analyst works in a data company")


Developer.company_info()
DataAnalyst.company_info()




class Electronics:
    def __init__(self, price):
        self.price = price

    def calculate_discount(self):
        return self.price * 20 / 100


class Clothing:
    def __init__(self, price):
        self.price = price

    def calculate_discount(self):
        return self.price * 10 / 100


class Grocery:
    def __init__(self, price):
        self.price = price

    def calculate_discount(self):
        return self.price * 5 / 100


def display_price(product):
    discount = product.calculate_discount()
    final_price = product.price - discount

    print("Original Price:", product.price)
    print("Discount:", discount)
    print("Final Price:", final_price)
    print()


display_price(Electronics(50000))
display_price(Clothing(5000))
display_price(Grocery(3000))






