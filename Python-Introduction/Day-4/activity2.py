'''
contact = {
    'name': {"first name" : "Marsha", "last name" : "Brady"},
    'first address': {"street" : "11222 Dilling St", "city" : "Studio City", "state" : "California"},
    'second address': {"street" : "11111 Fake Name", "city" : "Fake City", "state" : "Fake State"}
}
'''
first_address = {"street" : "11222 Dilling St", "city" : "Studio City", "state" : "California"}
second_address = {"street" : "11111 Fake Name", "city" : "Fake City", "state" : "Fake State"}
addresses = [first_address, second_address]

contact = {"first name" : "Marsha", "last name" : "Brady", "addresses" : addresses}

print(contact)