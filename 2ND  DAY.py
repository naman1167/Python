# DATA TYPESSS.........
str="computer science"
for (i) in str:
    print(i)
    # str= " jo bhe ander ha " woh line  me aa jayega
    print('str-', str) #print string
    print(str[7])
    # print or phir stringa ka [ke ander woh place jisko print karwaana hai ]
    print(str[0:9])# [ke ander 1:3 jaha se leke jaha tak chaiye]
    print(str[0:9:2])
#  isme 0 se 9 tak jayege or har dusra charateerr skip kar denge..
    print(str[3:])
    # isme 3 rd se shurhu hogaaa or end tak jayega 
    print(str[:3])
 # isme 3rd tak rahega sirfff.....
str2 = " \n science"
print(str+ str2)
# do string addd ho sakte h refrence ke liye upper dekhh.
print(str*3)
# str*3 yh print karoge toh string 3 baar aa jayegii neeche 
list=[6,8]
print(list[0])
# yeh string jaisa he ha 
tuple=(99,87)
print(tuple[1])
# yeh bhe string jaisa he kuch ha 
# Tuple modify nhi ho sakte list ho sakte ha 
str3 = (129,"naman", 234, 989)
print(str3)
dict1 =("roll no: 129, chort ; mz")
print(dict1)
# dict or set bhe kar sakte he define ...>(bilkul string ke tarah)

print(type(str2))
print(type(dict1))
# ise hame data ka type mil jata ha !!!!!!!
# ELIF STATEMENT 

# if condition1:
#     # code block executed if condition1 is True
# elif condition2:
#     # code block executed if condition2 is True (and condition1 was False)
# elif condition3:
#     # code block executed if condition3 is True (and the previous conditions were False)
# else:
#     # code block executed if none of the above conditions are True
