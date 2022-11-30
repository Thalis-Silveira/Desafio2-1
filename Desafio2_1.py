convidados = []

N = int(input("Número de súditos: "))
M = int(input("Número de turnos: "))
i = 1
#popula a lista 
for i in range(1, N + 1):
    convidados.append(i)

turnosN = 1
while(turnosN <= M):
    if(2 <= N <= 1000000000 and 1 <= M <= 5000):
        Ti = int(input("Digite o número: "))
        #remove os multiplos da posição atraves do Ti                   
        for i in range(1, len(convidados) + 1):
            if(i % Ti == 0):
                convidados[i - 1] = 0
        #função que filtra a lista removendo todos os 0´s(descomentar abaixo)
        #forma 1 de resolver
        removedor = 0
        convidados = [remove for remove in convidados if remove != removedor]
        #forma 2 de resolver
        #convidados = list(filter((0).__ne__,convidados))
        turnosN += 1
    else:
        while(not 2 <= N <=1000000000 and 1 <= M <= 5000):
            print("valores inválidos!\nTente novamente.")
            N = int(input("Número de súditos: "))
            M = int(input("Número de turnos: "))
            for i in range(1, N + 1):
                convidados.append(i)

if(len(convidados) > 10000):
    for i in range(1,convidados[10000]):
        print(i)
    len(convidados)
else:
    for i in convidados:
        print(i)
