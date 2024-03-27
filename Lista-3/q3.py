#itens que o percy quer
item_desejado = input()
item_desejado = item_desejado.split(", ")

#itens que estão no acampamento
item_acampamento = input()
item_acampamento = item_acampamento.split(", ")

#lista dos itens quer percy queria e estavam no acampamento
item_encontrado = []
#lista dos itens quer percy queria e não estavam no acampamento
item_comprar = []

for item in item_desejado:
  #se o item que percy deseja estiver no acampamento
    if item in item_acampamento:
        item_encontrado.append(item)
  #se o item que percy deseja não estiver no acampamento
    else:
        item_comprar.append(item)

#se percy não achou nenhum item que queria
if len(item_encontrado) == 0:
    print(f"Hmm, preciso visitar um vendedor ambulante! Não encontrei nenhum dos {len(item_desejado)} itens aqui no Acampamento Meio-Sangue.")
else:
    print("Estes são os itens que já tenho no Acampamento Meio-Sangue:")
    contador = 1
    #printando cada item que percy queria e estava no acampamento
    for indice in item_encontrado:
        print(f"{contador}º item: {indice}")
        contador += 1
    #se havia algum item que percy queria mas não encontrou
    if len(item_comprar) >= 1:
        print(f"Vou precisar adquirir {len(item_comprar)} itens antes da batalha!")
    else:
        print(f"Perfeito, encontrei todos os {len(item_desejado)} itens aqui no Acampamento Meio-Sangue!")

print("Estou pronto para a batalha! Que comece a guerra contra os Titãs!")