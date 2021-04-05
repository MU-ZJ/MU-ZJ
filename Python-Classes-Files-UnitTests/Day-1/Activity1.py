class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.addresses = []

class Address:
    def __init__(self, street, city, state, zipcode):
        self.street = street
        self.city = city
        self.state = state
        self.zipcode = zipcode

user = User("John", "Doe")
address = Address("Fake Street", "Fake City", "Fake State", "Fake Zipcode")
user.addresses.append(address)

print(user.first_name, user.last_name)
for address in user.addresses:
    print(address.street)
    print(address.city)
    print(address.state)
    print(address.zipcode)