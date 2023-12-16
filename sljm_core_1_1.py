import random,hashlib


def encript(txt: str, user_password: str = '') -> str:
    # gen word list
    word_list = list(set(txt))
    temp = list(word_list)
    random.shuffle(word_list)
    random.shuffle(temp)
    # gen password
    password = dict(zip(word_list, temp))
    # gen sep
    sep = ''.join(random.choices(word_list, k=2))
    # encript
    encripted = ''
    for i in range(len(txt)):
        encripted += list(password.values())[(list(password.keys()).index(txt[i])
                                             + (ord(user_password[i % len(user_password)]) if user_password else i)) % len(password.keys())]
    # hash
    hash_value = hashlib.md5(txt.encode()).hexdigest()[:5]
    return ''.join([a+b for a, b in password.items()]) + sep + encripted + hash_value


def decript(txt: str, user_password: str = '') -> tuple:
    # get dict
    password = {}
    for i in range(0, len(txt)-1, 2):
        if txt[i+1] in password.keys():
            break
        else:
            password[txt[i+1]] = txt[i]
    # del password & sep
    txt = txt[i+2:]
    # get hash
    hash_value=txt[-5:]
    txt=txt[:-5]
    # decript
    decripted = ''
    for i in range(len(txt)):
        decripted += list(password.values())[(list(password.keys()).index(txt[i])
                                             - (ord(user_password[i % len(user_password)]) if user_password else i)) % len(password.keys())]
    return decripted,hash_value==hashlib.md5(decripted.encode()).hexdigest()[:5]


# cout = 0
# for i in range(10000):
#     temp = str(random.randint(0, 999999999))
#     if temp == decription(encription(temp,True),True):
#         cout += 1
# print(cout)
if __name__ == '__main__':
    with open(input('file:'), 'r', encoding='utf-8')as file:
        temp = encript(file.read(), True)
        print(temp, decript(temp, True), sep='\n\n\n------------------\n\n\n')
