#remover duplicados de una linked list no ordenada

#comparar cada elemento contra todos los elementos -> complejdiad On2

#podria ahcerlo mas optimo no pasando el mismo lugar ya checado

#podria hacerle push a todos los elementos de una lista 

#mientras no sean null se agrega a lista

#falto preguntar cosas
#1. si al lsita esta vacio
#2. pregutnar si hay una maxima longitud de la lista?

class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next
   
set1 = set()
#estas modifcando el set por lo que no debes regresarla 
def removeDuplicates(list_iter: Node, set):
    #si esta vacia la regresas
    if list_iter is None or list_iter.next is None:
        return list_iter 
    
    #en python se usan sets
    set.add(list_iter)
    return removeDuplicates(list_iter.next, set)

    

