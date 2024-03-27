def multiplicar(sequencia, posicao, tamanho_binario, numero, numero_final):
    if tamanho_binario != -1:
        numero = int(sequencia[posicao]) * (2 ** tamanho_binario)
        posicao += 1
        tamanho_binario -= 1
        numero_final = multiplicar(sequencia, posicao, tamanho_binario, numero, numero_final) + numero
        return numero_final
    else:
        return numero_final

def conversao_binario_decimal(codigo, indice_binario, qnt_codigos, lista_numeros):
    numero_final = 0
    numero = 0
    if qnt_codigos > indice_binario:
        sequencia = list(codigo[indice_binario])
        posicao = 0
        tamanho_binario = len(sequencia) - 1
        numero_final += multiplicar(sequencia, posicao, tamanho_binario, numero, numero_final)
        lista_numeros.append(numero_final)
        indice_binario += 1
        lista_numeros = conversao_binario_decimal(codigo, indice_binario, qnt_codigos, lista_numeros)
        return lista_numeros
    else:
        return lista_numeros

def conversao_decimal_ascii(lista_numeros, tamanho_decimal, palavra):
    if tamanho_decimal != -1:
        letra = chr(lista_numeros[tamanho_decimal])
        tamanho_decimal -= 1
        palavra = letra + palavra
        palavra = conversao_decimal_ascii(lista_numeros, tamanho_decimal, palavra)
        return palavra
    else:
        return palavra
    
codigo = input().split()
qnt_codigos = len(codigo)
indice_binario = 0
indice_decimal = 0
lista_numeros = []
lista_numeros = conversao_binario_decimal(codigo, indice_binario, qnt_codigos, lista_numeros)
tamanho_decimal = len(lista_numeros) - 1
palavra = ""
palavra = conversao_decimal_ascii(lista_numeros, tamanho_decimal, palavra)
print(f"Os códigos da Matrix indicam que {palavra} está perto.")