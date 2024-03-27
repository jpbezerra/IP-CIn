pontos = 0
sair = 0 
musicas = 0

while pontos >= 0 and sair == 0:
    string = input()
    if string == "os fãs estão formando uma ciranda":
        pontos -= 3
    elif string == "os fãs estão ligando os flashes e atrapalhando a visão" or string == "os fãs estão dançando na frente da tela" or string == "os fãs estão gritando o nome da Taylor e atrapalhando a música":
        pontos -= 2
    elif string == "houve um pedido de casamento na sessão" or string == "os fãs estão cantando as músicas em coro":
        pontos += 2
    elif string == "long live":
        musicas += 1
        sair += 1
        print(f'A Taylor conseguiu concluir o show sem muitas interrupções e cantou {musicas} músicas.')
    else:
        pontos += 1
        musicas += 1

if pontos < 0:
    print(f'A Taylor só conseguiu cantar {musicas} músicas e a sessão foi interrompida.')