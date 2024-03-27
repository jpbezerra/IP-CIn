lugar_show = input()
acabar = False
codigo_vip = 0

while not acabar:
    codigo = int(input())
    if codigo == 1000:
        codigo_vip += 1
        print("Mais um VIP! Não podemos esquecer de contabilizá-lo.")
    elif codigo == 1001:
        print("Ingresso Normal. Não iremos contabilizá-lo.")
    elif codigo == 1002:
        print("Ele ficará na frente do show, porém não é VIP! Não será contabilizado também.")
    elif codigo == 1003:
        print("Espera, quem é esse? Ele não pagou! Não devemos sequer analisar sua entrada.")
    elif codigo == 1004:
        print("Esse código não existe! O sistema quebrou...\nVamos aguardar até que o suporte nos ajude.")
        acabar2 = False
        while not acabar2:
            ajuda = input()
            if ajuda != "Ajudou":
                print("Ainda não...")
            else:
                acabar2 = True
                acabar = True
    elif codigo == 0000:
        acabar = True
else:
    print(f"O show da Taylor Swift será em {lugar_show} e contará com {codigo_vip} VIPs!")