nome_vitima, nome_antagonista, tipo_armadilha, tempo = input(), input(), input(), int(input())/60
morre = False

if nome_antagonista == "John Kramer":
    if tipo_armadilha == "Armadilha de urso reversa":
            if tempo >= 5:
                print(f"Com tempo de sobra, {nome_vitima} consegue retirar a armadilha de sua cabeça, sobrevivendo com sucesso ao jogo de Jigsaw.")
            elif 2.5 <= tempo:
                print(f"À beira de perder a cabeça, e desafiando as expectativas de seu algoz, {nome_vitima} remove a armadilha de urso e por pouco escapa de um destino cruel.")
            else:
                morre = True

    if tipo_armadilha == "Tanque de agua" and tempo >= 4:
        print(f"{nome_vitima} usa suas práticas de respiração na natação a seu favor, vencendo o jogo de Jigsaw sem perder muito fôlego.")
    elif tipo_armadilha == "Tanque de agua" and 2 <= tempo:
        print(f"{nome_vitima} passa por maus bocados, mas vira o jogo e consegue evitar, no limite, seu afogamento dentro da armadilha.")
    elif tipo_armadilha == "Tanque de agua" and tempo < 2:
        print("Game Over...")

elif nome_antagonista == "Amanda Young" and (tipo_armadilha == "Caixa de laminas" or tipo_armadilha == "Asas de anjo"):
    if tipo_armadilha == "Caixa de laminas":
            if tempo >= 10:
                print(f"Apenas com ferimentos leves, {nome_vitima} se liberta rapidamente das perigosas lâminas da armadilha montada pela discípula de Jigsaw.")
            elif 6 <= tempo:
                print(f"Por um triz, {nome_vitima} sobrevive ao jogo de Amanda, mas com lesões profundas em suas mãos e braços.")
            else:
                morre = True

    if tipo_armadilha == "Asas de anjo":
            if tempo >= 3:
                print(f"Com surpreendente facilidade, {nome_vitima} alcança a chave da armadilha e vence o desafio da aprendiz de Jigsaw.")
            elif 1.5 <= tempo:
                print(f"{nome_vitima} desafia as possibilidades e o cruel anseio de sua algoz, escapando da armadilha com poucas queimaduras e arranhões.")
            else:
                morre = True

if morre:
    print("Game Over...")