import collections
class Solution:
    def minimumKeypresses(self, s: str) -> int:
        """
        the most common chars should be at the beginning of the button
        1. contar freq de cada uno en un dicc
        2. ordenar el dicc

        3.rellenar un hash de set para contar despues la posicion 
        3.1 rellenar del 1 al 9 siguiendo el orden en y add diccFreq[i]
        3.2 si ya se llego al 9 reiniciar el contador a 1 y add

        4. iterar palabra if palabra[i] in hashS[palabra[i]] -> obtener posicion + 1 para contar clicks

        """
        #te ahorra espacio usar colection 
        freq = collections.Counter(s)
        
        #invertir y sort values by frequency -> del mas frecuente al menos frecuente
        freq = dict(sorted(freq.items(), key = lambda pair:pair[1], reverse = True))
        
        #como 0/9 es = 0 se va aumentar en la primera iteracion!!!
        posButton = 0
        clicks = 0
        #necesitas enumerate para el index es lo mas importante!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1
        for indexEn, valFreq in enumerate(freq.values()):
            
            if indexEn % 9 == 0:
                posButton += 1

            clicks += posButton * valFreq

        return clicks
