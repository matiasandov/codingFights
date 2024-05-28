class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        """
        | candle

        n of plates * between candles |* |
        
        1. registrar index de cada candle
        2. Para cada substring debo encontrar la posicion candle | mas cercana al inicio y al final con bisect
        3. a partir de ahi puedo 
            1.contar cuantos elementos absolutos hay desde rightMost-leftMost y 
            2. como tengo sus index registrados, cada index entre indexRight indexLeft representara una candle

          bot
            * * * | * * | * * | *
            0 1 2 3 4 5 6 7 8 9 10
    candles       3     6     9 
    index         0     1     2

            total elemetos (9 - 3) - elementos que son velas(2-0)
                            6 - 2 = 4 solo hay 4 estrellas

        """

        res = []

        cand = []
       
        for i in range(len(s)):
            if s[i] == "|":
                cand.append(i)
        print(cand)
        for i in queries:
            bot = i[0]
            top = i[1]

            #index
            leftMost = bisect.bisect_left(cand, bot)
            #BISECT ESTA INDEXADO EN 1
            rightMost = bisect.bisect(cand, top)-1

            if leftMost < rightMost:
                total = cand[rightMost] - cand[leftMost]
                res.append(total - (rightMost-leftMost))
            else:
                res.append(0)
      
        return res