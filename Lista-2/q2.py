musicas = 0
quant_min = 0
sair = False

while musicas < 21 and not sair:
    opiniao = input()
    if opiniao == "amei":
        musicas += 1
        quant_min += 4
    elif opiniao == "não parei de ouvir":
        musicas += 1
        sair2 = False
        while not sair2:
            opiniao2 = input()
            if opiniao2 != "pulei":
                quant_min += 4
            else:
                sair2 = True
    elif opiniao == "essa não deu":
        musicas += 1
    elif opiniao == "escutei só metade":
        musicas += 1
        quant_min += 2
    else:
        sair = True
else:
    print(f'Você ouviu {quant_min} minutos hoje!!!')