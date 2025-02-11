
# def m(x,y):
#     while x<=y :
#         yield x
#         x+=1
    
# g=m(1,10)
# for y in g:
#     print(y)

# #  wap to febonacis series for the 5 numberss.. :)


# for i in range (0,15):
#     i+=1
# #     print(i)
# i=1
# while (i<20):
#     i+1
#     print(i)

# import tkinter
# top = tkinter.Tk()
# top.mainloop()

# from tkinter import * 

# top =Tk()
# CheckVar1= IntVar()
# CheckVar2= IntVar()
# C1=Checkbutton, top,Text="MUsic" , Variable =CheckVar1,onvalue=1,offvalue=0,height=5,width =2
# C2=Checkbutton,top,Text="MUsic" , Variable =CheckVar2,onvalue=1,offvalue=0,height=5,width =20,

from tkinter import *
from tkinter import messagebox

top = Tk()
top.geometry('200x200')
def hello ():
    messagebox.showinfo("SAy Hello", "Hello world")

E1= Entry(top,bd=5)
E1.pack()

E2=Entry(top, bd =5 )
E2.pack()

B1= Button(top,text= "Say Hello",command=hello)
B1.pack()

top.mainloop()