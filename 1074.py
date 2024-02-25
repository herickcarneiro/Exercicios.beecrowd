n = int(input())

for x in range(1, n+1):
    n = int(input())
    if n<0:
        if n%2==0:
            print("EVEN NEGATIVE")
        else:
            print("ODD NEGATIVE")
    else:
        if n%2==0:
            print("EVEN POSITIVE")
        else:
            print("ODD POSITIVE")