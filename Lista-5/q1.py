meu_codigo = int(input())
lista_numeros = []
senha = 1

def operacoes(meu_codigo, lista_numeros):
    if meu_codigo != 0:
        if meu_codigo % 2 != 0:
            lista_numeros.append(meu_codigo)
        meu_codigo -= 1
        operacoes(meu_codigo, lista_numeros)
    return lista_numeros

lista_numeros = operacoes(meu_codigo, lista_numeros)
for numero in lista_numeros:
    senha *= numero

print(senha)