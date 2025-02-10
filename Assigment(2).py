# Print multiplication table of a given number
num=int(input("enter a number"))
for i in range(1,11):
    print(num,"x",i,"=",num*i)
print(" ")

# Count the total number of digits in a number
number = int(input("Enter a number: "))
digit_count = 0
while number != 0:
    number //= 10
   
    digit_count += 1
print(f"Total number of digits: {digit_count}")

#  Print list in reverse order using a loop
lis=[1,2,3,4,5,6,7]
for i in lis:
    print(lis[-i],end=" ")

# Print all prime numbers within a range
def print_prime_numbers(start, end):
    for num in range(start, end + 1):
        
        if num > 1:
            for i in range(2, int(num ** 0.5) + 1):
                if (num % i) == 0:
                    break
            else:
                print(num, end=" ")



# Display Fibonacci series up to 10 terms
def fibonacci_series(n):
    a, b = 0, 1
    count = 0
    while count < n:
        print(a, end=" ")
        a, b = b, a + b
        count += 1


# Reverse a integer number without using any built-in function
num = int(input("Enter an integer: "))
reversed_num = 0

while num > 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num //= 10

print("Reversed Number: ", reversed_num)



def count_letters_digits(input_string):
    letters = digits = 0

    for char in input_string:
        if char.isalpha():
            letters += 1
        elif char.isdigit():
            digits += 1

    print(f"Letters {letters} Digits {digits}")

    

#
def reverse_integer(n):
    reversed_num = 0
    n = abs(n)  
    while n > 0:
        digit = n % 10
        reversed_num = reversed_num * 10 + digit
        n //= 10
    return reversed_num

number = int(input("Enter an integer to reverse: "))
print(f"The reversed number is {reverse_integer(number)}.")
 
def count_letters_and_digits(s):
    letters = 0
    digits = 0
    for char in s:
        if char.isdigit():
            digits += 1
        elif char.isalpha():
            letters += 1
    return letters, digits

print("(a) Number Pattern")
for i in range(5, 0, -1): 
    for j in range(i, 0, -1):
        print(j, end=" ")
    print() 
print("-"*20)
print("(b) Star Pattern")
rows = 5
for i in range(0, rows):
    for j in range(0, i + 1):
        print("*", end=' ')
    print(" ")

for i in range(rows, 0, -1):
    for j in range(0, i - 1):
        print("*", end=' ')
    print(" ")


