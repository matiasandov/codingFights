#recibes un set de characters y la longitud de las permutaciones
#permutaciones son todas las posibles combianciones de un dado set de characters con
#una longitud dada

def toString(List):
    return ''.join(List)

# Function to print permutations of string
# This function takes three parameters:
# 1. String
# 2. Starting index of the string
# 3. Ending index of the string.
def permute(a, l, r):
    
    #cuando el inicio y el final sea la misma posicion, ya lo revolviste bien entonces lo regresas
    if l==r:
        print(toString(a))
    else:
        #para todos los caracteres del string llamras la recursion
        for i in range(l,r+1):
            #se intercambia la posicion inicial  con el que se itera hasta el último
            a[l], a[i] = a[i], a[l]
            #pasas sig posicion
            permute(a, l+1, r)
            a[l], a[i] = a[i], a[l] # backtrack


def string_permutations(alphabet, permutation_length):
    if ((len(alphabet) <= 26) and (permutation_length <=50 )):

        
    