with open("guests.txt", "w") as file:
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    file.write(f"""First Name: {first_name}
Last Name: {last_name}""")