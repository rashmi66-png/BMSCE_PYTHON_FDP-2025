name=input("Enter your name: ")
age= int(input("Enter your age: "))
empID = input("Enter your empID: ")
#This line below is without formatted string
print("Your name is " + name + "and your age is " + str(age) + " and your empID is:" ,empID)

#This is an example of formatted strings
print(f"Your name is {name} and your {age} is age and your empID is {empID}")

