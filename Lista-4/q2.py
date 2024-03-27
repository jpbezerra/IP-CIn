def organizar_malas():
    lista_pesos_malas = input().split(", ")

    lista_pesos_malas.sort()
    lista_pesos_malas_copia = lista_pesos_malas.copy()

    lista_pesos_malas[0] = lista_pesos_malas_copia[-1]
    lista_pesos_malas[-1] = lista_pesos_malas_copia[0]
    lista_pesos_malas[1] = lista_pesos_malas_copia[-2]
    lista_pesos_malas[-2] = lista_pesos_malas_copia[1]

    string_list_malas = ", ".join(lista_pesos_malas)
    print(f"A nova organização das malas é a seguinte: {string_list_malas}")
    
def informacoes_trem():
    lista_informacoes = input().split(",")

    qtd_blocos_carvao = int(lista_informacoes[0])
    peso = int(lista_informacoes[1])
    num_passageiros = int(lista_informacoes[2])

    velocidade = int((qtd_blocos_carvao + 200)/2)
    print(f"A velocidade que o trem partirá é de: {velocidade}Km/H")

    carga_total_trem = int((peso + 4000)/1000)
    print(f"A carga do Trem em Toneladas é: {carga_total_trem} Ton.")

    total_pessoas = num_passageiros + 40
    print(f"A quantidade de passageiros é de {total_pessoas}")

def turno():
    funcionarios_convocados = []
    lista_funcionarios = input().split(", ")
    hora_viagem = input().split(":")
    roteiro = input().split()

    numero_roteiro = int(roteiro[-1])
    hora = int(hora_viagem[0])
    hora = hora * 60
    minuto = int(hora_viagem[1])
    tempo = hora + minuto

    if 1260 > tempo > 420:
        if numero_roteiro == 1:
            funcionarios_convocados.append(lista_funcionarios[0])
            funcionarios_convocados.append(lista_funcionarios[1])
        elif numero_roteiro == 2:
            funcionarios_convocados.append(lista_funcionarios[0])
            funcionarios_convocados.append(lista_funcionarios[-1])
    else:
        if numero_roteiro == 1:
            funcionarios_convocados.append(lista_funcionarios[2])
        elif numero_roteiro == 2:
            funcionarios_convocados = []

    if len(funcionarios_convocados) > 0:
        string_funcionarios_convocados = ", ".join(funcionarios_convocados)
        print(f"Os funcionários convocados são: {string_funcionarios_convocados}")
    else:
        print("Os funcionários convocados são: Nenhum! O turno da Madrugada vai ser tranquilo para todos")

def protocolo_inicio():
    organizar_malas()
    informacoes_trem()
    turno()

protocolo_inicio()