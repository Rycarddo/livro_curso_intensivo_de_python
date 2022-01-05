class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f'Restaurant Name: {self.restaurant_name.title()}\nCuisine Type: {self.cuisine_type.title()}')

    def open_restaurant(self):
        print(f'The restaurant {self.restaurant_name.title()} is open!!!')


restaurant_1 = Restaurant('La Pergola', 'Linear')
restaurant_1.describe_restaurant()

restaurant_2 = Restaurant('Il Luogo di Aimo e Nadia', 'Linear com Ilha')
restaurant_2.describe_restaurant()

restaurant_3 = Restaurant('Osteria Francescana', 'Paralela')
restaurant_3.describe_restaurant()

