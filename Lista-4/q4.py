quantidade_cidades = int(input())
lista_lista_inf_cidades = []

def descriptografar(palavra_criptografada, numero_posicoes, direcao):
    lista_letras = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    lista_letras_palavra = []
    for letra in palavra_criptografada:
        indice_letra = lista_letras.index(letra)
        if direcao == "L":
            letra_descriptografada = lista_letras[(indice_letra - numero_posicoes) % len(lista_letras)]
        elif direcao == "R":
            letra_descriptografada = lista_letras[(indice_letra + numero_posicoes) % len(lista_letras)]
        lista_letras_palavra.append(letra_descriptografada)
    palavra_descriptografada = "".join(lista_letras_palavra)
    return palavra_descriptografada

def calculo_distancia(coordenada_x_noel, coordenada_y_noel, coordenada_x_atual, coordenada_y_atual):
    distancia = float(((coordenada_x_atual - coordenada_x_noel) ** 2 + (coordenada_y_atual - coordenada_y_noel) ** 2) ** 0.5)
    lista_todas_distancias.append(distancia)
    return lista_todas_distancias

def ordem_cidades(menor_distancia, lista_todas_distancias, coordenada_x_atual, coordenada_y_atual, lista_lista_inf_cidades, novas_coordenadas, ordem_distancia):
    menor_distancia = lista_todas_distancias.index(min(lista_todas_distancias))
    coordenada_x_atual = (lista_lista_inf_cidades[menor_distancia][1])
    coordenada_y_atual = (lista_lista_inf_cidades[menor_distancia][2])
    novas_coordenadas.append(coordenada_x_atual)
    novas_coordenadas.append(coordenada_y_atual)
    ordem_distancia.append(lista_lista_inf_cidades[menor_distancia])
    for elemento in ordem_distancia:
        print(f"A senha da cidade {elemento[0]} é: {elemento[-1]}")
    lista_lista_inf_cidades.remove(lista_lista_inf_cidades[menor_distancia])
    return ordem_distancia

for _ in range(quantidade_cidades):
    informacoes_cidade = input().split(", ")
    palavra_criptografada = informacoes_cidade[3]
    numero_posicoes = int(informacoes_cidade[4])
    direcao = informacoes_cidade[5]

    palavra_descriptografada = descriptografar(palavra_criptografada, numero_posicoes, direcao)
    informacoes_cidade.append(palavra_descriptografada)
    lista_lista_inf_cidades.append(informacoes_cidade)

for numero in range(quantidade_cidades):
    menor_distancia = 0
    novas_coordenadas = []
    lista_todas_distancias = []
    ordem_distancia = []
    for informacoes_cidade in lista_lista_inf_cidades:
        coordenada_x_atual = float(informacoes_cidade[1])
        coordenada_y_atual = float(informacoes_cidade[2])
        if numero == 0:
            coordenada_x_noel = 0
            coordenada_y_noel = 0
        calculo_distancia(coordenada_x_noel, coordenada_y_noel, coordenada_x_atual, coordenada_y_atual)
    ordem_cidades(menor_distancia, lista_todas_distancias, coordenada_x_atual, coordenada_y_atual, lista_lista_inf_cidades, novas_coordenadas, ordem_distancia)
    coordenada_x_noel = float(novas_coordenadas[0])
    coordenada_y_noel = float(novas_coordenadas[1])
    