balance = int(input("Enter balance: "))
withdrawal = int(input("Enter amount withdrawal: "))

if withdrawal<=balance:
    if withdrawal>0:
        print("collect amount")
    else:
        print("Invalid amount")
else:
    print("Insufficient balance")




