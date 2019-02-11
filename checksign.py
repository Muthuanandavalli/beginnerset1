n=input()
if n.isnumeric:
    a=int(n)
    if a>0:
        print("Positive")
    elif a<0:
        print("Negative")
    else:
        print("Zero")
else:
    print("Invalid")
    
