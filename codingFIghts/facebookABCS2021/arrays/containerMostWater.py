#LA BUENA
def maxArea(self, A):
        """
        :type height: List[int]
        :rtype: int
        """
        l = 0
        r = len(A) -1
        area = 0

        while l < r:
            # Calculating the max area
            area = max(area, min(A[l],
                            A[r]) * (r - l))
            #es una manera mas eficiente de computar todos los resultados linealmente
            #en lugar de hacerlo con dos ciclos for que iban de mitad a mitad, porque asi no se computaban todos los resultados
            if A[l] < A[r]:
                l += 1
            else:
                r -= 1
        return area










import math

class Solution(object):
    #NO FUNCIONO PORQUE NO LOGRABA COMPUTAR TODOS LOS POSIBLES VALORES
    def NO_FUNCIONOmaxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        #para la multiplicacion tomar el minimo de la altura por la base 
        #no puedo ordenar el array porque perderia el sentido
        
        res = 0
        #base = abs(i - j)
        fHalf = int(math.floor(len(height)/2))
        sHalf = int(math.ceil((len(height)-1)/2))
        hf = 0
        bf = 0 
        
        #esto se puede optimizar con un while
        for i in range (0,fHalf ):
            for j in range ( len(height)-1 ,sHalf, -1 ):
                base = abs(i - j)
                h = min(height[i],height[j] ) 
                
                if (h*base) > res:
                    res = h*base
                    hf = h
                    bf = base
        
        print(hf)
        print(bf)
        return res
                           
        #tengo que computar todas las posibles soluciones pero de la amnera mas
        #eficiente, pdoria ser como hacer una binarySearch 
                
        