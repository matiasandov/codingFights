"""
Ejemplo: s = "dvdf"
Necesitas guardar los indices de donde viste la ultima aparición de cada caracter
Si lo haces con solo un for sin guardar indices cuando se encuentre la segunda "d" solo quedará guardado como máximo "df"
cuando en realidad el más largo es "vdf" pero cuando estes en la segunda "d" tienes que retroceder a "v" para encontrar longitud máxima 

"""


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        # Diccionario donde guardarás el index más reciente de cada elemento
        char_map = {}
        max_length = 0
        #index de incio de la max length
        start = 0

        #iteras accediendo a indice para poder guardarlo en lugar de for i in s
        for end in range(len(s)):
            # si ya se repitio el elemento en posicion "end", guardas la posición siguiente de la ultima vez que se encontro
            # es decir en "dvdf" se guardaria la posición [1] de s[1] = "v"
            if s[end] in char_map:
                start = max(start, char_map[s[end]] + 1)

            #guardas la última posicion vista (posicion actual)  del caracter actual
            char_map[s[end]] = end

            # calculas length actual +1 porque esta indexada en 0
            length = end - start + 1

            # actualizas la length maxima
            max_length = max(max_length, length)

        return max_length
