age = input('Digite sua idade:')

while not age.isnumeric():
    print('Você digitou uma idade inválida, tente novamente.')
    age = input('Digite sua idade:')

age = int(age)

if 2 <= age < 4:
    print('Você é uma criança.')

elif 4<= age <13:
    print('Você é um garoto(a).')

elif 13<= age < 20:
    print('Você é um(a) adolescente.')

elif 20<= age < 65:
    print('Você é adulto(a)')

elif age >= 65:
    print('Você é um(a) idoso(a).')