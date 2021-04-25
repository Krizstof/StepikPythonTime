a = int(input())
b = int(input())
c = int(input())
d = int(input())
for i in range(c, d + 1):
    if i == d:
        print('\t', i)
    else:
        print('\t', i, '\t', end="")
for z in range(a, b + 1):
    print(z, end="")
    for x in range(c, d + 1):
        if x == d:
            print('\t', x * z, "\t")
        else:
            print('\t', x * z, "\t", end="")
