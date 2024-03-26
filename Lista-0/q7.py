diamantes = int(input())
Arthur = 10
Luiz = 30
Pedro = 100

if diamantes == 0:
    print("Nenhum")
elif diamantes < 11:
    print("Arthur")
elif diamantes < 31:
    print("Luiz")
elif diamantes < 101:
    print("Pedro")
else:
    print("Nenhum")