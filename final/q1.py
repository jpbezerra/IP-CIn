dicionario_palavras = {}

linha = input().split(" ")

for palavra in linha:
    if palavra not in dicionario_palavras.keys():
        dicionario_palavras[palavra] = 1

    else:
        dicionario_palavras[palavra] += 1

for key in dicionario_palavras.keys():
    print(f"{key}: {dicionario_palavras[key]}")