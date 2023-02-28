#vas sacando mitades del array -> n log(n)
def binarySearch (arr, l, r, x):
  
    # Si el right es mayor 1 o igual a 1, aun se pude sacar mitad
    if r >= l:
        
        #division sin punto decimal de la mitad (en caso de que la mitad sea impar)
        mid = l + (r - l) // 2
  
        # checas si el elemento buscado es la mitad del array
        if arr[mid] == x:
            return mid
          
        # Si el elemento buscado es mas chico que el elemento en la mitad, solo buscaras a la izquierda
        elif arr[mid] > x:
            return binarySearch(arr, l, mid-1, x)
  
        # Si el elemento buscado es mayor que el valor del elemento en la mitad, solo buscaras a la derecha
        else:
            return binarySearch(arr, mid + 1, r, x)
  
    else:
        # Element is not present in the array
        return -1

# x: elemento buscado
# 0 : inicio de array (left)
# len(arr)-1 : final del (right)
def isBadVersion(arr, x):
    # Write your code here
    result = binarySearch(arr, 0, len(arr)-1, x)