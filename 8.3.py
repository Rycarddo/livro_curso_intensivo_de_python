def make_shirt(size, message):
    while not size.isnumeric():
        print('Você não digitou um tamanho válido, tente novamente.\n')
        size = input('Digite um tamanho válido:')
        size = int(size)
    print(f'Tamanho: {size}\nMensagem: {message.title()}')


make_shirt('3', 'oi')

make_shirt(message='f(x)', size='35')
