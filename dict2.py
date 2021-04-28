d ={}
strwar = [a.lower() for a in input().split()]

def coll(string,dict):
    for i in string:
        if i not in d:
            d[i]=1
        elif i in d:
            d[i]+=1

coll(strwar,d)
for key,value in d.items():
    print(key,value)