import random
import hashlib
import numpy as np


def encript(txt: list, user_password: str = '') -> "tuple[np.ndarray, str]":
    '''
    Return an encripted string and the hash value
    e.g. ( encripted, hash_value )
    '''
    # gen word list
    word_list_key = np.unique(txt, axis=0).tolist()
    word_list_value = list(word_list_key)
    random.shuffle(word_list_key)
    random.shuffle(word_list_value)
    # # gen password
    # password = dict(zip(word_list, temp))
    # gen sep
    sep = random.choices(word_list_key, k=2)
    # encript
    encripted = []
    for i in range(len(txt)):
        if i % 1000 == 0:
            print(i)
        encripted.append(word_list_value[(word_list_key.index(txt[i]) + (ord(user_password[i % len(user_password)]) if user_password else i)) % len(word_list_key)])
    # print(type(np.array(list(zip(word_list_key, word_list_value))).flatten()[0]),type(np.array(sep).flatten()[0]),type(np.array(encripted).flatten()[0]))
    dic = np.array(list(zip(word_list_key, word_list_value))
                   ).flatten()
    sep = np.array(sep).flatten()
    encripted = np.array(encripted).flatten()
    return np.concatenate([dic,sep,encripted]), hashlib.md5(str(txt).encode()).hexdigest()


def decript(txt: list, user_password: str = '') -> "tuple[np.ndarray, str]":
    '''
    Return a decripted string and the hash value
    e.g. ( decripted, hash_value )
    '''
    # get dict
    word_list_key = []
    word_list_value = []
    for i in range(0, len(txt)-1, 2):
        if txt[i+1] in word_list_key:
            # del password & sep
            txt = txt[i+2:]
            break
        else:
            word_list_key.append(txt[i+1]) 
            word_list_value.append(txt[i])
    
    # decript
    decripted = []
    for i in range(len(txt)):
        if i % 1000 == 0:
            print(i)
        decripted.append(word_list_value[(word_list_key.index(txt[i])
                                                  - (ord(user_password[i % len(user_password)]) if user_password else i)) % len(word_list_key)])
    return np.array(decripted).flatten(), hashlib.md5(str(decripted).encode()).hexdigest()


def nearest_factor_decomposition(n: int) -> "tuple[int, int]":
    lis = []
    for i in range(1, n+1):
        if n % i == 0:
            if n/i in lis:
                return i, n//i
            else:
                lis.append(i)


def hex2rgb(txt: str) -> "list[int, int, int]":
    r, g, b = txt[0:2], txt[2:4], txt[4:6]
    return [int(r, 16), int(g, 16), int(b, 16)]


def rgb2hex(rgb: 'tuple[int,int,int]') -> str:
    '''
    Return a hex string 
    '''
    r, g, b = rgb
    return hex(r)[2:].rjust(2,'0') + hex(g)[2:].rjust(2,'0') + hex(b)[2:].rjust(2,'0')


# cout = 0
# for i in range(10000):
#     temp = str(random.randint(0, 999999999))
#     if temp == decription(encription(temp,True),True):
#         cout += 1
# print(cout)
if __name__ == '__main__':
    # with open(input('file:'), 'r', encoding='utf-8')as file:
    #     temp = encript(file.read(), True)
    #     print(temp, decript(temp, True), sep='\n\n\n--------------------\n\n\n')
    temp = list(input('txt:'))
    print(''.join(encript(temp)[0]))
    print(''.join(decript(encript(temp)[0])[0]))
