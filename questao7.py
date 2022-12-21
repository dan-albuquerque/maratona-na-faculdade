matriz1=[[], [], [], []]
matrizFinal = [[],[],[],[]]
matriz2=[[], [], [], []]
for i in range(4):
    for j in range(4):
        matriz1[i].append(int(input()))
        matriz2[i].append(int(input()))
        matrizFinal[i].append(matriz1[i][j]+matriz2[i][j])

print(matrizFinal)