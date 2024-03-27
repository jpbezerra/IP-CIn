sair = False
valor_linha = 0
quantidade_reliquias = 0
#lista vazia que vai guardar as posições das relíquias
posicoes = []
while not sair:
  #pedindo inputs
    string = input()
    valor_coluna = 0
    if string == "Fim do labirinto":
        sair = True
    else:
      #criando uma lista com o input
        string = string.split(" ")
        #checando cada valor da lista
        for coordenada in string:
            #se não tem "1" na lista é porque não tem relíquia
            if coordenada != "1":
                quantidade_reliquias += 0
            #se o valor for "1" é porque tem relíquia
            elif coordenada == "1":
                #adicionando as posições das relíquias na lista vazia
                posicoes.append(f"linha: {valor_linha}, coluna: {valor_coluna}")
                quantidade_reliquias += 1
            #cada vez que checar um índice da string vai aumentar a coluna += 1
            valor_coluna += 1
    #nova linha (ou nova string)
    valor_linha += 1
else:
  #checando a quantidade_reliquias
    if quantidade_reliquias == 0:
        print("Nenhuma relíquia encontrada no labirinto.")
    else:
        print("Relíquias encontradas nos seguintes locais:")
        #printando cada índice da lista posicoes
        for i in posicoes:
            print(i)