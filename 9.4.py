class Restaurant:
    def __init__(self):
        self.number_served = 0

    # Seta o número de clientes atendidos
    def set_number_served(self, number_served):
        self.number_served = number_served
        print(f'The current number of served costumers is: {self.number_served}')

    # Soma o value com o número de clientes atendidos
    def increment_number_served(self, value):
        self.number_served += value
        print(f'{value} costumers were added.\nThe current number of served costumers is: {self.number_served}')


restaurant = Restaurant()

restaurant.set_number_served(10)

restaurant.increment_number_served(75)
