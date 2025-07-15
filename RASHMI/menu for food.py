
while True:
    Menu = input("Enter a food item: ")
    match Menu:
        case "1":
            print("Idli")
        case "2":
            print("shavige bath")
        case "3":
            print("burger")
        case "4":
            print("chat")
        case "5":
            print("icecream")
        case "6":
            print("Exit")
            break
        case _:
            print("invalid entry")
