for i in range(5):
    for spaces in range(5 - i - 1):
        print(" ", end=' ')
    for j in range(0, 2 * i + 1):
        print("*", end=' ')
    print()

