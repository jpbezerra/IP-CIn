local_do_teste = str(input())
hora_do_teste = int(input())
resposta = str(input())

if local_do_teste == "Salão":
    print("Em direção ao salão!")
elif local_do_teste == "Praça":
    print("Para a praça eu vou!")
elif local_do_teste == "Centro da cidade":
    print("Faz tempo que não visito o centro, mal posso esperar!")

if local_do_teste == "Salão" or local_do_teste == "Praça":
    print(f"Pra chegar na hora, vou ter que sair de {hora_do_teste - 2} horas.")
elif local_do_teste == "Centro da cidade":
    print(f"Pra chegar na hora, vou ter que sair de {hora_do_teste - 1} horas.")

if resposta == "Sim, Pearl! Siga seus sonhos!":
    print("Obrigada mãe! Eu vou ser uma estrela e o mundo todo saberá meu nome!")
elif resposta == "Não. Você ficará na fazenda.":
    print("Você não vai me deixar aqui! EU NÃO VOU FICAR NESSA FAZENDA!")

