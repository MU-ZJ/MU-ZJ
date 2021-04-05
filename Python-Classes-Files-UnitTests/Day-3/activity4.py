with open("emails.txt") as file:
    content = file.read()

email_list = content.split(',')

email_list = list(dict.fromkeys(email_list))

email_list_nd = ",".join(email_list)

with open("duplicate-free-email-list.txt", "w") as file:
    file.write(email_list_nd)