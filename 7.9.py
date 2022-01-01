sandwich_orders = ['Sandwich_1', 'Pastrami', 'Sandwich_2', 'Pastrami', 'Sandwich_3', 'Pastrami', 'Sandwich_4',
                   'Sandwich_5', 'Pastrami']
finished_sandwich = []

print('Infelizmente estamos sem Pastrami.')

while 'Pastrami' in sandwich_orders:
    sandwich_orders.remove('Pastrami')

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f'O {current_sandwich.title()} acabou de ser preparado.')
    finished_sandwich.append(current_sandwich)

finished_sandwich = sorted(finished_sandwich)
for word in finished_sandwich:
    print(word)



print(sandwich_orders)
