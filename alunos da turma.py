# o Dada uma lista de nomes de alunos, ordene a lista em ordem
# alfabética. Em seguida, adicione um novo aluno no início da lista
# e outro no final.

alunos = []
for lista_alunos in range (10):
    lista_alunos =  (input("Coloque o nome do alunos: "))
    alunos.append(lista_alunos)

alunos.sort()
print(alunos)