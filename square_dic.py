def square_of_dic(num):
    i=1
    dic={}
    while i<=num:
        dic[i]=i*i
        i+=1
    print(dic)
num=int(input("enter the number="))
square_of_dic(num)