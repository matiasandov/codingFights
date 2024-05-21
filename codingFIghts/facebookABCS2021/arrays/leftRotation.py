#1.tomar las primeras d posiciones y ponerlas en otro array y hacerles pop cada vez que las saques

#2. concatenas lo que resta del vector con el vector de las posiciones que borraste

def rotateLeft(d, arr):
    aux = []
    for i in range(0,d):
        #pones d elementos en el nuevo array
        aux.append(arr.pop(0))
        #borras los que vas agregando
        #arr.pop(0)

    #ya tienes el vector original sin los que querias rotar, ahora les haces append    
    arr.extend(aux)
    return arr
    # Write your code 