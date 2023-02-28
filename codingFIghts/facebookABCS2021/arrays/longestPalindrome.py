def longestPalindrome(s):
    leng = len(s)
    maxLen = 1
    start = 0
    low = 0
    high = 0

    for i in range(1, leng):
        #------primero considerar que podria ser un palindromo par----
        low = i-1
        high = i

        #va a considerar todos los posibles palindromos espejos a "i"
        while low >= 0 and high < leng and s[low] == s[high]:
            low -= 1
            high += 1

        #una vez acabado el loop te regresas a las posiciones anteriores y
        #y actualizas la max length si es que es mayor a la anterior
        low += 1
        high -= 1

        #Aqui actualizas nueva max length (sumas +1 por la len de python)
        if (high-low+1) > maxLen and s[low] == s[high]:
            start = low
            maxLen = high-low+1

        #encontrar palindromo impar ------------------------------
        low = i-1
        high = i+1

        #va a considerar todos los posibles palindromos espejos a "i"
        while low >= 0 and high < leng and s[low] == s[high]:
            low -= 1
            high += 1

        #una vez acabado el loop te regresas a las posiciones anteriores y
        #y actualizas la max length si es que es mayor a la anterior
        low += 1
        high -= 1

        #actualizas max length si es impar
        if (high-low+1) > maxLen and s[low] == s[high]:
            start = low
            maxLen = high-low+1
    #regresas substring desde el inicio del substring hasta su ultimo caracter del palindromo
    return s[start: start + maxLen]


