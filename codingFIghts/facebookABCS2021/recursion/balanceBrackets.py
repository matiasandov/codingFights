
#recorrer todo
#checar si i es open o close
#agregar los open a un stack
#si es close, buscar su open en el stack y borrar
#si la len del stack es mayor a 0, regresas no, si la len es regresas yes
def isBalanced2(s):
    open = ["[","{","("]
    close = ["]","}",")"]
    stack = []
    for i in s:
        if s[i] in open:
            stack.append(s[i])
        
        elif s[i] in close:
            #devovler el index (posicion) de donde se encuentra el bracket en la lista de close
            indexBracket = close.index(s[i])
            #guardas el index de donde esta el open bracket que borraras
            bracketToDelete = stack.index(open[indexBracket])
            #borras el bracket en su debido index
            stack.pop(bracketToDelete)
    return 0

def check2(original, reversed, iter):
    posO = -1
    posC = -2
    #posiciones correspondientes a cada tipo de bracket
    open_list = ["[","{","("]
    close_list = ["]","}",")"]

    for i in range(0, len(open_list)):
        #si encuentra 
         if (original[iter] == open_list[i]):
             posO = i
    
    for i in range(0, len(close_list)):
         if (reversed[iter] == close_list[i]):
             posC = i
    
    #si la posicion de open_list y close_list es diferente, no corresponde el bracket
    if((posC != posO) or (len(original) != len(reversed)) ):
            return "NO"

    #si ya llegaste al final y nunca se devolvio un no y la pos es la misma
    elif( iter == (len(original)-1) and (posO == posC) ):
        return "YES"
    
    else:
        return check(original, reversed, iter+1)


def isBalanced(s):
    reversed = s[::-1]
    print(s)
    print(reversed)
    print("")
    iter = 0
    #el resultado lo guardaras en 
    ans = check(s, reversed, iter)
    return ans


    
def check(original, reversed, iter):
    posO = -1
    posC = -2
    #posiciones correspondientes a cada tipo de bracket
    open_list = ["[","{","("]
    close_list = ["]","}",")"]

    for i in range(0, len(open_list)):
        #si encuentra 
         if (original[iter] == open_list[i]):
             posO = i
    
    for i in range(0, len(close_list)):
         if (reversed[iter] == close_list[i]):
             posC = i
    
    #si la posicion de open_list y close_list es diferente, no corresponde el bracket
    if((posC != posO) or (len(original) != len(reversed)) ):
            return "NO"

    #si ya llegaste al final y nunca se devolvio un no y la pos es la misma
    elif( iter == (len(original)-1) and (posO == posC) ):
        return "YES"
    
    else:
        return check(original, reversed, iter+1)

    
a = ["a", "b","c","d"]
b = "b"

a.pop(1)
print(a.index("e"))
print(a)
#print(reversed)

    #checar que las posiciones espejo sean exactament iguales y pertenezcan a un alfabeto de brackets    
# def checkBalance( brackets):
#     #iterador que empezara desde atras
#     back = len(brackets)
#     mitad = len(brackets)/2
#     inicio = 0

#     while((mitad < back) and (mitad>inicio)):
#         if(brackets[back] != brackets[inicio]):
#             return "NO"
#         else:
#             re
