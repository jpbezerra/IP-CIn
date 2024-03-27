numero = int(input())
ponto_vogal = 0
ponto_consoante = 0
numero_assento = 1

for numero in range(numero):
    ponto_vogal = 0
    ponto_consoante = 0
    musica = input().lower()
    for letra in musica:
        if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
            ponto_vogal += 1
        else:
            ponto_consoante += 2
    numero_assento *= (ponto_vogal + ponto_consoante)
else:
    print(f'Parabéns por adquirir o ingresso! Seu assento é o {numero_assento}, estamos ansiosos para vê-lo, vai ser incrível!')