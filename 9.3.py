class User:
    def __init__(self, first_name, last_name, gender, age, email):
        self.first_name = first_name
        self.last_name = last_name
        self.full_name = self.first_name + ' ' + self.last_name
        self.gender = gender
        self.age = age
        self.email = email

    def describe_user(self):
        print(f'Username: {self.full_name.title()}\nGender: {self.gender}\nAge: {self.age}\n'
              f'Email: {self.email}')

    def greet_user(self):
        print(f'Hello, {self.full_name.title()}!!!')


user_1 = User('isaac', 'newton', 'Male', '379', 'isaac_newton314@gmail.com')
user_1.describe_user()
print()
user_1.greet_user()

