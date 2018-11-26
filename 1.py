# Логин должен начинаться с латинской буквы, он может состоять из латинских букв,
# цифр, точки и минуса и должен заканчиваться латинской буквой или цифрой.
# Минимальная длина логина — 1 символ. Максимальная — 20 символов».
# Напишите код, проверяющий соответствие входной строки этому правилу.
# На выходе должен получиться скрипт или бинарник с regexp'ом и тестами.

import re

def checking(login):
    if re.match(r'^[a-z]{1}[a-z0-9-.]{0,18}[a-z0-9]{1}$', login, re.IGNORECASE):
        print('true')
        return True
    else:
        print('false')
        return False

if __name__ == '__main__':
    checking('kjfhsjkfhskjfd')
    checking('')
    checking('_')
    checking('x244345.jdfhsjf')
    checking('a1234567890098765432')
    checking('qwerty.')
    checking('a1234567899876543210z')
    checking('df-dfd.dfd111FJHF')
