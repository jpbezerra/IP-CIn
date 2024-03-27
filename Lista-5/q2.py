numero_pedidos = int(input())

def repartir(numero_inicial, numero_desejado):
    if numero_inicial == numero_desejado:
        return True
    elif numero_inicial % 3 != 0:
        return False
    else:
        numero_maior = (numero_inicial / 3) * 2
        numero_menor = numero_inicial / 3
        if numero_desejado > numero_maior and numero_desejado > numero_menor:
            return False
        elif numero_desejado == numero_maior or numero_desejado == numero_menor:
            return True
        else:
            if repartir(numero_maior, numero_desejado) or repartir(numero_menor, numero_desejado):
                return True
            else:
                return False

for pedido in range(numero_pedidos):
    pedido = input().split()
    numero_inicial = int(pedido[0])
    numero_desejado = int(pedido[1])
    if repartir(numero_inicial, numero_desejado):
        print("SIM")
    else:
        print("NAO")