from Restaurant import Restaurant


class User:

    def __init__(self, username, password, email):
        self.restaurants = []
        self.username = username
        self.email = email
        self.password = password

    def add_restaurant(self, name, table4count, table2count, locality):
        self.restaurants.append(Restaurant(name, table4count, table2count, locality))

