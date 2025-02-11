# # class vehicle:
# #     def __init__(self):
# #         self.make=''
# #         self.model=''

# #     def DisplayDetails(self):
# #         print("Make : " , self.make, "\nModel :" ,self.model)

# # class swift(vehicle):
# #     def __init__(self):
# #         self.make=" Hundai"
# #         self.model="Dzire"


# # o2=swift()
# # o2.DisplayDetails()
        

    
# class vehicle:
#     def __init__(self,mk,md):
#         self.make=mk
#         self.model=md
        
#     def DisplayDetails(self):
#         print("Make: ",self.make,"\nModel: ",self.model)
# class swift(vehicle):
#     def __init__(self,a,b):
#         super().__init__(a,b)
#         self.speed=100
#     def speed_details(self):
#         print("speed: ",self.speed)
# o2=swift('maruti','swift')
# o2.DisplayDetails()
# o2.speed_details()


# class animal :                  
#     def speak(Self):                  
#         print("Speaking")                  

# class dog (animal):                  
#     def speak(Self) :                
#         print("Barking")                  

# d=dog()                  
# d.speak() 
# 
# 
# 


class distance:
    def __init__(self,n):
        self.n=n
    def __add__(self,d2):
        result=self.n+d2.n
        return result
    def __sub__(self,d2):
        result=self.n-d2.n
        return result
    def __lt__(self,d2):
        result=self.n<d2.n
        return result
d1=distance(5)
d2=distance(10)
print(d1+d2)
print(d1-d2)
print(d1<d2)

# build a class complex having attributes real and imaginary. and perform complex number addition and subtraction opration   




