
while True:
    Menu = input("Enter a no: ")
    match Menu:
        case "1":
            print("Hello")
        case "2":
            print("Bye")
        case "3":
            print("Exit")
            break

        case _:
            print("invalid entry")
