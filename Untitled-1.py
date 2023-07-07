
                          #input(........) python
a=int(input('Enter the number of a:'))
b=int(input('Enter the number of b:'))
c=a+b
print(c)

a,b=input('Enter the name of a ,b,c:').split(',')
print(a)
print(b)

list=[]
print('Enter the list')

while True:
    para=input()
    if para:
        list.append(list)
    else:
        break
print(list)


                                               #string and string function
a='naveen kumar'
print(a)
print(a.capitalize())
print(a.count('e'))
print(a.endswith('ar'))
print(a.title())
print(a.find('e'))
print(a.find('e',5))
print(a.replace('e','a'))
print('This is upper:',a.isupper())
print('This is lower:',a.islower())
print('alfa numeruic:',a.isalnum())

k='nav\ee\hg'
print(k.splitlines())
print(k.splitlines(True))
y='this is correct'
print(y.split(" "))

z='         naveen       '
print(len(z))
print(len(z.strip()))
print(len(z.lstrip()))
print(len(z.rsplit()))

#Arthmatic operactor
a=50
b=20
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)
print(a**b)

                                              #assgiment operactor
c=40
print(c)
c+=10
print(c)
c-=10
print(c)
c=10
print(c)
c/=10
print(c)
c%=10
print(c)
c+=10
print(c)

                                           #comparison operactor or relaction
print(a==b)
print(a!=b)
print(a>b)
print(a<b)
print(a<=b)
print(a>=b)
                                         #logical operactor
print(a>=10 and b<=20)
print(a>=10 or b<=20)
print(not(a>=10 and b<=20))
#butwise operactor
print(a&b)     #and
print(a|b)     #or
print(a^b)     #xor
                                #if else statement
a=int(input('enter the number:'))
if a%2==0:
    print('this is even number')
else:
    print('this is add number')    

b=input('enter your name')
a=int(input('Enter your age'))
if a>=18:
    print(b,'your age is',a,'You are eligible for vote')
else:
    print(b,' your age is ',a,'You are not vote eligibie')    
                             #if elif else statement
a=int(input('Enter the days:'))
if a>=1 and a<=5:
    print('your amount is',a*0.5)
elif a>=6 and a<=10:
    print('Your amount is',a*1)
elif a>=11 and a<=30:
    print('your amount is',a*5)
else:
    print('your are dismissed')            
                              #nested if statement
name=(input('Enter your Name :'))
a=int(input('Enter your mark :'))
b=int(input('Enter your mark :'))
c=int(input('Enter your mark :'))
total=a+b+c
avarage=total/3
print('avarage :',avarage)
print('total :',total)
if a>35 and b>35 and c>35:
    print('Your are pass')
if avarage>=90 and avarage<=100:
    print('your grade is A')
elif avarage>=80 and avarage<90:
    print('your grade is B') 
elif avarage>=70 and avarage<80:
    print('your grade is C') 
elif avarage>35 and avarage<70:
    print('your grade is D')
else:
    print('your are  fail') 
                                        
                                               #while loop continue statement
a=1
while a<=20:
    if a%2==0:
        a=a+1
        continue
    print(a)
    a+=1

                                                #while loop  break statement
a=1 
while a<=10:
    if a==8:
        break
    print(a)
    a+=1
                                              #For loop
for a in range(6):
    for j in range (a):    
       print('*',end="  ")
    print("")

for a in range(5,0,-1):
    for b in range(a):
        print('*',end="  ")
    print('  ')  
    

# A-z  => 65 to 90
# a-z  => 97 to 122

for a in range(6):
    for b in range(a):
        print((b),end="  ")
    print(a)
                                     #List
a=[1,2,3,4,5,6]
b=[0,9,8,7,6]
print(a)
print(a.count(5))
print(len(a))
print(max(a))
print(min(a))
a.pop(0)          #index value remove
a.remove(5)
a.extend(b)
print(a)
a.insert(0,'naveen')
a.append('naveen')
print(a)
print(list(range(1,6)))
print(list('naveen'))
print('------------------------------------')
a=[9,7,9,4,8,4]
print(a)
a.sort()
print(a)
a.sort(reverse=True)
print(a)
b=['naveen','kumar','kavi']
b.sort(key=len)
print(b)
print('======================================')

a=[1,2,3,4,5,6,'next']
b=tuple(a)*4
c=set(a)
a.remove('next')
c.remove('next')
c.discard(6)
print(a)
print(b)
print(c)

print('================================================================================================')
                                            #def statement
a=int(input('Enterv the nuumber :'))
b=int(input('Enterv the nuumber :'))
def add():
    c=a+b
    return c
def sub():
    c=a-b
    return c
def mul():
    c=a*b
    return c
def div():
    c=a/b
    return c 

w=add()               
x=sub() 
y=mul() 
z=div() 

                                  #No return type without argument


def add ():
    a=int(input('Enterv the nuumber :'))
    b=int(input('Enterv the nuumber :'))
    c=a+b
    print(c)

add() 
                                 #No return type with argument                                   
def sub (a,b):
    c=a-b
    print(c)

sub(25,15)  

                               #Return type without argument

def mul (): 
    a=int(input('Enterv the nuumber :'))
    b=int(input('Enterv the nuumber :'))
    c=a*b
    return c

x=mul()
print(x)
 
                               #Return type with argument
def div (a,b):
    c=a/b
    return c

x=div(3,9)
print(x)    

                          #Arbitrary Argument Function in python (*)
def a (*student):
    print(student) 
    for b in student:
        print(b)


a('naveen','kumar','kaviya','pavithra')

                       #keyword Argument Function in python (*)
def value (name,age):
    print(name,'age is',age) 

value(name='naveen',age=5)                          
value(name='naveen kumar',age=25)

                          #Arbitary keyword Argument in python  (**)
def a (**value):
    print(value)
    for b in value:
        print(b)


a(name='naveen',age='24',sex='mail',marical_ststus='single')    

                                    #Defult perameter function in python
def a (name,age,city='madurai'):
    print(name,'age is',age,'come from ',city)

a('naveen',24,'coimbatore') 
a('kumar',24)

                                        #recursive function
def factorial (a):
    if a==1:
        return 1
    else:
        return(a * factorial(a-1))

print('Factorial is :',factorial(7))

import datetime as dt
current_date=dt.date.today()
print(current_date)

current_time=dt.datetime.now()
print(current_time)

new=dt.date.today()
new=dt.datetime.now()
print(new)

import math
print(math.ceil(2.11111))
print(math.sqrt(2.44444))
print(math.factorial(10))
print(math.fabs(-10))
print(math.pow(2,5))
print(math.log2(9))
print(math.pi)
print(math.e)
print(math.isclose())


                                          #try block in python
try:
    a=10/25 
    print(b) 
except Exception as e :
    print(e)
else:
    print('A value:',a)
finally:
    print('thank you')                                                      

class student ():
    name='naveen'
    age='20'
    dob='24 & 06 & 2003'
print(student.name)
print(student.age)
print(student.dob)
student.gender='mail'
print(student.gender)
student.city='madurai'
print(student.city)
del student.age
print(student.__dict__)
                                            #Method class in python
                         
class student:
    name='naveen'
    age='20' 

    def printall():
       print('name :',student.name)
       print('age :',student.age)

student.printall()
print(student.__dict__)
getattr(student,'printall')()
print(getattr(student,'printall'))

                                        #_init_ method in class
class user:
    def _init_(self,name):
        print('Your name is :')
        self.name=name

    def printall(self):
        print('name :',self.name)

o=user()
o=printall()


























































