a= int(input("Enter subject 1: "))
b = int(input("Enter subject 2: "))
c = int(input("Enter subject 3: "))
d = int(input("Enter subject 4: "))
e = int(input("Enter subject 5: "))
sum=a+b+c+d+e
percentage= (sum/500)*100
if percentage>=75:
    print("Grade is A")
elif percentage>=50 and percentage<75:
    print("Grade is B")
elif percentage>=30 and percentage<50:
    print("Grade is C")
else:
    print("Grade is F")

