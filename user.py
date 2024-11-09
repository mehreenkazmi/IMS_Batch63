# user.py

class User:
    users = {
        'admin@gmail.com': {'password': '123456', 'role': 'admin'},
        'user@gmail.com': {'password': '123456', 'role': 'user'}
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
            print("Invalid credentials.")
            return False