sandwich_orders = ['Sandwich_1', 'Sandwich_2', 'Sandwich_3', 'Sandwich_4', 'Sandwich_5']
finished_sandwich = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f'O {current_sandwich.title()} acabou de ser preparado.')
    finished_sandwich.append(current_sandwich)

finished_sandwich = sorted(finished_sandwich)
for word in finished_sandwich:
    print(word)



print(sandwich_orders)
