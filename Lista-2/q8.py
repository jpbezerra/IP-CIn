numero_celebridades = int(input())
kanye = ""
pique = ""
chris = ""

for _ in range(numero_celebridades):
    celebridade = input()
    print(f"Apresentador: Contamos com a ilustre presença de {celebridade}, uma salva de palmas!")
    if celebridade == "Kanye West":
        kanye = "Kanye West"
    elif celebridade == "Gerard Piqué":
        pique = "Gerard Piqué"
    elif celebridade == "Chris Martin":
        chris = "Chris Martin"

Taylor = ""
Katy = ""
Ariana = ""
Beyonce = ""
Shakira = ""
ganhadora = ""
sair = False

while not sair:
    candidato = input()
    if candidato == "Início da Premiação":
        print("Apresentador: Vamos deixar de enrolação e ir para a premiação!\nApresentador: E a artista do ano do MTV Video Music Awards 2023 é...")
        sair = True
    else:
        if candidato == "Taylor Swift":
            Taylor = "Taylor Swift"
        elif candidato == "Katy Perry":
            Katy = "Katy Perry"
        elif candidato == "Ariana Grande":
            Ariana = "Ariana Grande"
        elif candidato == "Beyoncé":
            Beyonce = "Beyoncé"
        elif candidato == "Shakira":
            Shakira = "Shakira"

if Taylor == "Taylor Swift":
    print("TAYLOR SWIFT")
    if kanye:
        print("Kanye West: Eu vou te deixar terminar. Estou feliz por você, mas Beyoncé fez um dos melhores vídeos de todos os tempos.")
elif Katy == "Katy Perry":
    print("KATY PERRY")
elif Ariana == "Ariana Grande":
    print("ARIANA GRANDE")
elif Beyonce == "Beyoncé":
    print("BEYONCÉ")
    if chris:
        print("Chris Martin: Minha heroína, minha irmã, meu tudo. Você merece!")
elif Shakira == "Shakira":
    print("SHAKIRA")
    if pique:
        print("Gerard Piqué: Meu amor me perdoa, volta pra mim...")