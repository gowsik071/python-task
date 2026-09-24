#Set

#Create a set of 5 numbers and print it.

'''a={1,4,2,3,5}
print(a)
'''

#Add 60 to a set.

'''a={1,4,6,7,9,3}
a.add(60)
print(a)
'''

#Remove 20 from a set.

'''a={1,2,20,3,5,6,7}
a.remove(20)
print(a)
'''


#Find the length of a set.

'''a={1,2,3,6,5,7,8,10}
print(len(a))
'''


#Check whether 30 exists in a set.


'''a={2,3,4,5,10,20,30,8}
print(30 in a)
'''


#Print all elements using a for loop.


'''a={1,2,3,4,5,6}
for i in a:
    print(i)
'''

#Create a set containing duplicate values and observe the output.


'''a={1,1,2,3,4,5,6,5,4,}
print(a)
'''


#Find the maximum value in a set.


'''a={10,34,26,40,70,100,101}
print(max(a))
'''


#Find the minimum value in a set.

'''
a={10,5,34,26,40,70,100,101}
print(min(a))

'''

#Find the sum of all elements in a set.


'''a={2,4,6,8,5}
print(sum(a))
'''


#Set Operations

#Find the union of two sets.


'''a={1,2,3,4}
b={3,4,5,6}
print(a.union(b))
'''

#Find the intersection of two sets.

'''a={1,2,3,4}
b={3,4,5,6}
print(a.intersection(b))
'''

#Find the difference between two sets.

'''a={1,2,3,4}
b={3,4,5,6}
print(a.difference(b))
print(b.difference(a))
'''


#Find the symmetric difference.

'''a={1,2,3,4}
b={3,4,5,6}
print(a.symmetric_difference(b))
'''

#Check whether one set is a subset of another.

'''a={1,2,6}
b={1,2,3,4,5}
print(a.issubset(b))
'''

#Convert a list into a set to remove duplicates.

'''a=[1,3,2,5,6,3,2,7,8,7]
print(set(a))
'''

#Find common elements between two student groups.

'''group1={'arun', 'raj', 'kumar', 'nithiya'}
group2={'nithiya', 'govind', 'muni', 'raj'}
print(group1.intersection(group2))
'''


#Dictionary

#Create a dictionary containing name, age and city.

'''a={"name":"Gowsik", "age":"21" ,"city":"Japan"}
print(a)


#Print the value of "name".

print(a.get("name"))

#Add a new key "course".

a.update({"course":"python"})
print(a)

#Change the value of "age".
a.update({"age":"21","age":"22"})
print(a)

#Delete the "city" key.

a.pop("city")
print(a)


#Find the number of items in a dictionary.
print(len(a))

#Check whether "name" exists.
if "name" in a:
    print("yes name is here")
else:
    print("no name")

#Print all keys.
print(a.keys())

#Print all values.
print(a.values())

#Print both keys and values using a for loop.
for key in a:
    print(key,":",a[key])
'''

#Moderate

#Create a dictionary containing 5 students and their marks.

a={"Ragu":300,"Angel":400,"Nithiya":350,"Kanal":370,"Nadiya":380}
print(a)

#Find the student with the highest mark
print(max(a,key=a.get))

#Find the student with the lowest mark.
print(min(a,key=a.get))

#Calculate the total of all marks.
total=0
for i in a.values():
    total+=i
print(total)

#Calculate the average mark.

avg=total/len(a)
print(avg)

#Count how many students scored above 50.
count=0
for i in a.values():
    if i >50:
        count+=1
print(count)

#Search for a student by name.

name=input("Enter name:")
if name in a:
    print("marks:",a[name])
else:
    print("Student not found")

#Update a student's mark.
mark=int(input("Enter new mark:"))
a[name]=mark
print(a)
    
