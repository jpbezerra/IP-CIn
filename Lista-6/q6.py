def adicionar(candidato, dicionario, participantes, fantasias):  #função para adicionar o nome do candidato e a sua fantasia no dicionário
    if candidato[0] not in participantes:  #se o candidato não está participando
        if candidato[1] not in fantasias:  #se a fantasia não está sendo utilizada por outro candidato na disputa
            participantes.append(candidato[0])
            fantasias.append(candidato[1])
            dicionario.update({candidato[0] : candidato[1]})
            print(f"{candidato[0]} é o novo participante do desfile!")
        else:
            candidato_fantasia_igual = plagio(candidato, dicionario)  #procurando de qual candidato o candidato[0] está "roubando" a fantasia
            print(f"Eita, parece que {candidato[0]} tentou usar a fantasia {candidato[1]} que ja está sendo utilizada por {candidato_fantasia_igual}, ele deverá ser desqualificado por plágio")
    else:
        print(f'Opa, parece que {candidato[0]} ja consta aqui, voce quis dizer "Atualizar"?')
    return dicionario

def remover(candidato, dicionario, participantes, fantasias, dicionario_pontuacao):  #função para remover o nome do candidato e a sua fantasia no dicionário
    if candidato[0] in participantes:  #se o candidato está participando
        participantes.remove(candidato[0])
        fantasias.remove(dicionario[candidato[0]])
        dicionario.pop(candidato[0])
        if dicionario_pontuacao != {}:
            dicionario_pontuacao.pop(candidato[0])
        print(f"Parece que {candidato[0]} desistiu...")
    else:
        print(f"Hmmm não consegui achar {candidato[0]} no banco de dados...")
    return dicionario

def atualizar(candidato, dicionario, participantes, fantasias):  #função para atualizar a fantasia de determinado candidato no dicionário
    if candidato[0] in participantes:  #se o candidato está na disputa
        if candidato[1] not in fantasias:  #se a fantasia não está sendo utilizada
            fantasias.remove(dicionario[candidato[0]])  #removendo a fantasia antiga
            fantasias.append(candidato[1])  #adicionando a fantasia nova
            dicionario[candidato[0]] = candidato[1] 
            print(f"Fantasia de {candidato[0]} atualizada")
        else:
            candidato_fantasia_igual = plagio(candidato, dicionario) 
            participantes.remove(candidato[0])  #desqualificando o candidato
            fantasias.remove(dicionario[candidato[0]])  #removendo a fantasia do candidato desqualificado
            dicionario.pop(candidato[0])  #removendo o candidato do dicionario
            print(f"Eita, parece que {candidato[0]} tentou usar a fantasia {candidato[1]} que ja está sendo utilizada por {candidato_fantasia_igual}, ele deverá ser desqualificado por plágio")
    else:
        print(f"Hmmm não consegui achar {candidato[0]} no banco de dados...")
    return dicionario

def plagio(candidato, dicionario): #função para verificar qual candidato está "roubando" uma fantasia já usada por outro candidato
    for i in dicionario:  #i = nome do candidato
        if dicionario[i] == candidato[1]:  #dicionario[i]: fantasia do candidato i
            candidato_fantasia_igual = i 
            return candidato_fantasia_igual
        
def pontuacao(dicionario, dicionario_pontuacao, consoantes, alfabeto, participantes): #função para determinar a pontuação dos candidatos
    for i in list(dicionario):  #i: nome do candidato 
        numero_consoantes = 0
        posicao = 1.0
        tamanho_string_fantasia = len(dicionario[i]) ** 2  #dicionario[i]: fantasia
        for j in list(dicionario[i]):  #list(dicionario[i]): percorrendo a string de fantasia letra por letra
            if j.lower() in consoantes:  #j: letra de dicionario[i]
                numero_consoantes += 1
                posicao = posicao * (alfabeto.index(j.lower()) + 1) #guardanda a posição de j
        if numero_consoantes == 0: #se não houver consoantes
            posicao = 0
        if posicao != 0 and (1/numero_consoantes) != 0: #se não ocorrer divisão por zero
            nota = tamanho_string_fantasia / (posicao ** (1/numero_consoantes))
            dicionario_pontuacao.update({i : nota}) #atualizando o dicionario_pontuacao
        else:
            dicionario.pop(i)
            participantes.remove(i)
    return dicionario_pontuacao

