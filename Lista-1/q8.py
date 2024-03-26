filme_1 = input()
pontuacao_global_filme_1 = int(input())
critica_filme_1 = input()
if critica_filme_1 == "boa":
    pontuacao_global_filme_1 *= 1.25
elif critica_filme_1 == "media":
    pontuacao_global_filme_1 *= 1.00
elif critica_filme_1 == "ruim":
    pontuacao_global_filme_1 *= 0.75
elif critica_filme_1 == "pessima":
    pontuacao_global_filme_1 *= 0

filme_2 = input()
pontuacao_global_filme_2 = int(input())
critica_filme_2 = input()
if critica_filme_2 == "boa":
    pontuacao_global_filme_2 *= 1.25
elif critica_filme_2 == "media":
    pontuacao_global_filme_2 *= 1.00
elif critica_filme_2 == "ruim":
    pontuacao_global_filme_2 *= 0.75
elif critica_filme_2 == "pessima":
    pontuacao_global_filme_2 *= 0

filme_3 = input()
pontuacao_global_filme_3 = int(input())
critica_filme_3 = input()
if critica_filme_3 == "boa":
    pontuacao_global_filme_3 *= 1.25
elif critica_filme_3 == "media":
    pontuacao_global_filme_3 *= 1.00
elif critica_filme_3 == "ruim":
    pontuacao_global_filme_3 *= 0.75
elif critica_filme_3 == "pessima":
    pontuacao_global_filme_3 *= 0

if (pontuacao_global_filme_1 > pontuacao_global_filme_2) and (pontuacao_global_filme_1 > pontuacao_global_filme_3):
    print("**** TOP 3 FILMES ****")
    print(f"{filme_1} está em 1° lugar")
    if pontuacao_global_filme_2 > pontuacao_global_filme_3:
        print(f"{filme_2} está em 2° lugar")
        print(f"{filme_3} está em 3° lugar")
        if critica_filme_3 == "pessima":
            print(f"{filme_3} teve uma crítica péssima")
    else:
        print(f"{filme_3} está em 2° lugar")
        print(f"{filme_2} está em 3° lugar")
        if critica_filme_2 == "pessima":
            print(f"{filme_2} teve uma crítica péssima")
elif (pontuacao_global_filme_2 > pontuacao_global_filme_1) and (pontuacao_global_filme_2 > pontuacao_global_filme_3):
    print("**** TOP 3 FILMES ****")
    print(f"{filme_2} está em 1° lugar")
    if pontuacao_global_filme_1 > pontuacao_global_filme_3:
        print(f"{filme_1} está em 2° lugar")
        print(f"{filme_3} está em 3° lugar")
        if critica_filme_3 == "pessima":
            print(f"{filme_3} teve uma crítica péssima")
    else:
        print(f"{filme_3} está em 2° lugar")
        print(f"{filme_1} está em 3° lugar")
        if critica_filme_1 == "pessima":
            print(f"{filme_1} teve uma crítica péssima")
elif (pontuacao_global_filme_3 > pontuacao_global_filme_1) and (pontuacao_global_filme_3 > pontuacao_global_filme_2):
    print("**** TOP 3 FILMES ****")
    print(f"{filme_3} está em 1° lugar")
    if pontuacao_global_filme_1 > pontuacao_global_filme_2:
        print(f"{filme_1} está em 2° lugar")
        print(f"{filme_2} está em 3° lugar")
        if critica_filme_2 == "pessima":
            print(f"{filme_2} teve uma crítica péssima")
    else:
        print(f"{filme_2} está em 2° lugar")
        print(f"{filme_1} está em 3° lugar")
        if critica_filme_1 == "pessima":
            print(f"{filme_1} teve uma crítica péssima")