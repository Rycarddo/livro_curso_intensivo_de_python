class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f'Restaurant Name: {self.restaurant_name.title()}\nCuisine Type: {self.cuisine_type.title()}')

    def open_restaurant(self):
        print(f'The restaurant {self.restaurant_name.title()} is open!!!')


restaurant = Restaurant('La Pergola', 'Linear')
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()
