def rewors(reverse_list):
    list1=[]
    i=(len(reverse_list))-1
    while i>0:
        list1.append(reverse_list[i])
        i=i-1
    return(list1)
print(rewors(["Z","A","A","B","E","M","A","R","D"]))