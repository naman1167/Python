#program to remove duplicates from a list.
a=(input("Enter the numbers to remove the duplucates ")).split(" ")
a=set(a)
print((a))


#function that takes two lists and returns True if they have at least one common member.
inpu1=(input("Enter the numbers or string ")).split(" ")
inpu2=(input("Enter the second numbers or string ")).split(" ")
for i in inpu1:
    if i in inpu2:
        print(True)
        break
else:
    print(False)


#program to print the numbers of a specified list after removing even numbers from it.
input5=input("Enter the numbers to remove the duplucates ").split(" ")
input5=[int(i) for i in input5]
input5=[j for j in input5 if j%2!=0]
print(input5)



#program to find the second smallest number in a list.
# input6=input("Enter the number to temm second smallest value  ").split(" ")
# input6=[int(i) for i in input6]
# # f=min(inpu)
# input6.remove(min(input6))
# print(f"The second smalles value is {min(input6)} ")


#program to split a list every Nth element.
def split_list(input_list, n):
    return [input_list[i:i+n] for i in range(0, len(input_list), n)]
input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
n = 3
print("Original List: ", input_list)
print("Split List: ", split_list(input_list, n))

#function to find the union and intersection of two lists
input_list = [1, 2, 3, 4, ]
input_list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
input_list=set(input_list)
input_list2=set(input_list2)
print(f"union of the list {input_list ,input_list2} is \n{input_list.union(input_list2)}")
print(f"intersection of the sets 'a-b' is {input_list.intersection(input_list2)}")





#function to check if a list is a palindrome or not
inpu=input("Enter the number to cgheck the list is palandrem   ").split(" ")
inpu=[int(i) for i in inpu]
if inpu[::1]==inpu[::-1]:
    print(True)
else:
    print(False)