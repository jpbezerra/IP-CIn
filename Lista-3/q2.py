lista_respostas = [["Zeus", "trovão", "deus"], ["Afrodite", "amor", "deusa"], ["Poseidon", "oceanos", "deus"], ["Hércules", "força", "semideus"], ["Aquiles", "resistência", "semideus"], ["Orfeu", "música", "semideus"]]
quantidade_questoes = int(input())
lista_respostas_percy = []
questoes_certas = 0
if quantidade_questoes == 0:
    print("Infelizmente, Percy Jackson, chegou atrasado para a exame...")
else:
    numero_questao = 1
    #pedindo input para cada quantidade de questões
    for resposta_percy in range(quantidade_questoes):
        resposta_percy = input().split(", ")
        #checando se existe a resposta de percy no gabarito checando os índices da lista
        for i in range(len(lista_respostas)):
            if (resposta_percy[0] in lista_respostas[i]) and (resposta_percy[1] in lista_respostas[i]) and (resposta_percy[2] in lista_respostas[i]):
                #se a resposta estiver correta vai adicionar a resposta no gabarito de percy
                lista_respostas_percy.append(resposta_percy)
        if resposta_percy in lista_respostas_percy:
            print(f"A resposta da {numero_questao}ª questão está... CORRETA!")
            questoes_certas += 1
        else:
            print(f"A resposta da {numero_questao}ª questão está... ERRADA!")
        numero_questao += 1
    
    taxa_acertos = int((questoes_certas / quantidade_questoes) * 100)
    print(f"Percy Jackson, sua taxa de acerto no EDEM é de aproximadamente... {taxa_acertos}%")
    #prints finais
    if taxa_acertos == 100:
        print("UAU, você gabaritou! Você é praticamente um deus do Olimpo!")
    elif taxa_acertos >= 60:
        print("Muito bem, você quase pode começar a desfilar entre os semideuses!")
    elif taxa_acertos >= 20:
        print("Você pode melhorar um pouco mais!")
    else:
        print("Bem... te vejo ano que vem")