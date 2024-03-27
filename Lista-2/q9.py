sair = False

while not sair:
    nome_pretendente = input()
    if nome_pretendente == "vou dormir":
        sair = True
    else:
        palavra_pretendente = input()
        palavra_taylor = input()
        contador = 0
        for letra in palavra_taylor:
            if letra in palavra_pretendente:
                contador += 1
                palavra_pretendente = palavra_pretendente.replace(letra, "", 1)      
        if contador == len(palavra_taylor):
            print(f"você acertou, estreou na lista! {nome_pretendente}")
        else:
            print("perdeu covarde!")