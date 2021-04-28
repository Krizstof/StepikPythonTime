"""
https://stepik.org/lesson/3373/step/7
"""
dict={}
xi = int(input())
for i in range(xi):
    num = int(input())
    if num not in dict:
        dict[num]=f(num)
        print(dict[num])
    else:
        print(dict[num])
