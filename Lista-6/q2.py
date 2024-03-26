nome = str
lista_penalidades = []
escolas = []
dicionario_media = {} #dicionario "final" utilizado para guardar as médias finais
while nome != "Não há mais escolas": #inputs das escolas
    penalidade = 0
    nome = input()
    if nome != "Não há mais escolas":
        tema = input()
        tempo = int(input())
        if 65 > tempo: #aplicando as penalidades
            penalidade += (65 - tempo)/10
        elif tempo > 75:
            penalidade += (tempo - 75)/10
        lista_penalidades.append(penalidade) #guardando as penalidades
        escolas.append(nome)
escolas = tuple(escolas) #guardando as escolas em uma tupla

print("Desfile de samba do Rio de janeiro 2024")

for i in range(len(escolas)): #adicionando elementos no dicionario "final"
    dicionario_media.update({escolas[i] : 0.0})

quesito = str
nome_nota = str
lista_quesitos = []
while quesito != "Não há mais quesitos": #inputs dos quesitos
    dicionario = {} #dicionario "temporário" usado para guardar valores de cada escola de acordo com o quesito
    quesito = input()
    if quesito != "Não há mais quesitos":
        lista_quesitos.append(quesito)
        for i in range(len(escolas)):
            nome_nota = input().split(" - ")
            dicionario.update({nome_nota[0] : float(nome_nota[1])}) #adicionando valores no dicionario "temporário"
            dicionario_media.update({nome_nota[0] : (float(nome_nota[1]) + dicionario_media[nome_nota[0]])}) #atualizando o dicionário com as notas
        print(f"Vamos às notas para o quesito {quesito}:") #printando os quesitos
        for j in dicionario:
            if dicionario[j] == 10.0:
                dicionario[j] = int(dicionario[j])
            print(f"{j}: {dicionario[j]}")
lista_quesitos = tuple(lista_quesitos) #guardando os elementos em uma tupla

indice = 0
for i in escolas: #fazendo as médias de cada escola
    dicionario_media.update({i : dicionario_media[i]/(len(lista_quesitos)) - float(lista_penalidades[indice])})
    if dicionario_media[i] == 10.0:
        dicionario_media[i] = int(dicionario_media[i])
    indice += 1

dicionario_ordenado = sorted(dicionario_media, key = dicionario_media.get, reverse = True) #criando um dicionário com a classificação decrescente das escolas
print(f"E o vencedor do desfile de escola de samba do Rio de Janeiro de 2024 é:\n{dicionario_ordenado[0]} com uma nota final de {dicionario_media[dicionario_ordenado[0]]:.2f}!")