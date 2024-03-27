def derivar(x1, y1, a, b, c, d, e):
    h = float(1e-9)
    derivada = (((a*((x1+h)+b)**c)+(e*(x1+h))+d) - ((a*(x1+b)**c)+(e*x1)+d)) / h #realizando a derivada
    if derivada == 0: #se derivada == 0 não tem raiz
        equacao = "y={0}".format(y1)
        print(f"Encontramos o ponto ({round(x1, 3)};{round(y1, 3)}) da função, a equação da reta tangente deste ponto é aproximadamente {equacao}, porém, ainda não é a raiz devemos continuar para otimizar a trajetória do disparo.")
        print(f"Droga, a reta tangente {equacao} é paralela ao eixo das abscissas, não tem raiz, tenho pena de quem estiver usando a arma quando isto acontecer, kkkkk.")
        return False
    else:
        termo_independente = y1 - (derivada*x1) #calculando o termo independente
        if termo_independente >= 0: #colocando o sinal do termo independente caso seja positivo (pois se o termo independente é negativo já vem com o sinal)
            sinal = "+"
        else:
            sinal = ""
        equacao = "y={0}*x{1}{2}".format(round(derivada, 3), sinal, round(termo_independente, 3))
        print(f"Encontramos o ponto ({round(x1, 3)};{round(y1, 3)}) da função, a equação da reta tangente deste ponto é aproximadamente {equacao}, porém, ainda não é a raiz devemos continuar para otimizar a trajetória do disparo.")
        x2 = (-termo_independente)/derivada #calculando o novo x
        y2 = (a*(x2+b)**c)+(e*x2)+d #calculando o novo y
        if round(y2, 3) == 0.000: #se o novo y é suficientemente próximo de zero
            print(f"Acertou em cheio! A raiz foi encontrada e o valor dela nas abscissas é aproximadamente {round(x2, 3)}, e a equação da reta tangente neste ponto é aproximadamente {equacao}.")
        else:
            derivar(x2, y2, a, b, c, d, e)

#inputs
x1 = float(input())
a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())

y1 = (a*(x1+b)**c)+(e*x1)+d

if a == 0 and e*x1 == 0: #se a derivada é de grau 0
    print(f"Maldição, a função é aproximadamente a reta y={d} que é paralela ao eixo das abscissas, não tem raiz e não é possível aplicar o método.")
else:
    derivar(x1, y1, a, b, c, d, e)