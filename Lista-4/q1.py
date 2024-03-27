quantidade_dias = int(input())
total_ovos_escondidos = 0
total_ovos_encontrados = 0
qnt_ovos_escondidos = 0

def maximo_ovos(qnt_ovos_escondidos, ovos_encontrados_dia):
    verificacao_1 = (qnt_ovos_escondidos * 0.7)
    verificacao_2 = (qnt_ovos_escondidos) / ((qnt_ovos_escondidos % dia) + 1)
    if verificacao_1 >= verificacao_2:
        ovos_encontrados_dia += int(verificacao_1)
    else:
        ovos_encontrados_dia += int(verificacao_2)
    return ovos_encontrados_dia

def caca_aos_ovos(ovos_encontrados_dia):
    if horoscopo_dia == "Os astros estão radiantes hoje! Eles farão o possível para abençoar a todos com boa sorte.":
        ovos_encontrados_dia += qnt_ovos_escondidos
    elif horoscopo_dia == "Os astros estão de bom humor hoje. Acho que você terá um pouco de sorte extra.":
        ovos_encontrados_dia += int(qnt_ovos_escondidos * 0.7)
    elif horoscopo_dia == "As estrelas estão neutras hoje. O dia está em suas mãos.":
        ovos_encontrados_dia = maximo_ovos(qnt_ovos_escondidos, ovos_encontrados_dia)
    elif horoscopo_dia == "Isso é raro. As estrelas estão absolutamente neutras hoje.":
        ovos_encontrados_dia += ((qnt_ovos_escondidos % dia) + 1)
    elif horoscopo_dia == "Hoje, Kiq não pôde consultar as estrelas. Sem a orientação astrológica, a busca por ovos fica à mercê do destino.":
        ovos_encontrados_dia += 0
    return ovos_encontrados_dia

for dia in range(1, quantidade_dias + 1):
    ovos_encontrados_dia = 0
    qnt_ovos_escondidos = int(input())
    horoscopo_dia = input()
    print(f"Dia {dia}")
    ovos_encontrados_dia = caca_aos_ovos(ovos_encontrados_dia)
    print(f"Hoje Carlos encontrou {ovos_encontrados_dia} ovos!!")
    total_ovos_escondidos += qnt_ovos_escondidos
    total_ovos_encontrados += ovos_encontrados_dia

print(f"Kiq encontrou {total_ovos_encontrados} de um total de {total_ovos_escondidos}")
aproveitamento = (total_ovos_encontrados / total_ovos_escondidos) * 100
if aproveitamento == 100:
    print("Incrível! Seu signo está em alta. Você encontrou todos os ovos!")
elif aproveitamento > 66:
    print("Ótimo trabalho! Os astros estão ao seu lado. Você encontrou a maioria dos ovos!")
elif aproveitamento > 33:
    print("Bom esforço! Os astros sorriem para você. Muitos ovos foram encontrados.")
elif aproveitamento > 0:
    print("Continue procurando! Seu horóscopo sugere que há mais ovos a serem encontrados.")
else:
    print("Ainda não encontrou nenhum ovo. O horóscopo aconselha persistência. Continue tentando!")