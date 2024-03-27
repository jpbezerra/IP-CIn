nome_missao = input()
sair = False
grupo_herois = []

while not sair:
  nome_heroi = input()
  if nome_heroi == "Grupo formado":
    sair = True
  else:
    grupo_herois.append(nome_heroi)
    #adicionando heróis na lista

print(f"O grupo formado por {len(grupo_herois)} heróis para a missão {nome_missao} foi:")

#printando o nome de cada herói
for nome_heroi in grupo_herois:
  print(f"- {nome_heroi}")