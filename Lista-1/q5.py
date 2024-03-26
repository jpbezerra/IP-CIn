resposta_correta_1 = input()
resposta_correta_2 = input()
resposta_correta_3 = input()
perdeu = False

pergunta_1 = input()
resposta_1 = input()
if resposta_1 == resposta_correta_1:
    print("Muito bem! Olha como a primeira foi fácil, seu amigo talvez sobreviva. Falta só mais duas para acabar com isso!")
    pergunta_2 = input()
    resposta_2 = input()
    if resposta_2 == resposta_correta_2:
        print("A resposta está e…exata! Você é mais inteligente do que eu pensei, já posso caprichar nesta última, vamos ver se você realmente conhece filmes de terror!")
        pergunta_3 = input()
        resposta_3 = input()
        if resposta_3 == resposta_correta_3:
            print("Droga, não vai ser hoje que vou ver sangue, que pena! Mas não se esqueça de mim, quem sabe um dia algum dos seus amigos não queiram brincar para lhe salvar!")
        else:
            perdeu = True
    else:
        perdeu = True
else:
    perdeu = True
if perdeu:
    print("A resposta está e…e…rrada hahahahaha. Essa é a parte que eu mais gosto, venha aqui no quintal, você pode dar um adeus!")