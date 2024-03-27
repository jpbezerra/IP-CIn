qnt_presentes = int(input())
soma = int
lista_presentes = []
lista_presentes_excluidos = []
string = str

def soma_valores(presente_codificado):
    soma = 0
    if presente_codificado != []:
      for i in presente_codificado:
        if i != "":
          soma += int(i)
    return soma

def decodificar(presente_codificado):
    lista_string = []
    if presente_codificado != []:
      for i in presente_codificado:
        if i != "":
          caractere = "".join(chr(int(i)))
          lista_string.append(caractere)
    string = "".join(lista_string)
    return string

if qnt_presentes != 0:   
    for presentes in range(qnt_presentes):
        presente_codificado = input().split(" ")
        soma = soma_valores(presente_codificado)
        string = decodificar(presente_codificado)
            
        if string not in lista_presentes and string not in lista_presentes_excluidos:
            print(f"{string} foi adicionado a lista ultrassecreta de presentes da Anya!!")
            if soma % 2 == 0:
                lista_presentes.append(string)
            else:
                if string not in lista_presentes_excluidos:
                    lista_presentes_excluidos.append(string)    
        else:
            print(f"{string} já está na lista de presentes da Anya!!")
            
    if len(lista_presentes_excluidos) > 0:
        string_lista_presentes_exlcluidos = ", ".join(lista_presentes_excluidos)
        print(f"Infelizmente o Twilight é mão de vaca e os seguintes itens precisaram ser excluídos da lista de presentes ultrassecretos da Anya: {string_lista_presentes_exlcluidos}.")
    else:
        print("Parece que o Dia das Crianças desse ano será especial!!!! Anya ganhará todos os presentes planejados, mesmo que ela não seja tão exemplar como deveria…")
    if len(lista_presentes) == 0:
            print("O quê? Nenhum presente? Isso é um absurdo! Vamos corrigir essa injustiça e garantir que Anya tenha um Dia das Crianças inesquecível!")
    else:
        string_lista_presentes = ", ".join(lista_presentes)
        print(f"Lista final dos melhores presentes da Anya: {string_lista_presentes}.")
else:
    print("O quê? Nenhum presente? Isso é um absurdo! Vamos corrigir essa injustiça e garantir que Anya tenha um Dia das Crianças inesquecível!")