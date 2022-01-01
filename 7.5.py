age = ''
while age != 'sair':
    age = input('==== Insira sua idade ====\nPara sair digite "sair".\nDigite aqui:')

    age = age.lower()

    if age == 'sair':
        break

    if age.isnumeric():
        age = int(age)

        if age <= 3:
            print('O ingresso será gratuito.\n\n\n\n')

        elif 3 < age <= 12:
            print('O ingresso custará 10 dólares.\n\n\n\n')

        elif age > 12:
            print('O ingresso custará 15 dólares.\n\n\n\n')

    else:
        print('Você não digitou uma idade válida, tente novamente.\n\n\n\n')

