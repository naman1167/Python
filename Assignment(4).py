# 1. Write a Python class that has two methods: get_String and print_String, 
# get_String accepts a string from the user and print_String prints the string in upper case.

class TextHandler:
    txt = ""

    def get_input(self):
        self.txt = input("Enter the text: ")

    def show_uppercase(self):
        print(self.txt.upper())

# Creating an instance and using the methods
txt_handler = TextHandler()
txt_handler.get_input()
txt_handler.show_uppercase()


# 2. Write a Python program to create a calculator class. Include methods for basic arithmetic operations.

class Calculator:
    def __init__(self):
        self.n1 = 0
        self.n2 = 0

    def input_numbers(self):
        self.n1 = float(input("Enter the first number: "))
        self.n2 = float(input("Enter the second number: "))

    def add(self):
        return self.n1 + self.n2

    def subtract(self):
        return self.n1 - self.n2

    def divide(self):
        if self.n2 != 0:
            return self.n1 / self.n2
        else:
            return "Division by zero is not possible."

    def multiply(self):
        return self.n1 * self.n2

    def result(self, operator):
        if operator == "+":
            print("Result:", self.add())
        elif operator == "-":
            print("Result:", self.subtract())
        elif operator == "/":
            print("Result:", self.divide())
        elif operator == "*":
            print("Result:", self.multiply())
        else:
            print("Invalid operator.")

# Using the Calculator class
calc = Calculator()
calc.input_numbers()
calc.result(input("Enter operation (+, -, /, *): "))


# 3. Write a Python class named Circle constructed from a radius and two methods that will compute the area and the perimeter of a circle.

import math

class Circle:
    def __init__(self, rad):
        self.rad = rad

    def calc_area(self):
        return math.pi * self.rad ** 2

    def calc_perimeter(self):
        return 2 * math.pi * self.rad

# Taking input for radius and calculating area and perimeter
radius = float(input("Enter the radius: "))
circle = Circle(radius)
print("Circle Area:", circle.calc_area())
print("Circle Perimeter:", circle.calc_perimeter())


# 4. Write a Python class to implement pow(x, n).

class PowerCalc:
    def __init__(self, base, exp):
        self.base = base
        self.exp = exp

    def power(self):
        return self.base ** self.exp

# Taking inputs and calculating power
base_val = float(input("Enter the base value: "))
exp_val = int(input("Enter the exponent: "))
power_calc = PowerCalc(base_val, exp_val)
print(f"{base_val} to the power of {exp_val} is:", power_calc.power())


# 5. Write a Python program to create a class representing a shopping cart. 
# Include methods for adding and removing items, and calculating the total price.

class Cart:
    def __init__(self):
        self.items = {}

    def add_item(self, name, price):
        if name in self.items:
            print(f"{name} is already in the cart.")
        else:
            self.items[name] = price
            print(f"{name} added to the cart.")

    def remove_item(self, name):
        if name in self.items:
            del self.items[name]
            print(f"{name} removed from the cart.")
        else:
            print(f"{name} is not in the cart.")

    def total_cost(self):
        return sum(self.items.values())

    def display_cart(self):
        if not self.items:
            print("Your cart is empty.")
        else:
            print("Items in the Cart:")
            for name, price in self.items.items():
                print(f"{name}: ${price:.2f}")

# Shopping Cart usage
cart = Cart()

while True:
    print("\n1. Add item\n2. Remove item\n3. Show cart\n4. Total price\n5. Exit")
    choice = int(input("Choose an option: "))

    if choice == 1:
        item_name = input("Enter item name: ")
        price = float(input(f"Enter price of {item_name}: "))
        cart.add_item(item_name, price)
    elif choice == 2:
        item_name = input("Enter the item name to remove: ")
        cart.remove_item(item_name)
    elif choice == 3:
        cart.display_cart()
    elif choice == 4:
        print(f"Total price: ${cart.total_cost():.2f}")
    elif choice == 5:
        break
    else:
        print("Invalid choice. Try again.")


# 6. Write a Python class Employee with attributes like emp_id, emp_name, emp_salary, and emp_department. 
# Include methods to calculate salary, assign department, and print employee details.

class Employee:
    def __init__(self, name, emp_id, salary, department):
        self.name = name
        self.emp_id = emp_id
        self.salary = salary
        self.department = department

    def assign_dept(self, dept):
        self.department = dept
        print(f"{self.name} assigned to the {dept} department.")

    def calc_salary(self, hours):
        if hours > 50:
            overtime = hours - 50
            overtime_pay = overtime * (self.salary / 50)
            total_pay = self.salary + overtime_pay
        else:
            total_pay = self.salary
        return total_pay

    def print_details(self):
        print(f"Name: {self.name}")
        print(f"ID: {self.emp_id}")
        print(f"Salary: ${self.salary:.2f}")
        print(f"Department: {self.department}")

# Example usage
emp = Employee("Alex", "E001", 60000, "Finance")
emp.print_details()

hours_worked = 55
print(f"Total Salary (with {hours_worked} hours): ${emp.calc_salary(hours_worked):.2f}")
emp.assign_dept("HR")
emp.print_details()


# 7. Write a Python class BankAccount with attributes like account_number, balance, date_of_opening and customer_name, 
# and methods like deposit, withdraw, and check_balance.

class BankAccount:
    def __init__(self, acc_num, name, opening_date, balance=0):
        self.acc_num = acc_num
        self.name = name
        self.opening_date = opening_date
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"${amount} deposited. New balance: ${self.balance:.2f}")
        else:
            print("Deposit amount should be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                print(f"${amount} withdrawn. Remaining balance: ${self.balance:.2f}")
            else:
                print("Insufficient balance.")
        else:
            print("Withdrawal amount should be positive.")

    def check_balance(self):
        print(f"Current balance: ${self.balance:.2f}")

    def print_account(self):
        print(f"Account Number: {self.acc_num}")
        print(f"Customer Name: {self.name}")
        print(f"Opening Date: {self.opening_date}")
        print(f"Balance: ${self.balance:.2f}")

# Bank account usage
acc = BankAccount("987654321", "John Doe", "2024-02-01", 1000)
acc.print_account()
acc.deposit(300)
acc.withdraw(200)
acc.check_balance()


# 8. Create a class hierarchy for different types of geometric shapes, including circles, rectangles, and triangles.

class Shape:
    def __init__(self, color):
        self.color = color

    def area(self):
        pass

    def print_info(self):
        print(f"Color: {self.color}")
        print(f"Area: {self.area()}")

class Circle(Shape):
    def __init__(self, color, rad):
        super().__init__(color)
        self.rad = rad

    def area(self):
        return math.pi * self.rad ** 2

    def print_info(self):
        super().print_info()
        print(f"Radius: {self.rad}")

class Rectangle(Shape):
    def __init__(self, color, length, width):
        super().__init__(color)
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def print_info(self):
        super().print_info()
        print(f"Length: {self.length}")
        print(f"Width: {self.width}")

# Usage for shape hierarchy
circle = Circle("Red", 7)
circle.print_info()

rect = Rectangle("Blue", 5, 3)
rect.print_info()


# 9. Create a Bus child class that inherits from the Vehicle class.
# Override the fare() method to add a 10% maintenance charge to the total fare.

class Vehicle:
    def __init__(self, capacity):
        self.capacity = capacity

    def base_fare(self):
        return self.capacity * 100

class Bus(Vehicle):
    def __init__(self, capacity=50):
        super().__init__(capacity)

    def total_fare(self):
        basic_fare = super().base_fare()
        maintenance_charge = basic_fare * 0