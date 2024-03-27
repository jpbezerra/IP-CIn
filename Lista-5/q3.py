def tamanho_certo(palavra):
    tamanho_palavra = len(palavra)
    if 32 > tamanho_palavra:
        palavra = "0" + palavra
        palavra = tamanho_certo(palavra)
        return palavra
    else:
        return palavra

def contido(byte, palavra, tamanho_byte, numero_slice, tamanho_palavra, resposta):
    if tamanho_palavra >= tamanho_byte:
        substring = palavra[numero_slice:tamanho_byte]
        if substring == byte:
            resposta += 1
            return resposta
        else:
            numero_slice += 1
            tamanho_byte += 1
            resposta = contido(byte, palavra, tamanho_byte, numero_slice, tamanho_palavra, resposta)
            return resposta
    else:
        resposta = 0
        return resposta
    
lista_palavra = []
acabar = False
palavra = input()
qnt_tentativas = int(input())
tamanho_palavra = len(palavra)
numero_slice = 0
resposta = 0
palavra = tamanho_certo(palavra)

while qnt_tentativas != 0 and acabar == False:
    byte = input()
    tamanho_byte = len(byte)
    resposta = contido(byte, palavra, tamanho_byte, numero_slice, tamanho_palavra, resposta)
    if resposta != 0:
        print("Muito bem! Estamos dentro! Vamos queimar essa cidade!!")
        acabar = True
    else:
        print("Não é essa a senha, estamos ficando sem tempo.")
        if qnt_tentativas == 1:
            print("Corre Keanu! Eles nos descobriram!!")
    qnt_tentativas -= 1