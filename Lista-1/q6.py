minha_vida = int(input())
poder_minha_arma = int(input())
minha_habilidade_luta = int(input())
meu_poder_surpresa = int(input())
poder_arma_inimigo = int(input())
habilidade_luta_inimigo = int(input())
poder_surpresa_inimigo = int(input())
defesa_inimigo = int(input())

if ((poder_minha_arma < poder_arma_inimigo) and (minha_habilidade_luta < habilidade_luta_inimigo) and (meu_poder_surpresa < poder_surpresa_inimigo)):
    minha_vida = minha_vida - defesa_inimigo

if ((poder_minha_arma > poder_arma_inimigo) and (minha_habilidade_luta > habilidade_luta_inimigo) and (meu_poder_surpresa > poder_surpresa_inimigo)) and minha_vida > 0:
    print("Ainda bem que deu tudo certo, está quase em casa")

    poder_arma_novo_mascarado = int(input())
    poder_luta_novo_mascarado = int(input())
    poder_surpresa_novo_mascarado = int(input())

    if (poder_minha_arma >= poder_arma_novo_mascarado) or (minha_habilidade_luta >= poder_luta_novo_mascarado) or (meu_poder_surpresa >= poder_surpresa_novo_mascarado):
        print("Casa, aqui vou eu")
    else:
        print("Oh, no! Acabou pra mim")
elif ((poder_minha_arma < poder_arma_inimigo) and (minha_habilidade_luta < habilidade_luta_inimigo) and (meu_poder_surpresa < poder_surpresa_inimigo)) and minha_vida > 0:
    poder_minha_arma = float(poder_minha_arma * 0.95)
    minha_habilidade_luta = float(minha_habilidade_luta * 0.95)
    poder_surpresa_inimigo = float(poder_surpresa_inimigo * 1.05)
    if minha_vida <= 0:
        print("Oh, no! Acabou pra mim")
    else:
        print("Rápido, corra antes que ele vá atrás de você!")
        poder_arma_novo_mascarado = int(input())
        poder_luta_novo_mascarado = int(input())
        poder_surpresa_novo_mascarado = int(input())

        if (poder_minha_arma < poder_arma_novo_mascarado) or (minha_habilidade_luta < poder_luta_novo_mascarado) or (meu_poder_surpresa < poder_surpresa_novo_mascarado):
            print("Oh, no! Acabou pra mim")
        else:
            print("Casa, aqui vou eu")
elif minha_vida <= 0:
    print("Oh, no! Acabou pra mim")
else:
    print("Oh, no! Acabou pra mim")