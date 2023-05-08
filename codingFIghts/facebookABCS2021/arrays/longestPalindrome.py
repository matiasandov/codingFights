def longestPalindrome(s):
    start = 0
    maxLength = 0

    #con los loops anidados vas a hacer posible que todas las letras se comparen contra todas las letras
    for i in range(len(s)):
        
        # Cuando es impar necesita encontrar un espejo a partir de la mitada por eso empiezan en el mismo indez
        left = i
        right = i
        while left >= 0 and right < len(s) and s[left] == s[right]:
            #tienes que sumarle +1 porque esta indexado en 0 la longitud
            if right - left + 1 > maxLength:
                start = left
                #tienes que sumarle +1 porque esta indexado en 0 la longitud
                maxLength = right - left + 1
            left -= 1
            right += 1

        # PAR necesita empezar en diferentes indexes porque si no jamas encontratra un espejo
        #ejemplo #lobbox -> cuando llegue a str[2] o sea la primera b encontrara enseguida la sig b gracias a right = i+1
        left = i
        right = i + 1
        while left >= 0 and right < len(s) and s[left] == s[right]:
            if right - left + 1 > maxLength:
                start = left
                maxLength = right - left + 1
            left -= 1
            right += 1

    return s[start:start+maxLength]



