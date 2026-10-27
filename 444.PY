email = input()

name = email.find('@')

mama = len(email)

domain = email[0: name]


print(name)
print(mama)
print(domain)
