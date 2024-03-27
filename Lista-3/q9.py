string = list(input())
tamanho_string = len(string)
string_decifrada = []
palavras_string_decifrada = []
sair = False
acabar = 0

for i in string:
    if i == ' ':
        string_decifrada.append(i)
    else:
        valor_caractere = ord(i)
        valor_novo_caractere = valor_caractere + tamanho_string
        novo_caractere = chr(valor_novo_caractere)
        string_decifrada.append(novo_caractere)

string_palavra_decifrada = "". join((i) for i in string_decifrada)

if string_palavra_decifrada == "" or string_palavra_decifrada == " " or string_palavra_decifrada == []:
    print("Ué não tem nada para me decifrar aqui")
else:
    for _ in range(1):
        for i in string_palavra_decifrada:
            if i == '0' or i == '1' or i == '2' or i == '3' or i == '4' or i == '5' or i == '6' or i == '7' or i == '8' or i == '9': 
                sair = True
        else:
            acabar += 1
    else:
        if sair:
            print("Algo de errado não está certo. Será que estou ficando doido?")
        else:
            print(f"Descobri o que a mensagem significa: {string_palavra_decifrada}")