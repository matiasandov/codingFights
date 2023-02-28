#anagram: que dos palabras tengan las mismas letras pero en diferente orden
#tener dos vectores ASCII
#si la suma de todos los valores(todas las apariciones de cada letra) es la misma para ambos vectores, si es anagrama
def are_anagrams(s1, s2):
    if( (len(s1) != len(s2)) ):
        return 0
    
    else:
        #usas un diccionario, donde el caracter es la key y tendra un value, que es las veces que aparece
        ascii1 = {}
        ascii2 = {}
        check = 0
        for i in s1:
            #cuentas la aparicion de cada caracter, d
            ascii1[i] = ascii1[i] +1 if i in ascii1 else 0

        for j in s2:
            #cuentas la aparicion de cada caracter
            ascii2[j] = ascii2[j] +1 if j in ascii2 else 0
    
    #este debe de compararse elemento por elemento creo
        #for k in ascii2.items():
        if(ascii2 == ascii1):
            return 1
        else:
            return 0
            # print(ascii2[k]," ",ascii1[k], " ", check)
            # check = check +1
    
        # if(check == len(s1)):
        #     return 1

#print(are_anagrams('abcd', 'dlbc'))

def checkRotation(s1):
    s1 = s1[::-1]
    return s1

st = "holaaaaa"
print(checkRotation("hola"))
print(st[:3])
