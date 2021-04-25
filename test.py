a = input()
var_chet= -(len(a))-1
var_lo =0
for i in a:
    var_chet+=1
    if var_chet==-1:
        var_lo+=1
        print(f'{i}{var_lo}',end='')
    elif i == a[var_chet+1]:
        var_lo+=1
    elif i != a[var_chet+1]:
        var_lo += 1
        print(f'{i}{var_lo}',end='')
        var_lo=0




