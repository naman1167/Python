# File I/O
#  TO create the file....
#  to write the data 
f=open("/Users/namansethi/Desktop/Python file/myfile.txt","w")
f=open("/Users/namansethi/Desktop/Python file/myfile.txt","w")
data="Naman Sethi.."

f.write(data)

f.close()
#  to read the file ...
f=open("/Users/namansethi/Desktop/Python file/myfile.txt","r")

data=f.read()
print("File Contents :",data)
f.close()

f=open("/Users/namansethi/Desktop/Python file/myfile.txt","r")

data=f.readlines ()
print("Files Contents  :", data)
c=1
for line in data :
    print(c,line)
    c=c+1
f.close()

f=open("/Users/namansethi/Desktop/Python file/myfile.txt","w")
data=["Btech CS\n","ITM KHARGHAR"]
f.write(data)

f.close()