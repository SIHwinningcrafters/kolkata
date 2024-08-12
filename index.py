'''print("hello world")
a=3
print(a)
a=5.6
print(a)
d="harry"
print(d)
e =None
print(e)
#typecasting
f="5" #ye ek string hai
print(int(f)+1)
g=5
print(g+1)
#operator
n1 =10
n2 =2
print("n1+n2 is =",n1+n2)
print("n1-n2 is =",n1-n2)
#comparison operator
x=4
y=8
print(x<y)
print(x!=y)
#logical operator
print(x==y and x<y)
#string
name="harru"
print(name[0:3])
print(name.upper())
#user input
name=input("enter your name?")
print(name)
#write a phy program to take a num from user as an input and 6 to it
num=input("enter your number=")
print(int(num)+6)
#list
L1=[3,5,4,"harry",6,9]
print(L1)
print(type(L1))
L1.remove("harry")
print(L1)
L1.count(5)
L1.append(78)
print(L1)
#set
s1={2,3,4,5,6,4,3}
s2={9,7,5,43,62,6,7}
print(s1)
print(s1.union(s2))
s1.add(43)
print(s1)
#dictionary
dict1 ={"good":"something pleasent","fetch":
        "to bring"}
print(dict1["good"])
marks={"harry":"34","muskan":"43","sakshi":"54","faiza":"32"}
print(marks["muskan"])
marks["priya"]=67
print(marks)
#if else
age=int(input("enter your age:"))
if(age>18):
    print("you can drive")
else:
     print("no you cant drive")
a=[1,23,43,54,67]
for item in a:
    print(item)
#function
def greet(name, ending):
    print("hello "+ name)
    print(ending)
greet("dipu", "thanks")
greet("harr","byy")
#except
try:
    a =int(input("enter your number:"))
    print(a+3)
except :
 print("some error occured")'''
#class
class Employee:
    salary=67
    def getsalary(self):
        return self.salary
rohan = Employee()
print(rohan.salary)
   

 
