# o Simule uma fila de atendimento. Adicione três pessoas à fila,
# depois atenda (remova) duas pessoas. Mostre o estado atual da
# fila

fila =  []
while len(fila) < 3:

    pacientes = input(str("Coloque o nome do paciente:"))
    atendimento = input(str("Atendimento realizado: ")).lower()
    if atendimento == "sim":
        del (pacientes)
    else:
        atendimento =="não"
        fila.append(pacientes)
print(fila)



