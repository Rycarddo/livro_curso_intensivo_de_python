ingredientes = []
ingrediente = input('Digite o ingrediente que quer na pizza.\nPara sair digite "sair"\nDigite aqui:')
ingrediente = ingrediente.lower()
while ingrediente != 'sair':
    print(ingrediente.title())
    ingredientes.append(ingrediente)
    ingrediente = input('\n\nDigite o ingrediente que quer na pizza.\nPara sair digite "sair"\nDigite aqui:')
    for item in ingredientes:
        print(f'\nAtualmente a lista de ingredientes contém: {item}')

