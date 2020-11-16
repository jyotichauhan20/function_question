def function(list1):
    i=0
    while i<len(list1):
        if list1[i]%2==0:
            print(list1[i],"even")
        elif list1[i]=="@" and list1[i]=="#" or list1[i]=="$":
            print(list1[i],"special character")
        else:
            print(list1[i],"alphabet")
        i=i+1
list1=["jyoti",12,"@",6,"kabita",8,"#"]
function(list1)