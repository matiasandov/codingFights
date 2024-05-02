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
        #index de inicio de la max length
        start = 0

        #iteras accediendo a index para poder guardarlo en lugar de for i in s
        for end in range(len(s)):
            # si ya se repitio el elemento en posicion "end",
           
            if s[end] in char_map:
                # recorres el inicio de la nueva substring de los caracteres unicos
                #-----------------------------------PARTE MAS IMPORTANTE--------------------------------------
                start = max(start, char_map[s[end]] + 1)

            #guardas la última posicion vista (posicion actual)  del caracter actual
            char_map[s[end]] = end

            # calculas length actual +1 porque esta indexada en 0
            length = end - start + 1

            # actualizas la length maxima
            max_length = max(max_length, length)

        return max_length
