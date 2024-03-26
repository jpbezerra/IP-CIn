numero_pessoas = int(input())
dicionario = {}

for i in range(numero_pessoas):
    informacoes = input().split(" -> ")
    dicionario[informacoes[0]] = {'mascara' : informacoes[1].split(": ")[0], 'cor' : informacoes[1].split(": ")[1], 'nivel' : 0, 'trocas_permitidas' : 0}

trocas = int(input())

for i in dicionario:
    dicionario[i]['trocas_permitidas'] = trocas

acabar = False
while not acabar:
    evento = input()
    if "<->" in evento:
        evento = evento.split(" <-> ")
        if evento[0] in dicionario.keys() and evento[1] in dicionario.keys():
            if dicionario[evento[0]]['trocas_permitidas'] == 0 and dicionario[evento[1]]['trocas_permitidas'] == 0:
                if dicionario[evento[0]]['mascara'] > dicionario[evento[1]]['mascara']:
                    print(f"Eita, amigo, tas preso com a {dicionario[evento[1]]['mascara']}, visse? Pode trocar mais ela não.")
                else:
                    print(f"Eita, amigo, tas preso com a {dicionario[evento[0]]['mascara']}, visse? Pode trocar mais ela não.")
            elif dicionario[evento[0]]['trocas_permitidas'] == 0:
                print(f"Eita, amigo, tas preso com a {dicionario[evento[0]]['mascara']}, visse? Pode trocar mais ela não.")
            elif dicionario[evento[1]]['trocas_permitidas'] == 0:
                print(f"Eita, amigo, tas preso com a {dicionario[evento[1]]['mascara']}, visse? Pode trocar mais ela não.")
            else:

                dicionario[evento[0]]['mascara'], dicionario[evento[1]]['mascara'] = dicionario[evento[1]]['mascara'], dicionario[evento[0]]['mascara']
                dicionario[evento[0]]['cor'], dicionario[evento[1]]['cor'] = dicionario[evento[1]]['cor'], dicionario[evento[0]]['cor']
                dicionario[evento[0]]['nivel'], dicionario[evento[1]]['nivel'] = dicionario[evento[1]]['nivel'] + 1, dicionario[evento[0]]['nivel'] + 1
                dicionario[evento[0]]['trocas_permitidas'], dicionario[evento[1]]['trocas_permitidas'] = dicionario[evento[1]]['trocas_permitidas'] - 1, dicionario[evento[0]]["trocas_permitidas"] - 1

    elif "->" in evento:
        beneficiados = []
        evento = evento.split(" -> ")

        for i in dicionario:
            if (dicionario[i]['nivel'] % 2) != 0 and (int(evento[1].split(": ")[1]) >= dicionario[i]['nivel']):
                dicionario[i]['mascara'], dicionario[i]['nivel'], dicionario[i]['trocas_permitidas'] = evento[1].split(": ")[0], int(evento[1].split(": ")[1]), trocas - 1
                beneficiados.append(i)
        
        if len(beneficiados) == 0:
            print("Vixe... Serviu pra nada o evento Chuva de máscaras :/")
        elif len(beneficiados) == 1:
            print(f"Apenas {beneficiados[0]} é que aproveitou mesmo o evento Chuva de máscaras.")
        else:
            string_beneficiados = ", ".join(beneficiados)
            print(f"Arretaaado demais!! Teve um evento maneiro aqui e {string_beneficiados} foram beneficiados.")

    elif "?" in evento:
        evento = evento.split(" cor ")
        evento[1] = evento[1].split("?")
        cor_mascara = evento[1][0]
        num_pessoas = 0

        for i in dicionario:
            if dicionario[i]['cor'] == cor_mascara:
                num_pessoas += 1

        print(f"Um total de {num_pessoas} pessoa(s) está(o) com máscara de cor {cor_mascara}!")        

    elif evento == "FIM":
        acabar = True

print("Agora é hora de ver quem ficou com que máscara!")

dicionario_ordem = sorted(dicionario.keys())
for i in dicionario_ordem:
    print(f"{i} -> {dicionario[i]['mascara']}: {dicionario[i]['nivel']}")

print("Troca de máscaras encerrada! Esperamos que todos tenham se divertido!")