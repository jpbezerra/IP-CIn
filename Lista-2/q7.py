numero_versos = int(input())
acertos = 0

for verso in range(numero_versos):
    palavra = ''
    input_plateia = input()
    for letra in input_plateia:
        letra = letra.upper()
        palavra += letra
    if verso == 0:
        print("Cause, baby, now we've got")
        if palavra == "BAD BLOOD":
            print("BAD BLOOD")
            acertos += 1
    if verso == 1:
        print("You know it used to be")
        if palavra == "MAD LOVE":
            print("MAD LOVE")
            acertos += 1
    if verso == 2:
        print("So take a look what")
        if palavra == "YOU'VE DONE":
            print("YOU'VE DONE")
            acertos += 1
    if verso == 3:
        print("Cause, baby, now we've got")
        if palavra == "BAD BLOOD, HEY":
            print("BAD BLOOD, HEY")
            acertos += 1
if acertos == numero_versos:
    print("A plateia deu um show! Acertou tudo!")
elif acertos >= (numero_versos/2):
    print("A plateia acertou a maior parte da música")
else:
    print("Foi um dia atípico e a plateia se esqueceu de grande da música")