def ordenar(dicionario_pontuacao, alfabeto):  #função para criar um dicionário "classificação" de acordo com a pontuação dos candidatos
    dicionario_ordenado = sorted(dicionario_pontuacao, key = dicionario_pontuacao.get, reverse = True)
    for i in range(len(dicionario_ordenado)):  
        troca = False
        if i != len(dicionario_ordenado) - 1:
            if dicionario_pontuacao[dicionario_ordenado[i]] == dicionario_pontuacao[dicionario_ordenado[i + 1]]:  

                #dicionario_pontuacao[dicionario_ordenado[i]]: nota do participante dicionario_ordenado[i]
                #dicionario_pontuacao[dicionario_ordenado[i + 1]]: nota do participante dicionario_ordenado[i + 1] (o próximo participante seguindo a classificação)
                
                for j in dicionario_ordenado[i]:  #j: letras de dicionario_ordenado[i]
                    for l in dicionario_ordenado[i + 1]:  #l: letras de dicionario_ordenado[i + 1]
                        if alfabeto.index(l.lower()) < alfabeto.index(j.lower()):  #se "l" é uma letra que vêm antes de "j" no alfabeto
                            troca = True  #precisa trocar os dois candidatos de lugar
        if troca:
            dicionario_ordenado[i], dicionario_ordenado[i + 1] = dicionario_ordenado[i + 1], dicionario_ordenado[i]  #realizando a troca no dicionario_ordenado
    return dicionario_ordenado

def inicio(): #função principal
    comando = str
    dicionario = {}
    dicionario_pontuacao = {}
    participantes = []
    fantasias = []
    consoantes = ('b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z')
    alfabeto = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
    while comando != "Fim do desfile":
        comando = input()
        if comando != "Fim do desfile":
            if comando == "Julgar previamente":
                dicionario_pontuacao = pontuacao(dicionario, dicionario_pontuacao, consoantes, alfabeto, participantes) #criando um dicionário com a key sendo o candidato e o value sendo a nota
                dicionario_ordenado = ordenar(dicionario_pontuacao, alfabeto) #criando uma lista de classificação, na qual os elementos são os candidatos, baseada na pontuação decrescente
                if len(participantes) >= 2: #só pode haver uma comparação se houver pelo menos 2 candidatos na disputa
                    print(f"Até o momento, o primeiro colocado é {dicionario_ordenado[0]} com uma diferença de {round((dicionario_pontuacao[dicionario_ordenado[0]] - dicionario_pontuacao[dicionario_ordenado[1]]), 1)} pontos para o segundo colocado")
            else:
                candidato = input().split(" - ")

                #candidato[0] = nome do participante
                #candidato[1] = fantasia do participante

                if comando == "Adicionar":
                    dicionario = adicionar(candidato, dicionario, participantes, fantasias)
                elif comando == "Remover":
                    dicionario = remover(candidato, dicionario, participantes, fantasias, dicionario_pontuacao)
                elif comando == "Atualizar":
                    dicionario = atualizar(candidato, dicionario, participantes, fantasias)

    print("=== RESULTADOS DO DESFILE ===")
    dicionario_pontuacao = pontuacao(dicionario, dicionario_pontuacao, consoantes, alfabeto, participantes)
    dicionario_ordenado = ordenar(dicionario_pontuacao, alfabeto)
    if len(dicionario_ordenado) == 0:  #se não há participantes
        print("Parece que não sobrou ninguem na disputa, que pena…")
    elif len(dicionario_ordenado) == 1:  #se há apenas 1 participante
        print(f"PARABÉNS {list(dicionario.keys())[0].upper()}!!! VOCÊ ACABA DE VENCER O PRIMEIRO DESFILE DO LIMOEIRO!!")
    else:
        j = 1
        for i in dicionario_ordenado:  #i: nome; dicionario_pontuacao[i]: pontuação de i
            print(f"{j}. {i} --- {round(dicionario_pontuacao[i], 1)}\n")
            j += 1

        print(f"PARABÉNS {dicionario_ordenado[0].upper()}!!! VOCÊ ACABA DE VENCER O PRIMEIRO DESFILE DO LIMOEIRO!!")
inicio()