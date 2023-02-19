def reverse():
    word=input("Enter the word :")
    l1=[]
    for i in range(len(word)-1,-1,-1):
      l1.append(word[i])
    rev="".join(l1)   
    return rev


print(reverse())