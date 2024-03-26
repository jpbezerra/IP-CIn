nome = str(input())
sobrenome = str(input())

if len(nome) + len(sobrenome) < 3:
    print("?")
elif len(nome) + len(sobrenome) > 17:
    print("?")
else:
    print("{}{}".format(nome, sobrenome))