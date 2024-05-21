class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str

        Creo que necesito una matriz y puedo llenarla de "" supongo

        Solo hay dos patterns - repetir hasta acabar palabra
        1. Bajar verticalmentente hasta int (incluido)
        2. Escribir cruzado desde ultima posicion 0 hasta int incluido

        Leer row por row
        """
        if numRows == 1 or numRows >= len(s):
            return s
        
        # so if numRows = 3, L = ['', '', '']
        rows = [""] * numRows
        index = 0
        step = 1

        for c in s:
            rows[index] += c

            #si llegaste hasta arriba ahora tienes que empezar a bajar de row
            if index == 0:
                step = 1
            #si llegaste hasta abajo empiezas a subir 
            elif index  == numRows-1:
                step = -1
            
            #subes o bajas en rows dependiendo de steps
            index += step
        
        s = ""
        for i in rows:
            s += i
        return s


            

#version brute force
def convert( s, numRows):
    if numRows == 1 or numRows >= len(s):
            return s

    matrix = []

    for i in range(0, len(s)):
        column = []
        for j in range(0, len(s)):
            column.append("")
        matrix.append(column)
    
    vert = False
    #servira para moverte horizontal
    column = 0
    cont = 0
    rowBack = 0

    for i in range(0,len(s)):

        if cont == numRows-1 or cont == 0:
            matrix[cont][column] = s[i]

            if vert:
                vert = False
                cont -= 1
                column += 1
            else:
                vert = True
                cont +=1

        elif vert and cont < numRows:
            matrix[cont][column] = s[i]
            cont+= 1
        elif vert == False and cont > -1:
            matrix[cont][column] = s[i]
            cont -= 1
            column += 1
        
        
    new = ""

    for i in range(len(s)):
        for j in range(len(s)):
            new += matrix[i][j]
    
    return new


