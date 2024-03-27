print("Vai começar! Vamos ver quem é a verdadeira diva!")
num_rodadas = int(input())
acabar = False
rodada = 1
rodada_ganha_tay = 0
rodada_ganha_bey = 0
while not acabar and rodada < num_rodadas + 1:
    print(f"Vai começar a {rodada}º rodada!")
    nota_coreografia_taylor = int(input())
    nota_figurino_taylor = int(input())
    nota_coreografia_beyonce = int(input())
    nota_figurino_beyonce = int(input())

    nota_final_taylor = (nota_coreografia_taylor)*4 + (nota_figurino_taylor)*3
    nota_final_beyonce = (nota_coreografia_beyonce)*4 + (nota_figurino_beyonce)*3
    diferenca = abs(nota_final_taylor - nota_final_beyonce)

    if nota_final_taylor > nota_final_beyonce:
        cantora = "Tay"
        print(f"Fim da apresentação! O placar da rodada {rodada} foi {nota_final_taylor}x{nota_final_beyonce} para os representantes da {cantora}.")
        rodada += 1
        rodada_ganha_tay += 1
        if diferenca > 20:
            print(f"A diferença na pontuação foi de {diferenca} pontos.")
        else:
            print(f"A diferença de pontos foi de apenas {diferenca}.")
    else:
        cantora = "Bey"
        print(f"Fim da apresentação! O placar da rodada {rodada} foi {nota_final_beyonce}x{nota_final_taylor} para os representantes da {cantora}.")
        rodada += 1
        rodada_ganha_bey += 1
        if diferenca > 20:
            print(f"A diferença na pontuação foi de {diferenca} pontos.")
        else:
            print(f"A diferença de pontos foi de apenas {diferenca}.")

    if num_rodadas%2 == 0:
        if rodada_ganha_tay > (num_rodadas/2) or rodada_ganha_tay == 3:
            print(f"Uuuh! Por um placar de {rodada_ganha_tay} a {rodada_ganha_bey}, a equipe da Taylor Swift venceu a competição e mostrou que ela é a verdadeira diva do pop!")
            acabar = True
        elif rodada_ganha_bey > (num_rodadas/2) or rodada_ganha_bey == 3:
            print(f"Minha nossa! A equipe da Beyoncé chocou o mundo e venceu a equipe da Taylor Swift por um placar de {rodada_ganha_bey} a {rodada_ganha_tay}. A Bey é a verdadeira rainha do pop!")
            acabar = True
    else:
        if rodada_ganha_tay == ((num_rodadas+1)/2) or rodada_ganha_tay == 3:
            print(f"Uuuh! Por um placar de {rodada_ganha_tay} a {rodada_ganha_bey}, a equipe da Taylor Swift venceu a competição e mostrou que ela é a verdadeira diva do pop!")
            acabar = True
        elif rodada_ganha_bey == ((num_rodadas+1)/2) or rodada_ganha_bey == 3:
            print(f"Minha nossa! A equipe da Beyoncé chocou o mundo e venceu a equipe da Taylor Swift por um placar de {rodada_ganha_bey} a {rodada_ganha_tay}. A Bey é a verdadeira rainha do pop!")
            acabar = True