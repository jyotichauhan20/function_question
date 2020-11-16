def sort ():
    empty=[]
    i=0
    while i<len(list1):
        j=i+1
        while j<len(list1):
            if list1[i]>list1[j]:
                swap=list1[i]
                list1[i]=list1[j]
                list1[j]=swap
            j=j+1
        empty.append(list1[i])
        i=i+1
    print(empty)
list1=[6,8,4,3,9,560,34,7,15]
sort()