#Operators
#1.Arithmetic Operators
a=int(input("A:"))
b=int(input("B:"))
print("Addition",a+b)
print("Subtraction",a-b)
print("Multipilcation",a*b)
print("Division",a/b)
print("Modulus",a%b)
print("Floor Division",a//b)
print("Exponentiation",a**b)

#Find last Digit
a=int(input("A:"))
print(a%10)

#Remove last digit
a=int(input("A:"))
print(a//10)

#Area and perimeter of Rectangle
l=int(input("Length:"))
b=int(input("Breadth:"))
print(l*b)
print(2*(l+b))


#2.Comparison Operators

#Comparing two numbers
a=int(input("A:"))
b=int(input("B:"))
print(a>b)
print(a<b)
print(a==b)


mark=int(input("Mark:"))
print(mark>=50)


#3.Logical Operators

age=int(input("Age:"))
has_id=input("Has valid id(yes/no):")
print(age>=18 and has_id=="yes")



num1=int(input("Enter your First number:"))
num2=int(input("Enter your Second number:"))
print(num1>100 or num2>100)


username=input("Username:")
password=input("Password:")
print(username=="admin" and password=="1234")

#Assignment Operators

num=100
num+=10
num-=20
num*=2
num/=2
print(num)

num=78
num+=10
num-=10
num*=2
num/=4
num%=2
num//=3
num**=2
print(num)

#Membership Operator
student=["Rasi","Sri","Anu"]
print("Rasi" in student)

fruits=["Apple","Mango"]
print("Apple"in fruits and "Mango" in fruits)

word="Python"
print("t" in word)

#Identity Operators
list1=[1,2,3]
list2=list1
print(list1 is list2)

a=[1,2,3,4]
b=[1,2,3,4]
print(a==b)
print(a is b)

#Bitwise Operators
a=int(input("A:"))
b=int(input("B:"))
print(a&b)
print(a|b)
print(a^b)
print(~a)
print((a&b)==(a|b))

#If-Else Task

#Task-1 Even or Odd

a=int(input("Enter your number:"))
if a%2==0:
    print("Even")
else:
    print("Odd")

#Task-2 Positive, Negative or Zero

num=int(input("Enter your number:"))
if num>0:
    print("Positive")
elif num<0:
    print("Negative")
else:
    print("Zero")

#Task-3 Voting Eligibility
age=int(input("Enter your age:"))
if age>=18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")

#Task-4 Biggest of two numbers
a=int(input("Enter your first number:"))
b=int(input("Enter your second number:"))
if a>b:
    print("A is bigger",a)
elif b>a:
    print("B is bigger",b)
else:
    print("both are equal")

#Task-5 Pass or fail

mark=int(input("Enter your mark:"))
if mark>=50:
    print("Pass")
else:
    print("Fail")

#Task-6 Divisible by 5

num=int(input("Enter your number:"))
if num%5==0:
    print("Divisible by 5")
else:
    print("Not divisible by 5")

#Task-7 Last digit

num=int(input("Enter your number:"))
last_digit=num%10
if last_digit %2==0:
    print(last_digit,"is Even")
else:
    print(last_digit,"is Odd")


#Task-8 Simple Login
    
username=(input("Enter your name:"))
password=input("Enter your password:")
if username=="admin" and password=="1234":
    print("Login Successful")
else:
    print("Invalid Login")







