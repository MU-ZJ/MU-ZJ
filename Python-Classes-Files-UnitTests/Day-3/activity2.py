while True:
    name = input("Enter your name, or press q to quit: ")  
    if name == "q":
        break
    else:
        reason = input("Enter your reason, or press q to quit: ")
        if reason == "q":
            break
        else:
            with open("responses.txt", "a") as file:
                file.write(f'''
{name}
    "{reason}"''')