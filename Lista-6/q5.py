informacoes_dolly = {}

vida_dolly = int(input())
ataque_dolly = int(input())
defesa_dolly = int(input())
informacoes_dolly.update({'Dolly' : vida_dolly}) #guardando a informação da vida de Dolly

qnt_inimigos = int(input())
inimigos_derrotados = 0 #guardando quantos inimigos foram derrotados

if qnt_inimigos == 0: #se não tem inimigos no caminho
    print("Oba! Sem intercorrências pelo caminho! Podemos ir para o carnaval em paz!")
else:
    print("Oh não! Eles querem acabar com o meu Dollynho!")
    for i in range(qnt_inimigos):
        informacoes_inimigo = {}

        nome_inimigo = input()
        vida_inimigo = int(input())
        ataque_inimigo = int(input())
        defesa_inimigo = int(input())

        informacoes_inimigo.update({nome_inimigo : vida_inimigo}) #guardando a informação da vida do inimigo

        while vida_inimigo > 0 and vida_dolly > 0: #fazendo o combate enquanto ambos Dolly e inimigo possuem vida
            vida_inimigo -= ataque_dolly - defesa_inimigo
            informacoes_inimigo.update({nome_inimigo : vida_inimigo}) #atualizando a vida do inimigo
            if vida_inimigo <= 0: #se o inimigo morreu
                print(f"O {nome_inimigo} foi derrotado!\nSTATUS DOLLY\nVida: {informacoes_dolly['Dolly']}")
                inimigos_derrotados += 1 #atualizando o número de inimigos derrotados
            else: #se inimigo ainda tiver vida
                vida_dolly -= ataque_inimigo - defesa_dolly
                informacoes_dolly.update({'Dolly' : vida_dolly}) #atualizando a vida de Dolly
                if vida_dolly <= 0: #se Dolly morreu
                    print("Que tristeza! Dollynho se foi!")
        
    if vida_dolly > 0 and inimigos_derrotados == qnt_inimigos: #se Dolly conseguiu sair vivo do combate contra todos inimigos
        print("OBA! Dolly venceu todos os inimigos!")
    else:
        print(f"Infelizmente Dollynho não conseguiu vencer todos os Barriguinhas Moles…\nPelo menos levou {inimigos_derrotados} baderneiros com ele!")