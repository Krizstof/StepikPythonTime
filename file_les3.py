'''
https://stepik.org/lesson/3363/step/4?unit=1135
'''
allmath =0
alleng =0
allphus = 0
z = 0
with open ('text.txt') as inf:
  for line in inf.read().split():
      z+=1
      var = line.split(';')
      allmath+=float(var[1])
      alleng +=float(var[2])
      allphus+=float(var[3])
      with open('les.txt','a') as fin:
          sol =((float(var[1])+float(var[2])+float(var[3]))/3)
          print(sol)
          fin.write(str(sol)+'\n')

with open('les.txt','a') as fin:
    finmath = allmath/z
    fineng = alleng/z
    finphus = allphus/z
    fin.write(str(float(finmath))+' ')
    fin.write(str(float(fineng))+' ')
    fin.write(str(float(finphus))+' ') 


