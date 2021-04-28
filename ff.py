lst =[1,2,3,4,5,6]
def modify_list(l):
    lez=len(lst)-1
    x=-1
    while lez!=x:
        x+=1
        if l[x]%2!=0:
            del l[x] 
            lez-=1
            x-=1

        else:
            l[x]=l[x]//2
print(modify_list(lst))
