 def min(list1):
    i=0
    min1=list1[i]
    while i<len(list1):
        if list1[i]<min1:
            min1=list1[i]
        i=i+1
    return(min1)
num=[8,6,4,8,4,50,2,7]
print(min(num))