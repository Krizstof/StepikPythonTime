varone = int(input())
mass = [0,0]
for i in range(varone):
    secondvar = input().split(" ")
    if secondvar[0] == "восток":
        mass[0]+=int(secondvar[1])
    elif secondvar[0] =="запад":
        mass[0]-=int(secondvar[1])
    elif secondvar[0] =="север": 
        mass[1]+=int(secondvar[1])
    elif secondvar[0] == "юг":
        mass[1]-=int(secondvar[1])

        
print(*mass)