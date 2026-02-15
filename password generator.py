
import random

chars = '+-/*!&$#?=@<>abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
number = int(input('Кол-во паролей: '))
length = int(input('Длина пароля: '))  # исправлено: lenght → length

with open('password.txt', 'a') as f:  # эффективная работа с файлом
    for _ in range(number):
        password = ''.join(random.choice(chars) for _ in range(length))
        print(password)
        f.write(password + '\n')
        
