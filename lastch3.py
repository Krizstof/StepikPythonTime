varone = int(input())
mass = []
omass=[]
for i in range(varone):
    stringone = input().lower()
    mass.append(stringone)
varone = int(input())
for i in range(varone):
    varone = input().lower().split(" ")
    for z in varone:
        if z in mass:
            pass
        if z not in mass:
            if z not in omass:
                omass.append(z)
for i in omass:
    print(i)