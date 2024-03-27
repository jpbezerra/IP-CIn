numero_compradores = int(input())
contador_criterios = 0
caractere_impar = 0
numero_suspeitos = 0

for _ in range(numero_compradores):
    nome_comprador = input()
    cpf_comprador = input()
    nome_identidade = input()
    cpf_identidade = input()
    qtd_ingressos = int(input())
    preco_ingressos = float(input())
    codigo_compra = input()
    contador_criterios = 0
    caractere_impar = 0

    if (nome_identidade != nome_comprador):
        contador_criterios += 1
    if (cpf_identidade != cpf_comprador):
        contador_criterios += 1
    if (qtd_ingressos > 12):
        contador_criterios += 1
    if (preco_ingressos > 1500):
        contador_criterios += 1
    for caractere in codigo_compra:
        if int(caractere) % 2 != 0:
            caractere_impar += 1
            if caractere_impar == 7:
                contador_criterios += 1
    if contador_criterios >= 3:
        numero_suspeitos += 1
else:
    print(f"Total de compradores analisados: {numero_compradores}\nTotal de suspeitas de cambistas: {numero_suspeitos}")