#Selection condition flow

#If-Else Tasks

'''a=int(input("Enter your number:"))
if a%2==0:
    print("Even")
else:
    print("Odd")
'''

'''age=int(input("Enter your age:"))
if age>=18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")
'''

'''num=int(input("Enter your Number:"))
if num>0:
    print("Positive")
else:
    print("Negative")
'''


'''mark=int(input("Mark:"))
if mark>=35:
    print("Pass")
else:
    print("Fail")
'''

'''num=int(input("Enter your number:"))
if num%5==0:
    print("Divisible by 5")
else:
    print("Not divisible by 5")
'''


#Elif tasks

'''mark=int(input("Enter your mark:"))
if mark>100 or mark<0:
    print("Invalid mark")
elif mark>=90:
    print("Grade A")
elif mark>=75:
    print("Grade B")
elif mark>=50:
    print("Grade C")
elif mark>=35:
    print("Grade D")
else:
    print("Fail")
'''

'''a=int(input("Enter your First number:"))
b=int(input("Enter your Second number:"))
c=int(input("Enter your Third number:"))
if a>=b and a>=c:
    print("1st number is largest number")
elif b>=a and b>=c:
    print("2nd number is largest number")
else:
    print("3rd number is largest number")
'''

'''a=int(input("Enter first number:"))
b=int(input("Enter your second number:"))
cal=input("add/sub/mul/div:")
if cal=="add":
    print(a+b)
elif cal=="sub":
    print(a-b)
elif cal=="mul":
    print(a*b)
elif cal=="div":
    print(a/b)
else:
    print("Invalid Number")
'''

'''day=int(input("Enter a number(1-7):"))
if day==1:
    print("Sunday")
elif day==2:
    print("Monday")
elif day==3:
    print("Tuesday")
elif day==4:
    print("Wednesday")
elif day==5:
    print("Thursday")
elif day==6:
    print("Friday")
elif day==7:
    print("Saturday")
else:
    print("Invalid number! please enter 1to7 only")
'''

'''units=int(input("Enter units consumed:"))
if units<=100:
    print("Category:low usage")
elif units<=200:
    print("Category: Medium usage")
elif units<=400:
    print("Category: High usage")
else:
    print("Category: Very high usage")
'''

#Nested if-else

'''age=int(input("Enter your age:"))
driving_licence=input("Do you have licence(yes/no)")
if age>=18:
    if driving_licence=="yes":
        print('you eligible for driving')
    else:
        print("You need a driving licence")
else:
    print("Not eligible")
'''

'''username=(input("Enter your username:"))
password=(input("Enter your password:"))
if username=="admin":
    if password=="1234":
        print("Login sucessfull")
    else:
        print("Incorrect password")
else:
    print("Invalid username")
'''

'''budget=int(input("Enter your budget amount:"))
brand=input("Enter your brand:")
if budget>=50000:
    if brand=="dell" or brand=="hp":
        print("you can purchase your laptop")
    else:
        print("Brand is not preferred")
else:
    print("Budget is not enough")
'''

'''attendance=int(input("Enter your attendance percentage:"))
mark=int(input("Enter your mark:"))
if attendance>=75:
    if mark>=40:
        print("Eligible and passed")
    else:
        print("Eligible but failed")
else:
    print("Not eligible for exam")
'''

'''pin=int(input("Enter your pin number:"))
amount=int(input("Enter your amount:"))
balance=10000
if pin==1234:
    if balance<=10000:
        print("Whithdraw sucessfull")
        print("Reamining balance",balance-amount)
    else:
        print("Insufficient balance")
else:
    print("Invalid password")
'''


'''age=int(input("Enter your age:"))
movie=(input("Enter your movie(action/comedy/horror):"))
tickets=int(input("Enter number of tickets:"))
if age>=18:
    if movie=="action":
        price=150
    elif movie=="comedy":
        price=200
    elif movie=="horror":
        price=300
    else:
        print("Invaid movie type")
        price=0
    total=price*tickets
    if price>0:
        print("Tickets price=",price)
        print("Total amount=",total)
else:
    print("Not eligible to watch movie")
'''    
    




   
