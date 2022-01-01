active = True
places = []
while active:
    place = input('Se pudesse visitar um lugar do mundo, para onde você iria?\nDigite aqui:')
    place = place.title()
    places.append(place)

    question = input('\nVocê quer adicionar mais lugares?\nDigite "Sim" para continuar ou "Não" para sair.\n'
                     'Digite aqui:')

    question = question.lower()

    while question != 'sim' and question != 'não' and question != 'nao':
        print('Você não digitou uma resposta válida, tente novamente.')
        question = input('\nVocê quer adicionar mais lugares?\nDigite "Sim" para continuar ou "Não" para sair.\n'
                         'Digite aqui:')
        question = question.lower()

    if question == 'não' or question == 'nao':
        for place in places:
            print(f'\nVocê gostaria de visitar {place}')
        break
