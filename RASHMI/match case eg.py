fruit = input("Enter fruit name: ")
match fruit:
    case "Apple":
        print("Apple")
    case "Orange":
        print("Orange")
    case "Mango":
        print("Mango")
        #case_: is the syntax given for default, like else
    case _:
        print("May be some random fruit or invalid entry")
