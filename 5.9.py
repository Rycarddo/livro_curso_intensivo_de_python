users = ['josé', 'Rycarddo']
tamanho_lista = len(users)

if users:
    if tamanho_lista <= 1:
        print('A lista contém um usuário.')
    elif tamanho_lista > 1:
        print('A lista contém usuários.')
else:
    print('A lista está vazia.')

