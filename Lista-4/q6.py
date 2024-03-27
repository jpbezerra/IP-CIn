#organizando a matriz inicial
def fazer_matriz(linha, matriz):
    for _ in range(8):
        linha.append('-')
    for _ in range(8):
        matriz.append(linha.copy())
    
    matriz[percyY][percyX] = 'P'
    matriz[clarisseY][clarisseX] = 'C'
    matriz[aguaY][aguaX] = 'A'
    matriz[bandeiraY][bandeiraX] = 'B'
    return matriz

#movimentando os "objetos" da matriz
def movimentacao(coordenadas_clarisse, coordenadas_percy, coordenadas_agua, coordenadas_bandeira, matriz, vencer, pegou_bandeira):
    while not vencer:
        coordenadas_clarisse = movimentacao_clarisse(coordenadas_clarisse, coordenadas_percy, matriz)
        #prints
        if coordenadas_clarisse == coordenadas_agua:
            print("Vitória!! Nunca subestime o cabeça de alga!")
            vencer = True
        elif coordenadas_clarisse == coordenadas_percy:
            print("Ah não, Annabeth vai me matar...")
            vencer = True
        else:
            direcao = input()
            coordenadas_percy = movimentacao_percy(direcao, coordenadas_percy, matriz, coordenadas_bandeira, coordenadas_agua, pegou_bandeira)
            #prints
            if matriz[coordenadas_bandeira[0]][coordenadas_bandeira[1]] == 'B':
                print("Preciso pegar aquela maldita bandeira vermelha.")
            else:
                if coordenadas_percy == coordenadas_bandeira:
                    print("Isso! Consegui a bandeira!")
                else:
                    if coordenadas_percy[0] != 0:
                        print("Agora eu só preciso meter o pé daqui!")
                    else:
                        print("Vitória!! Nunca subestime o cabeça de alga!")
                        vencer = True
        #printando matriz
        for m in matriz:
            print(*m)
        if vencer != True:
            print()

def movimentacao_clarisse(coordenadas_clarisse, coordenadas_percy, matriz):
    #removendo o objeto com a coordenada "antiga"
    matriz[coordenadas_clarisse[0]][coordenadas_clarisse[1]] = '-'

    #movimentando clarisse
    if coordenadas_clarisse[1] != coordenadas_percy[1]:
        if coordenadas_percy[1] > coordenadas_clarisse[1]:
            coordenadas_clarisse[1] += 1
        else:
            coordenadas_clarisse[1] -= 1
    else:
        if coordenadas_percy[0] != coordenadas_clarisse[0]:
            if coordenadas_percy[0] > coordenadas_clarisse[0]:
                coordenadas_clarisse[0] += 1
            else:
                coordenadas_clarisse[0] -= 1

    #colocando o objeto com a coordenada "nova"
    matriz[coordenadas_clarisse[0]][coordenadas_clarisse[1]] = 'C'
    return coordenadas_clarisse

def movimentacao_percy(direcao, coordenadas_percy, matriz, coordenadas_bandeira, coordenadas_agua, pegou_bandeira):
    #removendo o objeto com a coordenada "antiga"
    matriz[coordenadas_percy[0]][coordenadas_percy[1]] = '-'
    
    #atualizando as coordenadas
    if coordenadas_percy != coordenadas_agua:
        matriz[coordenadas_agua[0]][coordenadas_agua[1]] = 'A'
        if direcao == "esquerda":
            coordenadas_percy[1] -= 1
        elif direcao == "direita":
            coordenadas_percy[1] += 1
        elif direcao == "cima":
            coordenadas_percy[0] -= 1
        elif direcao == "baixo":
            coordenadas_percy[0] += 1
    
    #se percy jackson pisar na água durante sua rodade de movimentação
    if coordenadas_percy == coordenadas_agua:
        print("Sinto o poder de Poseidon em minhas veias!")
        if direcao == "esquerda":
            coordenadas_percy[1] -= 1
        elif direcao == "direita":
            coordenadas_percy[1] += 1
        elif direcao == "cima":
            coordenadas_percy[0] -= 1
        elif direcao == "baixo":
            coordenadas_percy[0] += 1
        matriz[coordenadas_agua[0]][coordenadas_agua[1]] = 'A'
    
    #checando se percy jackson pegou ou está com a bandeira
    if coordenadas_percy == coordenadas_bandeira:
        pegou_bandeira = True
    if pegou_bandeira == True:
        matriz[coordenadas_bandeira[0]][coordenadas_bandeira[1]] = '-'    

    #fazendo com que percy não saia do "campo de batalha"
    if coordenadas_percy[0] < 0:
        coordenadas_percy[0] = 0
    elif coordenadas_percy[0] > 7:
        coordenadas_percy[0] = 7
    
    if coordenadas_percy[1] < 0:
        coordenadas_percy[1] = 0
    elif coordenadas_percy[1] > 7:
        coordenadas_percy[1] = 7

    #colocando o objeto com a coordenada "nova"
    matriz[coordenadas_percy[0]][coordenadas_percy[1]] = 'P'
    return coordenadas_percy

#declarando variáveis
linha = []
matriz = []
vencer = False
pegou_bandeira = False

#inputs das coordenadas dos objetos
percyY = int(input())
percyX = int(input())
clarisseY = int(input())
clarisseX = int(input())
aguaY = int(input())
aguaX = int(input())
bandeiraY = int(input())
bandeiraX = int(input())

#colocando as coordenadas em listas diferentes
coordenadas_percy = [percyY, percyX]
coordenadas_clarisse = [clarisseY, clarisseX]
coordenadas_agua = [aguaY, aguaX]
coordenadas_bandeira = [bandeiraY, bandeiraX]

#fazendo a matriz inicial
matriz = fazer_matriz(linha, matriz)

#movimentando os objetos
movimentacao(coordenadas_clarisse, coordenadas_percy, coordenadas_agua, coordenadas_bandeira, matriz, vencer, pegou_bandeira)