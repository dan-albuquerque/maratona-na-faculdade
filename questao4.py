import os
os.system('cls')
somaP=0
somaI=0
somaD=0
m=[[], [], [], []]
for i in range(4):
    for j in range(4):
        m[i].append(int(input()))

for i in range(4):
    for j in range(4):
        print(m[i][j], end='  ')
        if i==j:
            somaD+=m[i][j]
    somaP+=m[i][0]
    somaI+=m[i][2]
    print('\n')
print('artur ', somaP)
print('henrique ',somaI)
print('carol ',somaD)

if somaP> somaI and somaP>somaD:
    print('artur ganhou! ')
elif somaI> somaP and somaI>somaD:
    print("henrique ganhou! ")
elif somaD>somaP and somaD>somaI:
    print('carol ganhou! ')
elif somaI==somaP and somaI==somaD and somaD==somaP:
    print('empate triplo ')
elif somaP==somaI:
    print('empate de artur e henrique ')
elif somaP==somaD:
    print('empate de artur e carol ') 
elif somaI==somaD:
    print('empate de heenrrique e carol ')
