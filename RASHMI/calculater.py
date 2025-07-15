# def add(a, b):
#      return a+b
# def sub(a, b):
#      return a - b
# def mul(a, b):
#       return a * b
# def div(a, b):
#       return a / b
#
# total1 = add(10,20)
# print(total1)
# total2 = sub(10,20)
# print(total2)
# total3 = mul(10,20)
# print(total3)
# total4 = div(10,20)
# print(total4)
from unittest import case


# we can do even like this
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b
# while True: if we use while loop use break,.. If we dont use break it will go to infinite loop
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))

    operation = int(input("Enter operation: \n 1.add \n 2.sub \n 3.mul \n 4.div \n"))
#\t-tab space. \n next line
    match operation:
        case 1:
             print("your addition result is: ", add(num1, num2))
        case 2:
             print("your subtraction result is: ", sub(num1, num2))
        case 3:
             print("your multiplication result is: ", mul(num1, num2))
        case 4:
             print("your division result is: ", div(num1, num2))

             # break
        case _:
             print("invalid operation")



