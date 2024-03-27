computadores_disponiveis = int(input())
dinheiro_disponivel = int(input())
tempo_espera_limite = (int(input())) * 60
sair = False
amigo = 0

# conferindo quantos amigos vão ajudar baseado na quantidade de computadores disponíveis
while not sair:
    nome = input()
    if nome != "end" and nome != "laura" and nome != "carlos" and nome != "roberto":
        amigo += 1
        computadores_disponiveis -= 1
    else:
        if (nome == "laura") or (nome == "carlos") or (nome == "roberto"):
            amigo += 0
        else:
            sair = True
    if computadores_disponiveis == 0:
        sair = True

# quantidade de amigos (quantidade de computadores ocupados)
if amigo == 0:
    print("Ah não! João não conseguiu nenhum amigo que o ajudasse. Agora ele vai ter que contar com a sorte para pegar um bom lugar na fila, usando apenas seu computador.")
elif amigo >= 1:
    print(f"Bom começo! Consegui {amigo} amigos que podem me ajudar a comprar o ingresso")
    # a quantidade inteira x de amigos vão tentar comprar o ingresso (o máximo de ingressos é exatamente igual à quantidade de amigos pois é a quantidade de chances de conseguir o ingresso)
    ingresso_disponivel = 0
    posicao_escolhida = 100000
    computador_escolhido = 0
    #para cada amigo (número de computadores), cada computador vai receber variáveis
    for contador in range(amigo):
        valor_ingresso = int(input())
        local_show = input()
        while local_show != "end" and local_show != "rio de janeiro" and local_show != "são paulo" and local_show != "buenos aires":
            valor_ingresso = int(input())
            local_show = input()
        if local_show != "end":
            print("Consegui um ingresso em um local que João possa ir! Agora temos que ver o preço")
            if dinheiro_disponivel >= valor_ingresso:
                print("Consegui o dinheiro! Agora só falta ver a minha colocação na fila dos ingressos...")
                posicao = int(input())
                tempo_fila = float((posicao / 16) * 10)
                if tempo_fila > tempo_espera_limite:
                    print(f"Caramba, essa foi quase! Mas infelizmente não consegui um bom lugar na fila dos ingressos no computador de número {contador + 1}")
                else:
                  #se conseguiu um ingresso
                    print("ISSOOO, conseguimos um ingresso!!!")
                    ingresso_disponivel += 1
                    #checando em qual computador vamos comprar o ingresso baseada na menor posicao em cada computador
                    if posicao < posicao_escolhida:
                        posicao_escolhida = posicao
                        computador_escolhido = contador + 1 #atualizando o número do computador
            else:
                print("Caramba! Só tinha ingresso para a pista vip, que está bem acima do meu orçamento.")
        else:
            ingresso_disponivel += 0
    # Impressão final checando a quantidade de ingressos disponíveis
    if ingresso_disponivel >= 1:
        print(f"Consegui o ingresso! Com {int((ingresso_disponivel / amigo) * 100)}% de aproveitamento da ajuda dos meus amigos. E a fila escolhida para comprar o ingresso foi do computador número {computador_escolhido}. Rumo ao show da Taylor!!!")
    elif ingresso_disponivel == 0 and (amigo > (computadores_disponiveis / 2)):
        print("Não acredito que tive amigos para ocuparem mais da metade dos computadores, e ainda assim não consegui um ingresso...")
    elif ingresso_disponivel == 0 and ((computadores_disponiveis / 2) >= amigo):
        print("Poxa, não acredito que não consegui o ingresso, acho que eu devia ter chamado mais amigos para ajudar.")