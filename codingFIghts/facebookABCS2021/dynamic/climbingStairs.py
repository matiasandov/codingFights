#programacion dinamica es ir acumulando
class Solution(object):
    def climbStairs(self, n):
        #necesitas sacaar el numero de combinaciones 
        #tienes 2 opciones de step y longitud n 
        # el metodo para lograrlo es que las primeras dos posiciones sera 1 porque
        #solo existen esas dospisbles combinaciones, lo demas se va acumulando
        """
        :type n: int
        :rtype: int
        """
        if n == 0 or n==1:
            #el unico camino es no subir: 1 camino
            return 1
        else:
            res = [0] * (n+1)
            #el unico camino es no subir: 1 camino
            res[0] = 1
            #el unico camino es subir 1 escalon
            res[1] = 1
            
            for i in range(2,n+1):
                #vas a ir acumulando las combinaciones hasta n
                res[i] = res[i-1] + res[i-2]
            
            return res[n]
            