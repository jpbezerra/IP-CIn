escolas_samba = ("Porto da Pedra", "Beija-flor", "Salgueiro", "Grande Rio", "Unidos da Tijuca", "Imperatriz", "Mocidade", "Portela", "Vila Isabel", "Mangueira", "Paraíso do Tuiuti", "Viradouro")
escolas_samba_copia = ["Porto da Pedra", "Beija-flor", "Salgueiro", "Grande Rio", "Unidos da Tijuca", "Imperatriz", "Mocidade", "Portela", "Vila Isabel", "Mangueira", "Paraíso do Tuiuti", "Viradouro"]
escola = str
dicionario = {}

while escola != "Fim": #recebendo os inputs
    escola = input()
    if escola != "Fim":
        escola = escola.split(":")
        if escola[0] not in escolas_samba:
            print("Epa, o que essa escola está fazendo aqui?!")
        else:
            if escola[0] in escolas_samba_copia:
                print(f"{escola[0]} teve sua nota apurada!")
                escolas_samba_copia.remove(escola[0])
                dicionario.update({escola[0] : float(escola[1])}) #adicionando chaves e valores no dicionário
            else:
                print(f"{escola[0]} teve sua nota atualizada!")
                dicionario[escola[0]] = float(escola[1]) #atualizando chaves pré-existentes

print("\nCLASSIFICAÇÃO DO CARNAVAL 2024:")
dicionario_ordenado = sorted(dicionario, key = dicionario.get, reverse = True) #criando uma lista
#ordenando as chaves com base nos valores atribuídos a elas (de forma decrescente)

j = 1
for i in dicionario_ordenado:
    print(f"{j}. {i}: {dicionario[i]}") # i = chave; dicionario[i] = valor associado à chave no dicionario inicial
    j += 1

print(f"\nÉ CAMPEÃ! A ESCOLA {dicionario_ordenado[0]} É A GRANDE VENCEDORA DO CARNAVAL DE 2024, FAZENDO {dicionario[dicionario_ordenado[0]]} PONTOS!!")
print(f"Infelizmente, a escola {dicionario_ordenado[-1]} não alcançou as expectativas, fazendo apenas {dicionario[dicionario_ordenado[-1]]} pontos, e foi rebaixada.")