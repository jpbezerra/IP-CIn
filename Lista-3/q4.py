colecao_livros = ["O Ladrão de Raios", "O Mar de Monstros", "A Maldição do Titã", "A Batalha do Labirinto", "O Último Olimpiano"]
colecao_sergio = input().split(", ")
quantidade_edicoes = int(input())
livros_obtidos = []
livros_faltando = []
livros_outro_universo = []

for i in range(quantidade_edicoes):
    #se qualquer elemento que está na colecao_sergio fazer parte da colecao_livros, isso quer dizer que ele possui um livro obtido
    if colecao_sergio[i] in colecao_livros:
        livros_obtidos.append(colecao_sergio[i])
    #se qualquer elemento que está na colecao_sergio não fazer parte da colecao_livros, isso quer dizer que ele possui um livro que não faz parte da saga percy jackson
    if colecao_sergio[i] not in colecao_livros:
        livros_outro_universo.append(colecao_sergio[i])

#checando quais livros faltam para Sérgio completar a sua coleção
for livro in colecao_livros:
    if livro not in colecao_sergio:
        livros_faltando.append(livro)

#prints finais
if len(livros_obtidos) == 5:
    print("Sua coleção está completa! Você pode ler à vontade.")
elif len(livros_obtidos) >= 1:
    #transformando lista em string
    string_livros_faltando = ", ".join((l) for l in livros_faltando)
    print(f"Infelizmente, sua coleção está incompleta. Falta(m) esse(s) livro(s): {string_livros_faltando}.")
else:
    print("Caramba, você não tem nenhum livro. Compre todos imediatamente.")
if len(livros_outro_universo) > 0:
    #transformando lista em string
    string_livros_outro_universo = ", ".join((j) for j in livros_outro_universo)
    print(f'Cuidado, Sérgio! Você está organizando seus livros de uma forma errada, o(s) livro(s): {string_livros_outro_universo}, não faz(em) parte da saga "Percy Jackson e os Olimpianos".')