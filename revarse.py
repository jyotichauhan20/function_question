def rev(string):
    rev=0
    rev=len(string)-1
    while rev>=0:
        print(string[rev])
        rev=rev-1
string=input("enter the input=")
rev(string)


