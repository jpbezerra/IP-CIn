pontos = 0
direcao_porta_1 = input()
numero_porta_1 = int(input())
porta_2 = False
porta_3 = False
porta_4 = False
porta_5 = False
output = False

if (numero_porta_1%2) != 0:
    if direcao_porta_1 == "direita":
        pontos += 150
        resultado_1 = "CERTA"
        porta_2 = True
    elif direcao_porta_1 == "esquerda":
        pontos -= 150
        resultado_1 = "ERRADA"
        porta_2 = True
else:
    if direcao_porta_1 == "esquerda":
        pontos += 150
        resultado_1 = "CERTA"
        porta_2 = True
    elif direcao_porta_1 == "direita":
        pontos -= 150
        resultado_1 = "ERRADA"
        porta_2 = True

if porta_2:
    direcao_porta_2 = input()
    cor_porta_2 = input()
    planta_porta_2 = input()
    macaneta_porta_2 = input()
    if (cor_porta_2 == "dourada" or cor_porta_2 == "prateada") or ((planta_porta_2 == "avenca" or planta_porta_2 == "espadinha") and macaneta_porta_2 == "redonda"):
        if direcao_porta_2 == "direita":
            pontos += 200
            resultado_2 = "CERTA"
            porta_3 = True
        elif direcao_porta_2 == "esquerda":
            pontos -= 200
            resultado_2 = "ERRADA"
            porta_3 = True
    else:
        if direcao_porta_2 == "esquerda":
            pontos += 200
            resultado_2 = "CERTA"
            porta_3 = True
        elif direcao_porta_2 == "direita":
            pontos -= 200
            resultado_2 = "ERRADA"
            porta_3 = True

if porta_3:
    direcao_porta_3 = input()
    cor_porta_3 = input()
    numero_porta_3 = int(input())
    planta_porta_3 = input()
    macaneta_porta_3 = input()
    if ((numero_porta_3%5 == 0) and (planta_porta_3 == "espadinha") and (macaneta_porta_3 == "quadrada")) or (cor_porta_3 == "perolada"):
        if direcao_porta_3 == "esquerda":
            pontos += 250
            resultado_3 = "CERTA"
            porta_4 = True
        elif direcao_porta_3 == "direita":
            pontos -= 250
            resultado_3 = "ERRADA"
            porta_4 = True
    else:
        if direcao_porta_3 == "direita":
            pontos += 250
            resultado_3 = "CERTA"
            porta_4 = True
        elif direcao_porta_3 == "esquerda":
            pontos -= 250
            resultado_3 = "ERRADA"
            porta_4 = True

if porta_4:
    direcao_porta_4 = input()
    numero_porta_4 = int(input())
    if (numero_porta_4%3 == 0) and (numero_porta_4%2 != 0) and (numero_porta_4%5 != 0):
        if direcao_porta_4 == "direita":
            pontos += 300
            resultado_4 = "CERTA"
            porta_5 = True
        elif direcao_porta_4 == "esquerda":
            pontos -= 300
            resultado_4 = "ERRADA"
            porta_5 = True
    else:
        if direcao_porta_4 == "esquerda":
            pontos += 300
            resultado_4 = "CERTA"
            porta_5 = True
        elif direcao_porta_4 == "direita":
            pontos -= 300
            resultado_4 = "ERRADA"
            porta_5 = True

if porta_5:
    cor_porta_5 = input()
    numero_porta_5 = int(input())
    planta_porta_5 = input()
    flor_porta_5 = input()
    macaneta_porta_5 = input()
    if (cor_porta_5 == "acobreada") and ((numero_porta_5%2 != 0) or ((macaneta_porta_5 == "triangular") or (macaneta_porta_5 == "quadrada"))) and (planta_porta_5 == "jiboia"):
        pontos += 500
        resultado_5 = "CERTA"
        output = True
    elif (cor_porta_5 == "prateada") and ((flor_porta_5 != "margarida") or (flor_porta_5 != "papoula") or (flor_porta_5 != "cosmos")) and ((macaneta_porta_5 == "hexagonal") or (macaneta_porta_5 == "redonda")):
        pontos += 450
        resultado_5 = "CERTA"
        output = True
    elif (cor_porta_5 == "dourada") and ((flor_porta_5 == "lirio") or (flor_porta_5 == "ixora")) and (macaneta_porta_5 == "hexagonal"):
        pontos += 400
        resultado_5 = "CERTA"
        output = True
    else:
        pontos -= 500
        resultado_5 = "ERRADA"
        output = True

if output:
    print("ARISU, VOCÊ FEZ SUAS ESCOLHAS E AGORA VEREMOS SE ESCOLHEU AS PORTAS CERTAS:")
    print(f'{resultado_1} {resultado_2} {resultado_3} {resultado_4} {resultado_5}')
    if pontos > 0:
        if (resultado_1 == "CERTA") and (resultado_2 == "CERTA") and (resultado_3 == "CERTA") and (resultado_4 == "CERTA") and (resultado_5 == "CERTA"):
            print(f'Parece que a sorte está ao seu favor, Arisu... Você conseguiu passar com {pontos} pontos!')
        elif (pontos > 0) and ((resultado_1 == "ERRADA") or (resultado_2 == "ERRADA") or (resultado_3 == "ERRADA") or (resultado_4 == "ERRADA") or (resultado_5 == "ERRADA")):
            print(f'Você passou com {pontos} pontos, mas faça melhores escolhas da próxima vez.')
    elif pontos <= 0:
        if (resultado_1 == "CERTA") or (resultado_2 == "CERTA") or (resultado_3 == "CERTA") or (resultado_4 == "CERTA") or (resultado_5 == "CERTA"):
            print(f'Por mais que você tenha feito escolhas corretas, não foi suficiente para sobreviver. Você finalizou o jogo com {pontos} pontos')
        elif (resultado_1 == "ERRADA") and (resultado_2 == "ERRADA") and (resultado_3 == "ERRADA") and (resultado_4 == "ERRADA") and (resultado_5 == "ERRADA"):
            print(f'Todas suas escolhas foram erradas, Arisu, esperávamos mais de você... Você será executado pois obteve {pontos} pontos.')