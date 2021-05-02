mass=[]
dict = {}

with open ('text1.txt') as inf:
    for line in inf:
        var = line.strip().split("\t")
        mass.append(var)

for i in range(11+1):
    dict[i]=[0,0]

for i in mass:
   varz=dict[int(i[0])]
   varz[0]+=1
   varz[1]+=int(i[2])
   dict[int(i[0])]=varz
for i in range(11+1):
    varx=dict[i]
    if i == 0:
        pass
    elif varx[0]==0:
        print(i," -")
    else:
        print(i,float(varx[1]/varx[0]))
    