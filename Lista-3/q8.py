equipamentos_disponiveis = ["Foice de Hades", "Talismã de Ícaro", "Elmo da Invisibilidade", "Cinto de Hermes", "Espada Anaklusmos", "Escudo Aegis", "Adaga Katoptris"]
sair = False
while not sair:
    copia_equipamentos_disponiveis = []
    string_copia_equipamentos_disponiveis = ""
    equipamento = input().split("-")
    if equipamento[0] != "Parar":
        #guardando a string do nome e deletando ela da lista
        nome = equipamento[0]
        equipamento.remove(nome)
        #fazendo uma cópia da lista equipamentos_disponiveis
        copia_equipamentos_disponiveis = equipamentos_disponiveis.copy()
        for objeto in equipamento:
            #analisando se os elementos da lista equipamento estão na lista equipamentos_disponiveis
            if objeto in equipamentos_disponiveis:
                #se tiver, o elemento em questão vai ser removido da lista cópia elementos_disponíveis
                #não tira da lista original pois precisamos dela a fim de comparar os equipamentos em outros inputs do while
                copia_equipamentos_disponiveis.remove(objeto)
        #prints finais
        if len(copia_equipamentos_disponiveis) == 0:
            print(f"{nome} irá batalhar na base do murro!")
        elif len(copia_equipamentos_disponiveis) == 1:
            #como há apenas um elemento, só existe o índice 0
            print(f"{nome} irá rumo a batalha com o equipamento: {copia_equipamentos_disponiveis[0]}!")
        else:
            #transformando uma lista em uma string; pegar os todos os elementos (com exceção do último) e separá-los por vírgula
            #após isso, concatenar os elementos com vírgula e colocar + "e" + e somar a última string da lista
            string_copia_equipamentos_disponiveis = ", ".join((elemento) for elemento in copia_equipamentos_disponiveis[:-1]) + f" e {copia_equipamentos_disponiveis[-1]}" 
            print(f"{nome} irá rumo a batalha com os seguintes equipamentos: {string_copia_equipamentos_disponiveis}!")
    else:
        sair = True