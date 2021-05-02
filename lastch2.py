dict = {}
zdict= {}

string = input()
chstring = input()
fstring = input()
zstring = input()

for i in range(len(string)):
    if string[i] not in dict:
        dict[string[i]]=chstring[i]
for i in range(len(string)):
     if chstring[i] not in zdict:
        zdict[chstring[i]]=string[i]


for i in range(len(fstring)):
   print(dict[fstring[i]],end="")

for  i in range(len(zstring)):
    if i == 0:
        print('\n',zdict[zstring[i]],end="")
    else:
        print(zdict[zstring[i]],end="")