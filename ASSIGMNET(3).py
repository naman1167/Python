# Question -1
m= [1, 2, 3, 4, 5]
r= m[::-1]
print(r)

# QUESTION -2
m = [1, 2, 3, 4, 5, 2, 2]
e= int(input("Enter the element you want to be counted: "))
count = m.count(e)
print(f"The number of occurrences of {e} is: {count}")

# Question -3
m = [1, 2, 3, 4, 5, 6, 2]
for i in m :
    count = m.count(i)
count = m.count(e)
if count!=1:
    print(" This Array contain duplicate element")
else:
  print("True")

# Question -4 
def f(arr):
    expected_sum = sum(range(min(arr), max(arr) + 1))
    actual_sum = sum(arr)
    return expected_sum - actual_sum

array = [1, 2, 4, 5]
missing_number = f(array)
print("The missing number is:", missing_number)

def r(arr):
    return [-1 if x % 2 != 0 else x for x in arr]

array = [1, 2, 3, 4, 5]
m=r(array)
print("Modified array:",m)