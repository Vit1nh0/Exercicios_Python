# Lista de jogo
# o crie uma lista com pelo menos 5 itens que você compraria em uma
# ida ao supermercado,remova o terceiro item da lista e adicione dois
# novos itens a final. Mostre a lista final

lista = ['banana', 'mamao',' uva',' beterraba', 'manteiga']
del lista [2]
while len(lista) <= 10:
    compras = input("Adicione mais coisas a lista de mercado: ")
    lista.append(compras)

print(lista)