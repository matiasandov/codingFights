#selection sort
#se hacen dos ciclos, uno para ir avanzando en las posiciones
#y otro para ir comparando la posicion actual con las siguientes posiciones
#en cada iteracion de comparacion del loop interno, se va guardando la posicion del elemento más pequeño
#que esta entre i y el final del array, cuando se avanza a la sig posicion, el más pequeño actual se intercambia con el comparado en el pasado
def merge_arrays(arr1, arr2):
    a = arr1 +arr2
    for i in range (0, len(a)):
        minAct = i
        # va comparando la posicion actual con las siguientes posiciones
        for j in range (1+i, len(a)):
            if(a[j] < a[minAct]):
                minAct = j
        #ya que compara el elemento i (primer loop) contra todos los posteriores, swap hace swap entre i y el min act
        a[i],a[minAct] = a[minAct], a[i]
    return a