alturaMin = float(input())
alturaMax = float(input())
numVisitantes = int(input())
cont =0
for i in range(numVisitantes):
    altura = float(input())
    if altura >= alturaMin and altura <= alturaMax:
        cont +=1
print(cont)