# vars
main_mass = []

while True:
    inp = input().split()
    if inp == ['end']:
        break
    else:
        for i in range(len(inp)):
            inp[i] = int(inp[i])
        main_mass.append(inp)
for i in range(len(main_mass)):
    for j in range(len(main_mass[i])):
