l1=[10,20,30,40]
for i in l1 :
   print(i, end=" ")
   c=0
   while(c<len(l1)):
      print(l1[c])
      c=c+1 

       
# i=100
# while i>=100 and i<=200:
#     print(i, end=" ")
#     i=i+1

# s1="Computer"
# for i in s1 :
#     print(i)

# s1=input("Enter your word")
# c=0
# for i in s1 :
#     if i== '':
#         c=c+1
#         print("Number of words",c) 
# for i  in range (1,11):
#     if (i==5):
#         break
#     print(i,end=" ")

# for i in range (1,11):
#     if (i==5) :
#         continue
#     print(i, end=" ")

#     to print all odd number between 1 to 100

# for i in range(1,101) :
#         if(i%2==0) :
#             continue
#         print(i,end=" ")

# Prime Numbers 
# n=int(input("Enter the number :"))
# for i in range(2,n) :
#     if(i%2==0) :
#         flag = False
#         print("Not a prime number ")
#         break
# if(flag=True):
#     print("Prime numberrr!!!!!!!")

# for i in range(1,101):
#     if(i%2==0):
#         pass
#     else:
#         print(i,end=" ")

# for i in range (1,6):
#     for j in range(1,i+1) :
#         print("*", end=" ")
#     print(' ')

for i in range (1,6):   
    for k in range(5,i,-1) :   
        print(' ', end=" ")   
        print(" " , end="")   
        print("*", end=" ")   
    print(' ') 
   
