nomeJogador1=input()
escolha1=input()
escolhanum1= int(input())
nomeJogador2=input()
escolhanum2= int(input())

if escolha1== "PAR":
    if (escolhanum1+escolhanum2)%2==0:
        print(f"{nomeJogador1} ganhou")
    elif (escolhanum1+escolhanum2)%2 !=0:
        print(f"{nomeJogador2} ganhou")
else:
    if (escolhanum1+escolhanum2)%2==0:
        print(f"{nomeJogador2} ganhou")
    elif (escolhanum1+escolhanum2)%2 !=0:
        print(f"{nomeJogador1} ganhou")