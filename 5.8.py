users = ['admin', 'Toni', 'Ezekyel', 'Rycarddo', 'Josiscleves']

for user in users:
    if user == 'admin':
        print(f'Olá {user}, gostaria de ver um relatório de status?')
    else:
        print(f'Olá {user}, obrigado por fazer login novamente.')
