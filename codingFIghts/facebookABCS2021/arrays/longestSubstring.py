
def longestUniqueSubsttr(str):
    
    n = len(str)
    
    # Result
    res = 0

    for i in range(n):
        
        # marcar que letras ya visito
        visited = [0] * 256  

        for j in range(i, n):
        #va a comparir i contra todos los otros valores siguentes
            # If current character is visited
            # Break the loop
            if (visited[ord(str[j])] == True):
                break

            # Else update the result if
            # this window is larger, and mark
            # current character as visited.
            else:
                res = max(res, j - i + 1)
                visited[ord(str[j])] = True
        
        # Remove the first character of previous
        # window
        # si encuentra dos repetidos, excluira como la primera 
        #aparicion del repetidoe
        visited[ord(str[i])] = False
    
    return res