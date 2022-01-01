number = input('Type a number:')

if not number.isnumeric():
    print("\nYou didn't typed a number, try again.\n")
    number = input('Type a number:')

elif number.isnumeric():
    number = int(number)

if number % 10 == 0:
    print(f'The number {number} is multiple of 10')
elif number % 10 != 0:
    print(f'The number {number} is not multiple of 10')
