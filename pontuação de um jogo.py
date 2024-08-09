# o Você tem uma lista com as pontuações dos jogadores em um
# jogo. Encontre a pontuação mais alta, a mais baixa e a média das
# pontuações

pontuacoes = [2300, 2500, 300, 1500, 3000 ]

pontuacoes.sort()

pontuacao_maxima = max(pontuacoes)
minimo_pontuacao = min(pontuacoes)
media_pontuacao = sum(pontuacoes) / len(pontuacoes)

print(pontuacao_maxima)
print(minimo_pontuacao)
print(media_pontuacao)