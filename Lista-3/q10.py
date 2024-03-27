lista_objetos = input().split(' - ')
mochila = []
lista_maior_menor = []

#verificando por qual item dentro da lista_objetos devemos começar
item_mostrado_clarisse = lista_objetos[int((len(lista_objetos)/2))]
vezes_girar = int(input())

for i in range(vezes_girar):
    #guardando o índice do item_clarisse baeado na lista_objetos
    indice_item_clarisse = lista_objetos.index(item_mostrado_clarisse)
    maior_ou_menor = input()
    #guardando a quantidade de vezes vamos ter que avançar ou retroceder na lista
    indice_maior_menor = int(maior_ou_menor[:-1])
    #mudando o item_guardado_clarisse com base no resto da divisão entre o tamanho da lista_objetos e o (índice inicial do item somando ou subtraindo com o indice_maior_menor)
    if maior_ou_menor[-1] == '>':
        item_mostrado_clarisse = lista_objetos[(indice_item_clarisse + indice_maior_menor) % len(lista_objetos)]
    elif maior_ou_menor[-1] == '<':
        item_mostrado_clarisse = lista_objetos[(indice_item_clarisse - indice_maior_menor) % len(lista_objetos)]
    decisao_clarisse = input()
    #adicionando o item_mostrado_clarisse na mochila
    if decisao_clarisse == "Adicionar":
        if item_mostrado_clarisse not in mochila:
            mochila.append(item_mostrado_clarisse)
            print(f"{item_mostrado_clarisse} adicionado a mochila!")
        else:
            print(f"{item_mostrado_clarisse} já está na mochila. Não seja gananciosa, ou acabará como Midas!")
    #ignorando o item_mostrado_clarisse
    elif decisao_clarisse == "Ignorar":
        if item_mostrado_clarisse not in mochila:
            print(f"{item_mostrado_clarisse} não vai ser tão útil assim!")
        else:
            print(f"{item_mostrado_clarisse} já está na mochila. Não seja gananciosa, ou acabará como Midas!")

if len(mochila) == 0:
    print("Não achei nada útil no arsenal. Acho que vamos precisar ser menos violentos dessa vez…")
else:
    string_mochila = ", ".join((j) for j in mochila)
    print(f"Com {string_mochila}, seremos imbatíveis na caça à bandeira!")