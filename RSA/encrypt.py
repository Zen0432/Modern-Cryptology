from utilities import *

LINEAR_KEY_TRANS = [
        [84, 0, 0, 0, 0, 0, 0, 0],
        [113, 70, 0, 0, 0, 0, 0, 0],
        [17, 27, 43, 0, 0, 0, 0, 0],
        [100, 21, 30, 12, 0, 0, 0, 0],
        [100, 56, 6, 116, 112, 0, 0, 0],
        [30, 49, 19, 55, 96, 11, 0, 0],
        [22, 112, 11, 98, 27, 93, 27, 0],
        [94, 8, 76, 28, 22, 69, 29, 38]
        ]


EXPONENT_KEY = [21, 111, 43, 71, 89, 54, 25, 28]


def LinExpoEncrypt (plaintext, lin_key, exp_key):
    plaintext = [ord(c) for c in plaintext]
    CT = [[0 for j in range (8)] for i in range(8)]
    #  Exponentiation
    for ind, elem in enumerate(plaintext):
        CT[0][ind] = Exponentiate(elem, exp_key[ind])

    #  Linear Transform
    CT[1] = LinearTransform(lin_key, CT[0])

    #  Exponentiation
    for ind, elem in enumerate(CT[1]):
        CT[2][ind] = Exponentiate(elem, exp_key[ind])

    #  Linear Transform
    CT[3] = LinearTransform(lin_key, CT[2])

    #  Exponentiation
    for ind, elem in enumerate(CT[3]):
        CT[4][ind] = Exponentiate(elem, exp_key[ind])
    return CT[4]

password1 = "lhgmfllnkiflkmfm"
password2 = "jtkkmhmpmmjufqll"

def DecryptPassword(password):
    paswd = DecodeBlock(password)
    prev = ""
    for ind in range(8):
        for ans in range(128):
            inp = prev + EncodeChar(chr(ans))+(16-len(prev)-2)*'f'
            if ord(paswd[ind]) == LinExpoEncrypt(DecodeBlock(inp), LINEAR_KEY_TRANS, EXPONENT_KEY)[ind]:
                prev += EncodeChar(chr(ans))
                break
    print(prev)
    return prev