class User:
    def __init__(self, login_attempts):
        self.login_attemps = login_attempts


    def increment_login_attempts(self):
        self.login_attemps += 1

    def reset_login_attempts(self):
        self.login_attemps = 0

    def print_login_attempts(self):
        print(self.login_attemps)


user = User(135)
user.print_login_attempts()
user.increment_login_attempts()
user.print_login_attempts()
user.reset_login_attempts()
user.print_login_attempts()
