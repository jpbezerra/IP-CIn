def colocar_equipamento(matriz_caixa, linha_atual, coluna_atual, tamanho_coluna_equip, tamanho_linha_equip, letra):
    if matriz_caixa[linha_atual][coluna_atual] == "O":
        if caber_item(matriz_caixa, linha_atual, coluna_atual, tamanho_coluna_equip, tamanho_linha_equip):
            matriz_caixa = preencher_matriz(matriz_caixa, letra, tamanho_coluna_equip, tamanho_linha_equip, linha_atual, coluna_atual)
            return True
    
    coluna_atual += 1
    if coluna_atual == len(matriz_caixa[0]):
        coluna_atual = 0
        linha_atual += 1
        if linha_atual == len(matriz_caixa):
            return False
    return colocar_equipamento(matriz_caixa, linha_atual, coluna_atual, tamanho_coluna_equip, tamanho_linha_equip, letra)

def caber_item(matriz_caixa, linha_atual, coluna_atual, tamanho_coluna_equip, tamanho_linha_equip):
    if linha_atual + tamanho_linha_equip > len(matriz_caixa) or coluna_atual + tamanho_coluna_equip > len(matriz_caixa[0]):
        return False
    else:
        for i in range(tamanho_linha_equip):
            for j in range(tamanho_coluna_equip):
                if matriz_caixa[i + linha_atual][j + coluna_atual] != "O":
                    return False
    return True
              
def preencher_matriz(matriz_caixa, letra, tamanho_coluna_equip, tamanho_linha_equip, linha_atual, coluna_atual):
    for l in range(tamanho_linha_equip):
        for c in range(tamanho_coluna_equip):
            matriz_caixa[l + linha_atual][c + coluna_atual] = letra

equip_obtido = []
matriz_caixa = []
caixa = input()
while caixa != "finalizar":
    matriz_caixa.append(list(caixa))
    caixa = input()
    if "A" in list(caixa):
        equip_obtido.append("acessorios")
    if "P" in list(caixa):
        equip_obtido.append("primaria")
    if "S" in list(caixa):
        equip_obtido.append("secundaria")
    if "B" in list(caixa):
        equip_obtido.append("branca")
    if "G" in list(caixa):
        equip_obtido.append("granada")
    if "M" in list(caixa): 
        equip_obtido.append("munição")    

equip_obrigatorio = input().split(", ")
if len(equip_obtido) > 0:
    for i in equip_obtido:
        if i in equip_obrigatorio:
            equip_obrigatorio.remove(i)
            
equip = input()
while equip != "finalizar programa":
    equip = equip.split("-")
    tamanho_coluna_equip = int((equip[1]).split("x")[0])
    tamanho_linha_equip = int((equip[1]).split("x")[1])
    if equip[-1] == "acessorios":
        letra = "A"
    elif equip[-1] == "primaria":
        letra = "P"
    elif equip[-1] == "secundaria":
        letra = "S"
    elif equip[-1] == "branca":
        letra = "B"
    elif equip[-1] == "granada":
        letra = "G"
    elif equip[-1] == "munição":
        letra = "M"

    if equip[-1] not in equip_obrigatorio:
        print(f"Não precisamos de {equip[0]}")
    else:
        if colocar_equipamento(matriz_caixa, 0, 0, tamanho_coluna_equip, tamanho_linha_equip, letra):
            print(f"Item adicionado: {equip[0]}")
            equip_obrigatorio.remove(equip[-1])
        else:
            print(f"Não há espaço para {equip[0]}")
    
    equip = input()

for i in range(len(matriz_caixa)):
    for j in range(len(matriz_caixa[0])):
        print(matriz_caixa[i][j], end="")
    print()

if len(equip_obrigatorio) > 0:
    string_faltando = ", ".join(equip_obrigatorio)
    print(f"Faltou: {string_faltando}")