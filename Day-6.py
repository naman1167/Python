### Loops Control in Pyhton...>>>
# two types of loop statements
#  while and for 
# to print numbers from 1 to 10
# i=1 # counter intialisation   (Step-1)
# while(i<=10) :         # condition   (STEP-2)
#     print(i,end=" ")          # loop body  (Step-3)
#     i=i+1                       # incrememnt        (STEP-4) , after STEP-4 ,after step 4 goto STEP 2
# print("End of Loop")

# ###  ISS Code 10 to 1 countin hogiii...>>

# i=10 # counter intialisation   (Step-1)
# while(i>=1) :         # condition   (STEP-2)
#     print(i,end=" ")          # loop body  (Step-3)
#     i=i-1                       # incrememnt        (STEP-4) , after STEP-4 ,after step 4 goto STEP 2
# print("End of Loop")
# # if you will comment out incremnet or decrement then it is an infinite looppp!!!

# a = int(input("till what number you want to print"))
# for i in range (1,a)  :
#     print(i,end=" ")

#     print("End of looop")


# a = int(input("till what number you want to print"))
# for i in range (1,a,2)  :
#     print(i,end=" ")

#     print("End of looop")

# a = int(input("till what number you want to print"))
# for i in range (1)  :
#     print(i,end=" ")

#     print("End of looop")

# for i in range (10,0,-1) :
#     print(i,end=" ")

#     l1 =[6,8,3,5,9]
#     for i in l1 :
#         print(i,end=" ")
for i in range(1,101):
    if(i%2==0):
        pass
    else:
        print(i,end=" ")



