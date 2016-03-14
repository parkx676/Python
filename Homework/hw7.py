## Substitution Cipher
## Juhwan Park (3917664)


## Import random module
import random

## alphabets in string format
alphabet_str = 'abcdefghijklmnopqrstuvwxyz.,!? '

## alphabets in string format into list format
alphabet_list = []
for i in alphabet_str:
    alphabet_list.append(i)

## Secret key in list and change it into string.
def makeKey(alphabet):
    random.shuffle(alphabet)
    secret_key = ''
    for i in alphabet:
        secret_key += i
    return secret_key

## Make secret key by makeKey(alphabet) function with alphabets in list
secret_key = makeKey(alphabet_list)

## Printing the alphabet string and the generated secret-key string 
print("Alphabet: '%s'" %alphabet_str)
print("Key:      '%s'" %secret_key)

##Encrypt
def encryptMsg(plaintext, key, alphabet):
    p = plaintext
    p = p.lower()
    n = ''
    for i in p:
        if i in alphabet:
            n += i
    idx = 0
    en = ''
    while idx <= len(n) - 1:
        en += key[alphabet.find(n[idx])]
        idx += 1
    return en

## Input plain text & encrypting + printing the result
plaintext = str(input('Input plaintext: '))
en = encryptMsg(plaintext, secret_key, alphabet_str)

print("Ciper text:     '%s'" %en)

##Decrypt
def decryptMsg(ciphertext, key, alphabet):
    idx = 0
    de = ''
    while idx <= len(ciphertext) - 1:
        de += alphabet[key.find(ciphertext[idx])]
        idx += 1
    return de

## Decrypting and printing the result
de = decryptMsg(en, secret_key, alphabet_str)
print("Decrypted text: '%s'" %de)
