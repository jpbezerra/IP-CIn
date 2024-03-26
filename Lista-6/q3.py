tabela_precos = {"tomate" : 3.00, "cebola" : 2.00, "coentro" : 1.00, "manteiga" : 5.50, "macaxeira" : 3.00, "alho" : 1.50, "pimentao" : 2.00, "azeite" : 15.00, "camarao" : 30.00, "carne de sol" : 30.00, "queijo coalho" : 15.00, "massa de tapioca" : 10.00, "leite de coco" : 5.00, "dende" : 15.00, "creme de leite" : 4.00, "moranga" : 10.00, "bobo de camarao" : 58.00, "tapioca de carne de sol" : 60.00, "carne de sol com macaxeira" : 38.50, "camarao na moranga" : 68.50}
receitas = {"bobo de camarao" : ("camarao", "macaxeira", "leite de coco", "dende", "tomate", "cebola"), "tapioca de carne de sol" : ("massa de tapioca", "carne de sol", "queijo coalho", "tomate", "cebola"), "carne de sol com macaxeira" : ("carne de sol", "macaxeira", "manteiga"), "camarao na moranga" : ("moranga", "camarao", "cebola", "alho", "tomate", "pimentao", "creme de leite", "azeite", "coentro")}
quantidade_ingredientes = {"tomate" : 5, "cebola" : 5, "coentro" : 5, "manteiga" : 5, "macaxeira" : 5, "alho" : 5, "pimentao" : 5, "azeite" : 5, "camarao" : 5, "carne de sol" : 5, "queijo coalho" : 5, "massa de tapioca" : 5, "leite de coco" : 5, "dende" : 5, "creme de leite" : 5, "moranga" : 5}
relatorio_pedidos = {"bobo de camarao" : 0, "tapioca de carne de sol" : 0, "carne de sol com macaxeira" : 0, "camarao na moranga" : 0}
pedido_indisponivel = {}
caixa = 30

acabar = False
while not acabar:
    try:
        pedido = input()
        if pedido not in receitas.keys():
            if pedido not in pedido_indisponivel.keys():
                pedido_indisponivel.update({pedido : 1})
                print(f"{pedido} ainda não é uma opção disponível.")
            else:
                pedido_indisponivel[pedido] += 1
                if pedido_indisponivel[pedido] > 2:
                    print(f"Atendendo demandas, {pedido} é a mais nova adição ao cardápio do Sabores de Recife.")
                    valor_novo_pedido = 0.00
                    receitas.update({pedido : ()})
                    for i in range(9):
                        ingrediente = input()
                        receitas[pedido] = receitas[pedido] + (ingrediente,) 
                        valor_novo_pedido += tabela_precos[ingrediente]
                    pedido_indisponivel.pop(pedido)
                    relatorio_pedidos.update({pedido : 0})
                    tabela_precos.update({pedido : valor_novo_pedido + 5})
                else:
                    print(f"{pedido} ainda não é uma opção disponível.")
        else:
            for i in quantidade_ingredientes:
                if quantidade_ingredientes[i] == 0:
                    quantidade_ingredientes[i] = 4
                    caixa -= tabela_precos[i] * 4
            for i in receitas[pedido]:
                quantidade_ingredientes[i] -= 1
            print(f"{pedido} saindo...")
            relatorio_pedidos[pedido] += 1
            caixa += tabela_precos[pedido]
    except EOFError:
        classificacao_pedidos = sorted(relatorio_pedidos, key = relatorio_pedidos.get, reverse = True)
        print(f"##### Fim do expediente #####\nO lucro obtido no dia de hoje foi de R${(caixa - 30):.2f}.")
        if classificacao_pedidos[0] == "bobo de camarao":
            print("O bom e tradicional Bobó de Camarão, líder em vendas, nunca será superado!")
        else:
            print(f"{(classificacao_pedidos[0]).capitalize()} está fazendo sucesso entre os clientes, ultrapassando até mesmo o lendário Bobó de Camarão.")
        acabar = True