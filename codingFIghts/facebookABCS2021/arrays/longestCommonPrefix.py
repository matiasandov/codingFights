def longestCommonPrefix(v) :
    res = ""
    #ordena por orden alfabetico las palabras 
    # asi puedes tomar solo es ultimo y el primero y si se puede iterar
    #a traves de ellos quiere decir que las palabras de en medio también
    #incluyen las mismas letras que el primero y el ultimo
    # entrada:  ["flower","flow","flight"]
    # ordenado: ['flight', 'flow', 'flower']
    # output: "fl"
    v = sorted(v)
    print(v)
    first = v[0]
    #toma ultimo elemento
    last = v[len(v)-1]

    #va a iterar dentro del rango de la longitud de la palabra mas corta
    for i in range(0, min(len(first), len(last))):
        if last[i] != first[i]:
            return res
        else:
            res += first[i]

    return res

   
#["flower","flow","flight"]
def longestCommonPrefix2(arr):
    #1. ordenas ya que al ordenar distancias los 2 elementos mas distintos entre si, entonces te ahorras recorrer el de en medio
    #  si un elemento esta en primero y ultimo, tambien estara en el de en medio
    
    arr = sorted(arr)
    first = arr[0]
    last = arr[len(arr)-1]
    
    for i in range(min(len(first), len(last))):
        if first[i] != last[i]:
            return first[0:i-1]
        
    return ""
    
print(sorted(["flower","flow","flowal"]))