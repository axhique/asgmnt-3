def calc():
    a=input("Enter :")
    upc =0
    lwc =0
    up_case = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    lw_case = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    
    
    for i in a:
        for j in up_case:
            if j==i :
                upp +=1
    
    for k in a:
        for p in lw_case:
            if p==k:
                lww +=1
                
    print( 'Upper case :',upc ,'\nLower case :',lwc)
     

print(calc())



# sample input :

#  Enter :CArs Go on The road
#  Upper case : 4
#  Lower case : 11