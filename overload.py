#Define a class Book with an integer pages attribute and overload the + operator to produce a new Book whose pages equals the sum of the two operands’ pages.
class Book:
    def __init__(self, pages):
        self.pages = pages

    def __add__(self, other):
        return Book(self.pages + other.pages)


b1 = Book(150)
b2 = Book(200)
b3 = b1 + b2

print("Book 1 Pages:", b1.pages)
print("Book 2 Pages:", b2.pages)
print("Total Pages:", b3.pages)


# output: Book 1 Pages: 150
# Book 2 Pages: 200
# Total Pages: 350


#Define a class Employee with a numeric salary attribute and overload the > operator to compare the salaries of two employees.
class Employee:
    def __init__(self, salary):
        self.salary = salary

    def __gt__(self, other):
        return self.salary > other.salary


e1 = Employee(50000)
e2 = Employee(40000)

print(e1 > e2)


#output: True

#Define a class Temperature with a numeric celsius attribute and overload the - operator to return the numeric difference between two temperatures.
class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    def __sub__(self, other):
        return self.celsius - other.celsius


t1 = Temperature(35)
t2 = Temperature(20)

print("Temperature Difference:", t1 - t2)

#output:Temperature Difference: 15



#Define a class Rectangle with length and width attributes and overload the * operator so that multiplying two rectangles yields a numeric value equal to the product of their individual areas.
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def __mul__(self, other):
        return self.area() * other.area()


r1 = Rectangle(5, 4)
r2 = Rectangle(3, 2)

print("Area Product:", r1 * r2)

# output:Area Product: 120



# Define a class Time with hours and minutes attributes and overload the + operator to add two Time objects, normalizing minutes (e.g., 70 minutes becomes 1 hour 10 minutes).
class Time:
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes

    def __add__(self, other):
        total = self.hours * 60 + self.minutes
        total += other.hours * 60 + other.minutes

        return Time(total // 60, total % 60)

    def display(self):
        print(self.hours, "hours", self.minutes, "minutes")


t1 = Time(2, 40)
t2 = Time(1, 50)

t3 = t1 + t2
t3.display()

# output:4 hours 30 minutes


# Define a class ShoppingCart that stores a collection of item prices and overload the + operator to combine two carts into a new cart containing all items from both.
class ShoppingCart:
    def __init__(self, prices):
        self.prices = prices

    def __add__(self, other):
        return ShoppingCart(self.prices + other.prices)


c1 = ShoppingCart([100, 200])
c2 = ShoppingCart([300, 400])

c3 = c1 + c2

print("Cart 1:", c1.prices)
print("Cart 2:", c2.prices)
print("Combined Cart:", c3.prices)
print("Total Price:", sum(c3.prices))

# output:Cart 1: [100, 200]
# Cart 2: [300, 400]
# Combined Cart: [100, 200, 300, 400]
# Total Price: 1000



# Define a class Distance with a numeric meters attribute and overload the +, -, and == operators to add, subtract, and compare distances respectively.
class Distance:
    def __init__(self, meters):
        self.meters = meters

    def __add__(self, other):
        return Distance(self.meters + other.meters)

    def __sub__(self, other):
        return Distance(self.meters - other.meters)

    def __eq__(self, other):
        return self.meters == other.meters


d1 = Distance(500)
d2 = Distance(300)
d3 = d1 + d2
d4 = d1 - d2

print("Addition:", d3.meters, "meters")
print("Subtraction:", d4.meters, "meters")
print("Equal:", d1 == d2)

# output:Addition: 800 meters
# Subtraction: 200 meters
# Equal: False



# Define a class Vector with x and y numeric components and overload the +, -, and * operators to perform vector addition, subtraction, and compute the dot product (*).
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return self.x * other.x + self.y * other.y

    def display(self):
        print("(", self.x, ",", self.y, ")")


v1 = Vector(2, 3)
v2 = Vector(4, 5)

print("Addition:")
(v1 + v2).display()

print("Subtraction:")
(v1 - v2).display()

print("Dot Product:", v1 * v2)


#  output:Addition:
# ( 6 , 8 )
# Subtraction:
# ( -2 , -2 )
# Dot Product: 23




