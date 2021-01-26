KEY = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
ciphertext = input('Enter Cipher Text? ')

def decrypt(x, ciphertext):
    result = ''
    for l in ciphertext:
        try:
            index = KEY.index(l)
            i =  (index - x) % 26
            result += KEY[i]
        except ValueError:
            result += l
    return result

for x in range(0,27):
    dec = decrypt(x, ciphertext)
    print("[+] Shift: %d - %s" % (x,dec))
