class Solution:
    def longestValidSubstring(self, word: str, forbidden: List[str]) -> int:
        
        #para cada char solo deberas revisar 10 chars mas porque es el max de este
        #usas un set O1 encontrar substring

        """
        1. vas a tener un pointer que guardara el inicio hasta la izq de longest valid string
        2. tengo que tener una window que checa desde la ultima aparicion de un forbidden+1
            -para eso necesitare un pointer

        setF=set(forbidden)
        maxLen=0
        afterForb=0
        for i in range (len(word)):
            #en un punto si ya no estuvo dentro de un rango de 10, mejor recorro 10 lugares
            #ya que no podra encontrar un forbidden mayor a 10
            for j in range (max(afterForb,i-10),i+1):
                #la ventana checa hacia atras s[ultima aparicion: i incluido]
                if word[j:i+1] in setF:
                    afterForb=j+1
                   
            maxLen=max(maxLen,i-afterForb+1)
        return maxLen

        """

        setForb = set(forbidden)
        #after forbidden
        afterForb = 0
        maxLen = 0

        for i in range(len(word)):
            #checar hasta word[i] actual
            #te regresas desde la ultima aparicion de prohibido hasta i
            for j in range(max(i-10, afterForb) , i+1  ):
                if word[j:i+1] in setForb:
                    #donde inicia el prohibido+1 te lo saltas
                    #existen forbidden de un char por eso es importante mas 1
                    afterForb = j+1
            #i es el ultimo reciente y como esta identado en cero su valor real sera +1
            maxLen = max(maxLen,(i+1)-afterForb )
        return maxLen