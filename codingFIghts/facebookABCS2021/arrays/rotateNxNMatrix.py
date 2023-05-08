#rotar clockwise
def rotateMatrix(mat):
    #first row
    p =0
    #ultima row -> siempre -1 
    u = len(mat) -1
    
    #reverse matrix
    #intercambia hasta que se encuentren en la mitad de la matriz, funciona aunque sea par o impar mientras 
    #u > p
    while u > p:
        mat[p],mat[u] = mat[u],mat[p]
        p += 1
        u -= 1
    
    #transpose
    for i in range(len(mat)):
        for j in range(i):
            mat[i][j],mat[j][i] = mat[j][i],mat[i][j]
            
    
    #si quiero rotar anticlockwise haces reverse de nuevo
    # while u > p:
    #     mat[p],mat[u] = mat[u],mat[p]
    #     p += 1
    #     u -= 1
        
    return mat
