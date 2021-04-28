dict = {}
with open ('text.txt') as inf:
    for line in inf.read().split():
        if line not in dict:
            dict[line] = 1
        else:
            dict[line] = dict[line]+1
p=(max(dict,key=dict.get))
m =dict.get(p)
string = (p + ' ' + str(m))
with open ('so.txt','w') as inf:
    inf.write(string)
        
     

