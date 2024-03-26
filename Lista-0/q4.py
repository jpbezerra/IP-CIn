dhora_arthur = int(input())
dhora_luiz = int(input())
dhora_pedro = int(input())
hora = int(input())

total_arthur = dhora_arthur * hora
total_luiz = dhora_luiz * hora
total_pedro = dhora_pedro * hora

funcao = int((total_arthur + total_luiz + abs(total_arthur - total_luiz)) / 2)
maximo = int((funcao + total_pedro + abs(funcao - total_pedro)) / 2)

print(maximo)