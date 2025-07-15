# List is mutable, ordered collection of data

#Properties
#Ordered
#Mutable
#Allows Duplicates
# takes heterogeneous data

# In other langauages we have arrays--> int arr[]

a=[1, "Hello" , 10.5, True]


mylist=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
anotherlist = list(range(2, 101, 2))


print(mylist)
print(anotherlist)
print(mylist[2])
print(mylist[3:8]) #to slice, or to run part of the list
print(mylist[-8:8])
mylist.append(12)# for append
mylist.insert(5,     3000) # for inserting
print(mylist[2:])
mylist.remove(3000)
print(mylist)
mylist.pop()


#OTHER FUNCTIONS
mylist.sort()
print(mylist)


# for i in mylist:
#     print(i, end=" ")


















