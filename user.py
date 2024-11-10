# user.py
class User:
    users = {
        'owner@gmail.com': {'password': 'owner123', 'role': 'admin'},
        'customer@gmail.com': {'password': 'customer123', 'role': 'user'}
    }

    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.role = None

    def login(self):
        user = self.users.get(self.email)
        if user and user['password'] == self.password:
            self.role = user['role']
            return True
        else:
            print("Oops! Incorrect login details. Please try again.")
            return False
