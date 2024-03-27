deuses = ['Zeus', 'Poseidon', 'Atenas', 'Ares', 'Afrodite']
poder = [100, 90, 80, 70, 60]
artefato = ['Raio', 'Tridente', 'Égide', 'Lança', 'Cinto Mágico']

lista_sequencia = input()
contador = 0

for indice in range(len(lista_sequencia)):
    if int(lista_sequencia[indice]) == 2 or int(lista_sequencia[indice]) == 4:
        tipo_deus = "Deusa"
    else:
        tipo_deus = "Deus"
    if contador == (len(lista_sequencia) - 1):
        print(f"{tipo_deus}:{deuses[int(lista_sequencia[indice])]}")
        print(f"Poder:{poder[int(lista_sequencia[indice])]}")      
        print(f"Artefato:{artefato[int(lista_sequencia[indice])]}")
    else:
        print(f"{tipo_deus}:{deuses[int(lista_sequencia[indice])]}")
        print(f"Poder:{poder[int(lista_sequencia[indice])]}")      
        print(f"Artefato:{artefato[int(lista_sequencia[indice])]}\n")
    contador += 1