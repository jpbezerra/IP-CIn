def contador_letras(frase_x):
    lista_letras_frases_x = []
    lista_contador_letras_iguais = []
    contador_letras_iguais = 0
    for palavra in frase_x:
        for letra in palavra:
            lista_letras_frases_x.append(letra)
    for indice in range(len(lista_letras_frases_x)):
        contador_letras_iguais = 0
        for letra in lista_letras_frases_x:
            if letra == lista_letras_frases_x[indice]:
                contador_letras_iguais += 1
        lista_contador_letras_iguais.append(contador_letras_iguais)
    return lista_contador_letras_iguais

def desafio_x():
    frase_x = input().upper().split()
    lista_letras = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    maximo = max(contador_letras(frase_x))
    minimo = min(contador_letras(frase_x))
    for palavra in frase_x:
        for letra in palavra:
            if letra in lista_letras:
                lista_letras.remove(letra)
    if len(lista_letras) == 0:
        coordenada_x = int(maximo)
    else:
        coordenada_x = int(minimo)
    return coordenada_x

def fibonacci(tamanho):
    numero1 = 1
    numero2 = 1
    if tamanho > 2:
        for numero in range(tamanho - 2):
            numero = numero1 + numero2
            numero1 = numero2
            numero2 = numero
    elif tamanho == 2:
        numero = numero2
    else:
        numero = numero1
    return numero

def desafio_y():
    vogais = ['A', 'E', 'I', 'O', 'U']
    palavra_y = input().upper()
    palavra_y.split()
    tamanho = len(palavra_y)
    numero = fibonacci(tamanho)
    contador_vogal = 0

    for letra in palavra_y:
        if letra in vogais:
            contador_vogal += 1
    
    if contador_vogal > 0:
        coordenada_y = numero * 4
    else:
        coordenada_y = numero * 2
    return coordenada_y

def desafio_z():
    alfabeto_maiusculo = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    alfabeto_minusculo = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    palavra_z = input()
    frase_z = input().split()

    contador_minusculo_frase_z = 0
    contador_maiusculo_frase_z = 0
    contador_minusculo_palavra_z = 0
    contador_maiusculo_palavra_z = 0
    
    for palavra in frase_z:
        for letra in palavra:
            if letra in alfabeto_minusculo:
                contador_minusculo_frase_z += 1
            elif letra in alfabeto_maiusculo:
                contador_maiusculo_frase_z += 1
    diferenca_frase_z = contador_minusculo_frase_z - contador_maiusculo_frase_z

    for letra in palavra_z:
        if letra in alfabeto_minusculo:
            contador_minusculo_palavra_z += 1
        elif letra in alfabeto_maiusculo:
            contador_maiusculo_palavra_z += 1
    diferenca_palavra_z = contador_minusculo_palavra_z - contador_maiusculo_palavra_z

    coordenada_z = int(diferenca_frase_z ** diferenca_palavra_z)
    return coordenada_z

def inicio():
    coordenada_x = desafio_x()
    coordenada_y = desafio_y()
    coordenada_z = desafio_z()

    x_noel = int(input())
    y_noel = int(input())
    z_noel = int(input())
    distancia = float(((x_noel - coordenada_x) ** 2 + (y_noel - coordenada_y) ** 2 + (z_noel - coordenada_z) ** 2) ** 0.5)

    print(f"A 1ª coordenada do Papai Noel é: {coordenada_x}")
    print(f"A 2ª coordenada do Papai Noel é: {coordenada_y}")
    print(f"A 3ª coordenada do Papai Noel é: {coordenada_z}")
    print(f"A distância entre Jack Esqueleto e Papai Noel é: {distancia:.2f}")

inicio()
