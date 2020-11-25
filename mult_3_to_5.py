def multi(limit):
    i=0
    s=0
    while i<=limit:
        if i%3==0 or i%5==0:
            s=s+i
        i=i+1
    print(s)
limit=int(input("enter the number="))
multi(limit)
