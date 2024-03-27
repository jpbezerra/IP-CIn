linhas = int(input())
colunas = int(input())
lista_soma = []
lista_chales = []
matriz = []
soma_linha = 0

#fazendo uma lista dentro de uma litsa
for i in range(linhas):
    for j in range(colunas):
        numero_campistas_chale = int(input())
        lista_chales.append(numero_campistas_chale)
    matriz.append(lista_chales)
    lista_chales = []

for i in matriz:
    print(*i)

#checando qual índice da lista matriz tem a maior soma
for i in matriz:
    for j in i:
        soma_linha += j
    lista_soma.append(soma_linha)
    maior_soma = max(lista_soma)
    soma_linha = 0
print('')
print(f"O chalé {lista_soma.index(maior_soma) + 1} foi o que mais recebeu semi-deuses, tendo um acréscimo de {maior_soma} novos campistas!")