a=int(input("Enter a: "))
b=int(input("Enter b: "))
c=int(input("Enter c: "))
if a>b and a>c:
    print(f"{a} is larger")
elif b>a and b>c:
    print(f"{b} is larger")
else:
    print(f"{c} is larger")
