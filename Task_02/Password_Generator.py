import random

lengthOfPassword = int(input('enter the password:'))

character = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@#$%&'

password = []

for i in range(1,lengthOfPassword+1):
    val = random.choice(character)
    password.append(val)
print(''.join(password))
