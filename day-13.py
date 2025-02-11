# # # # class sample:
# # # #     def __init__(self):
# # # #         self.n=int(input("enter your number"))
# # # #     def display(self):
# # # #             print("number",self.n)
# # # #     def __del__(self):
# # # #          print(" object destroyed")

# # # # obj1=sample()
# # # # obj2=sample()
# # # # print("object 1")
# # # # obj1.display()
# # # # print("object 2")
# # # # obj2.display()











# # # # class sample:
# # # #     def __init__(self):
# # # #         self.n=int(input("enter your number"))
# # # #     def display(self):
# # # #             print("number",self.n)
# # # #     def __del__(self):
# # # #          print(" object destroyed")

# # # # obj1=sample()
# # # # obj2=sample()
# # # # print("object 1")
# # # # obj1.display()
# # # # print("object 2")
# # # # obj2.display()


# # # class CSStudent :
# # #     stream="IT"
# # #     def __init__(self , name ,rollno) :
# # #         self.name = name
# # #         self.rollno = rollno

# # # a=CSStudent('ABC',1)
# # # b=CSStudent('DEF',2)

# # # print('Student1')
# # # print(a.stream)
# # # print(a.rollno)
# # # print(a.name)
# # # print('Student2')
# # # print(b.stream)
# # # print(b.rollno)
# # # print(b.name)

# # # class Constr_types :
# # #     def _init_(self,arg1=0):
# # #         data=arg1
# # #         print("Parametrised  Constructor")

# # # obj1=Constr_types()
# # # obj2=Constr_types(10)


# # class Constr_types:
# #     def __init__(self, arg1=0):  # Corrected __init__ with double underscores
# #         self.data = arg1  # Added 'self.' to make 'data' an instance variable
# #         print("Parametrised Constructor")

# # # Creating objects
# # obj1 = Constr_types()  # This will call the constructor with default arg1=0
# # obj2 = Constr_types(10)  # This will call the constructor with arg1=10

# # class constr_types :
# #     def __init__(self):
# #         print("default constructor")
# #     def __init__(self,ang1=0):
# #         data=ang1
# #         print("parametrised constructor")
# # obj1=constr_types()
# # obj2=constr_types(10)



# class students:
#     roll=0
#     sname=""

#     def setdata(self):
#         self.roll=int(input("Enter your roll no ;  "))
#         self.sname=input('Enter your name ; ')


#     def getdata(self):
#         print('Roll No; ' ,self.roll)
#         print('Name; ' ,self.sname)

# s1=students()
# s1.setdata()
# # print(getattr(s1,"sname"))

# # print(hasattr(s1,'roll '))
# # setattr(s1,)

# delattr(s1,'sname')
# print(hasattr(s1,'sname'))
# s1.getdata()


# print(students.module)
# print(students.doc)
# p={"NamansSethi...>><<()"}
# print(p)


def function():
    print("Hello Naman")
   