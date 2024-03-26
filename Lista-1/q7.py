numero_1 = int(input())
if numero_1 < 0:
    print(f"{numero_1:.2f} não está gravado(a) na caixa, não adianta nem continuar que ela não vai abrir.")
else:
    if (numero_1 % 2) != 0:
        numero_1 = float(numero_1 * 0.5)
    else:
        numero_1 = numero_1 * 2
    numero_2 = int(input())
    if numero_2 < 0:
        print(f"{numero_2:.2f} não está gravado(a) na caixa, não adianta nem continuar que ela não vai abrir.")
    else:
        if (numero_2 % 2) != 0:
            numero_2 = float(numero_2 * 0.5)
        else:
            numero_2 = numero_2 * 2
        numero_3 = int(input())
        if numero_3 < 0:
            print(f"{numero_3:.2f} não está gravado(a) na caixa, não adianta nem continuar que ela não vai abrir.")
        else:
            if (numero_3 % 2) != 0:
                numero_3 = float(numero_3 * 0.5)
            else:
                numero_3 = numero_3 * 2
            palavra = input()
            if palavra != palavra.lower():
                print(f"{palavra} não está gravado(a) na caixa, não adianta nem continuar que ela não vai abrir.")
            else:
                numero_4 = int(input())
                numero_final = (numero_1 * numero_2 * numero_3 * numero_4) ** 0.5
                tempo = 10 - numero_final

                if numero_final >= 10:
                    print(f"O número {numero_final:.2f} e a palavra {palavra} eram as respostas. A caixa foi aberta.")
                else:
                    print(f"A combinação era muito pequena, a caixa só vai poder ser aberta daqui a {tempo} anos.")
