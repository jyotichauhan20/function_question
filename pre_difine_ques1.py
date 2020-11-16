def max(number):
    i=0
    max1=number[i]
    while i<len(number):
        if number[i]>max1:
            max1=number[i]
        i=i+1
    return(max1)
print(max([3,5,7,34,2,89,2,5]))

