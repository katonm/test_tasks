import re


def checking(login):
    if re.match(r'^[a-z]{1}[a-z0-9-.]{0,18}[a-z0-9]?$', login, re.IGNORECASE):
        return True
    else:
        return False


if __name__ == '__main__':
    import random
    import string

    BASE_STRING = string.ascii_letters + string.digits + string.punctuation
    sample = ''.join([random.choice(BASE_STRING) for _ in range(random.randint(0, 25))])
    if checking(login=sample):
        print(f'{sample} is valid')
    else:
        print(f'{sample} is invalid')
