n=int(input("Enter a num:"))
is_prime = True
if n<2:
    is_Prime = False
else:
    i= 2
    while i<n:
        if n%i==0:
            is_prime = False
            break
        i+=1

print("prime" if is_prime else "Not Prime")
