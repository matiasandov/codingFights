#el pedo es que solo va comparando como si fuera espejo, cuando en realidad debe buscar para cada open bracket
#un close bracket, en la posicion que sea

#recibes un string de un numero y devuelves la suma de todos los digitos, multiplicado por k
def superDigit(n, k):
    #if(n > 1000000 or k > 100000):
        #return 0
    # Write your code here
    newString = n * k
    return superDigit1(newString)

def superDigit1(n):
    if (int(n) < 10 ):
        #si no funciona trata de hacer int()
        return n
    else:
        sum = 0
        for digit in range(0, len(n)):
            sum = sum + int(digit)
        
        return superDigit1(str(sum))


print(superDigit("123", 3))