convidados = ['Ana', 'Newton', 'Luiz Leal', 'Einstein', 'Steve Jobs', 'Sergio']

convidados_removidos = ''
for i in range(2, 4):
    convidados_removidos = convidados.pop(i)
    print(f'Infelizmente,{convidados_removidos} as vagas foram reduzidas. Estou '
          f'deveras triste por você não poder ir :(')

del convidados[-1]
del convidados[-1]

print(convidados)