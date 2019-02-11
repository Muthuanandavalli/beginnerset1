ar=int(input())
if ar%4==0:
    if ar%100==0:
        if ar%400==0:
            print("yes")
        else:
            print("no")
    else:
        print("yes")
else:
    print("no")
