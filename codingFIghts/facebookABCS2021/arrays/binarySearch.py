#vas sacando mitades del array -> log(n)
def binarySearch (arr, l, r, x):
  
    # Si el right es mayor l o igual a l, aun se pude sacar mitad
    if r >= l:
        
        #division sin punto decimal de la mitad entre l y r(en caso de que la mitad sea impar)
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

#tiene que estar sorted
#recursivo
def binaryRepaso(arr,x, l, r):
    
    # 0 1 2 3 4  5  6 7 8 9 10
    if l<= r:
        #si dejo r-l//2 y busco 6 se buscaria entre arr[0:5 ] al sacar la mitad
        mid = l + (r-l)//2
        
        if arr[mid]==x:
            return mid
        elif arr[mid] < x:
            return binaryRepaso(arr, x, mid+1, r)
        else :
            return binaryRepaso(arr, x, l, mid-1)
        
    else:
        return -1

arr = [-5,1,2,3,4,5,6,7,8,9,10, 23]
print(binaryRepaso(arr, -5, 0, len(arr)))