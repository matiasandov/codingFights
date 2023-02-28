#1. obtener un alfabeto rotado
def leftrotate(s, d):
    tmp = s[d : ] + s[0 : d]
    return tmp

def caesarCipher(s, k):
    result = ""
    #alfabetos
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    rotatedAlphabet = leftrotate(alpha, k)

    alphaUp = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    rotatedAlphabetUp = leftrotate(alphaUp, k)
    
    #recorrer string caracter por caracter
    for i in range (0, len(s)):
        #si se encuentra una letra (los simbolos no se cambiaran)
        if(s[i].islower()):
            result = result + rotatedAlphabet[alpha.index(s[i])]
        elif(s[i].isupper()):
             result = result + rotatedAlphabetUp[alphaUp.index(s[i])]
        else:
             result = result + s[i]
    return result