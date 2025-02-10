
#Perimeter of Circle
pi=3.14
r=int(input('Enter the radius: '))
perimeter=2*pi*r
print(perimeter)

#Perimeter of Square
side=int(input("Enter a side of square"))
perimeter=4*side
print(perimeter)

#Perimeter of rectangle
l=int(input("Enter the length: "))
b=int(input("Enter the breadth: "))
perimter=2*(l+b)
print(perimeter)

#Perimeter of Triangle
a=int(input("Enter 1st side of the triangle: "))
b=int(input("Enter 2nd side of the triangle: "))
c=int(input("Enter 3rd side of the triangle: "))
perimeter=a+b+c
print(perimeter)    

#Area of circle
pi=3.14
r=int(input('Enter the radius: '))
area=pi*(r**2)
print(area)

#Area of square
side=int(input("Enter a side of square"))
area=side**4
print(area)

#Area of Rectangle

44
343
434
l=int(input("Enter the length: "))
b=int(input("Enter the breadth: "))
area=l*b
print(area)

#Area of a triangle
base=int(input("Enter the base of the triangle: "))
alt=int(input("Enter the altitude of the triangle: "))
area=0.5*base*alt
print(area)

#Area and Volume of 3d Circle
area = 4 * pi * r ** 2
volume = (4/3) * pi * r ** 3
print(area)
print(volume)

#Area and Volume of 3d Cube
area = 6 * side ** 2
volume = side ** 3
print(area)
print(volume)

#Area and Volume of Cuboid
l=int(input("Enter the length of the cuboid: "))
b=int(input("Enter the breadth of the cuboid: "))
h=int(input("Enter the height of the cuboid: "))
area = 2 * (l * b + b * h + h * l)
volume = l * b * h

#Area and volume of the Cone
r=int(input("Enter the radius of the cone: "))
h=int(input("Enter the height of the cone: "))
l =(r ** 2 + h ** 2)**0.5
area = pi * r * (r + l)
volume = (1/3) * pi * r ** 2 * h
