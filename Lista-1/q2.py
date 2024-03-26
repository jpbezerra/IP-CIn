frase_monstro = str(input())
caracteristica_monstro = str(input())

if frase_monstro == "Parou filhotada, assim vocês vão deixar todo mundo maluco." and (caracteristica_monstro == "Uivar" or caracteristica_monstro == "Pelos" or caracteristica_monstro == "Caninos"):
    print("Bem-vindos ao Hotel Transilvânia!\nWayne, seu cachorrão.")
elif frase_monstro == "Veio de novo pelo correio, deixa de ser pão duro." and (caracteristica_monstro == "Desmontável" or caracteristica_monstro == "Parafusos" or caracteristica_monstro == "Morto-vivo"):
    print("Bem-vindos ao Hotel Transilvânia!\nFrank, assim vai acabar perdendo a cabeça.")
elif frase_monstro == "Quem me beliscou?" and caracteristica_monstro == "Transparente":
    print("Bem-vindos ao Hotel Transilvânia!\nGriffin, prazer em vê-lo.")
elif frase_monstro == "Tô na área galera!" and (caracteristica_monstro == "Enfaixado" or caracteristica_monstro == "Morto-vivo"):
    print("Bem-vindos ao Hotel Transilvânia!\nMurray, sempre soltando areia.")
else:
    print("UM HUMANO! Quem é você, e como você achou esse lugar?")
