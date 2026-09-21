#String Task

#1. Upper & Lower

'''name=input("Enter your name:")
print(name.upper())

name=input("Enter your name:")
print(name.lower())

'''

#2. Swapcase

'''name=input("Enter your name:")
print(name.swapcase())
'''

#3. Capitalize

'''name=input("Enter your name:")
print(name.capitalize())
'''

#4. Startswith

'''name=input("Enter name:")
print(name.startswith('Python'))
'''

#5. Endswith
'''
file_name=input("Enter file name:")
print(file_name.endswith('.py'))

'''
#6. Replace

'''a="Gowsik is learning java"
print(a.replace('java','python'))
'''

#7 strip
'''
a="     Hello   "
print(a.strip())
print(a.lstrip())
print(a.rstrip())

'''

#8 split

'''a=" ram is a player"
print(a.split())

'''


# Formatting methods

#9 Format
'''a=str(input("Enter name:"))
b=int(input("I am years"))
c=str(input("I live in:"))
print(f"My name is{a}")
print(f"I am {b} years old")
print(f"I live in{c}")

'''

#10 Center

'''a=str(input('Enter your words:'))
print(a.center(20))
'''

#11 L just

'''a=str(input("Enter sentence:"))
print(a.ljust(20))

#12 R just

a=str(input("Enter sentence:"))
print(a.rjust(20))
'''

#13 Zfill

'''a=(input("Enter a number:"))
print(a.zfill(6))

'''

#Checking methods

#14 Isdigit

'''a=str(input("Enter your name:"))
print(a.isdigit())

'''

#15 isalpha

'''a=str(input("Enter letters"))
print(a.isalpha())
'''


#16 Isascii

'''a=str(input("Enter sentence:"))
print(a.isascii())
'''

#17 Combined Tasks

'''a=str(input("Enter your username:"))
print(a.strip())
print(a.capitalize())
print(a.startswith('A'))

'''

#18 Input a filename and heck

'''file=str(input("Enter your file name:"))
print(file.isascii())
print(file.endswith(".py"))
print(file.isalnum())
'''


#19 Input a mobile number and

'''a=(input("Enter your mobile number:"))
print(a.isdigit())
print(a.zfill(15))
'''

#20 Input a sentence and:

'''a=input("Enter a sentence:")
print(a.upper())
print(a.replace('g','a'))
print(a.split())
'''

#21 for else task

#print numbers 1 to 5 usinf for else

'''for i in range(1,6):
    print(i)
    
else:
    print("Loop completed")

'''
#print even numbers from 1 to 10 using for else

'''for i in range(1,11):
    if i%2==0:
        print(i)

else:
    print("Loop completed")

'''

# print each character in "python"for using for else

'''a="python"
for i in a:
    print(i)

else:
    print("Loop completed")
'''

# search for 5 in [1,2,3,4,5]

'''a=[1,2,3,4,5]
print(5 in a)
'''


# search for 10 in [2,4,6,8]

'''a=[2,4,6,8]
print(10 in a)

'''

# search for the letter in ap
'''a="apple"
print(a.find('a'))
'''


































































