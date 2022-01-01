words = {'Listas:': 'São de fato listas onde elementos podem ser adicionados ou removidos.',
         'Tuplas:': 'São listas que contém elementos fixos, ou seja, não podem ser adicionados e nem '
                   'removidos. É possível "mudar" o valor de uma tupla se você mudar a tupla toda.',
         'String:': 'São as "palavras" da programação, strings podem ser concatenadas, cortadas...',
         'Int:': 'São os números inteiros',
         'Float:': 'São os números reais da programação ou números de ponto flutuante'}


for key, value in words.items():
    print(f'{key} {value}\n')
