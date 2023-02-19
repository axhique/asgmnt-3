def sum():
    a=input("Enter the list :").split(",")
    l1=[]
    for i in a:
        l1.append(int(i))
    
    sum=0
    for j in l1:
        sum +=j
     
    print(" + ".join(a),"=",sum)
 
print(sum())