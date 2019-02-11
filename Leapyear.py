ma=int(input())
if ma%4==0:
    if ma%100==0:
        if ma%400==0:
            print("yes")
        else:
            print("no")
    else:
        print("yes")
else:
    print("no")
