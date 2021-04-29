dict = {}
n = int(input())
for i in range(n):
    z = [a for a in input().split(";")]
    mass = z
    one_team = mass[0]
    second_team = mass[2]

    if one_team not in dict:
        dict[one_team]=[1,0,0,0,0]
        OneTeamInfo=dict[one_team]
        if int(mass[1]) > int(mass[3]):
            OneTeamInfo[1]+=1
        elif int(mass[1]) == int(mass[3]):
            OneTeamInfo[2]+=1
        else:
            OneTeamInfo[3]+=1
        OneTeamInfo[4]=OneTeamInfo[1]*3+OneTeamInfo[2]*1
        dict[one_team]=OneTeamInfo

    elif one_team in dict:
        OneTeamInfo=dict[one_team]
        OneTeamInfo[0]+=1
        if int(mass[1]) > int(mass[3]):
            OneTeamInfo[1]+=1
        elif int(mass[1]) == int(mass[3]):
            OneTeamInfo[2]+=1
        else:
            OneTeamInfo[3]+=1
        OneTeamInfo[4]=OneTeamInfo[1]*3+OneTeamInfo[2]*1
        dict[one_team]=OneTeamInfo

    if second_team not in dict:
        dict[second_team]=[1,0,0,0,0]
        SecondTeamInfo =dict[second_team]
        if int(mass[3]) > int(mass[1]):
            SecondTeamInfo[1]+=1
        elif int(mass[3])==int(mass[1]):
            SecondTeamInfo[2]+=1
        else:
            SecondTeamInfo[3]+=1
        SecondTeamInfo[4]=SecondTeamInfo[1]*3+SecondTeamInfo[2]*1
        dict[second_team]=SecondTeamInfo

    elif second_team in dict:
        SecondTeamInfo =dict[second_team]
        SecondTeamInfo[0]+=1
        if int(mass[3]) > int(mass[1]):
            SecondTeamInfo[1]+=1
        elif int(mass[3])==int(mass[1]):
            SecondTeamInfo[2]+=1
        else:
            SecondTeamInfo[3]+=1
        SecondTeamInfo[4]=SecondTeamInfo[1]*3+SecondTeamInfo[2]*1
        dict[second_team]=SecondTeamInfo

for key in dict:
    print(key+":",*dict[key])
    