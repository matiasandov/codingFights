#split de la lsita para tener k elementos
#primer ahipotesis la
#1. conozco el tamaño de la lista? no 
class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

#computar el tamaño
def getSize(node: Node):
    cont = 0
    while node != None:
        cont = cont +1
        #el actual ahora será el siguiente
        node = node.next 
    return cont

#falto constrint

#recursion
def getKlist(node: Node, k):
    size = getSize(node)
    newBeginning = size - k
    

    #linked list a regresar
    cont = 0
    while cont < newBeginning:
        nodeNext = node.next
        node = None

def kResult(node: Node, k, i):
    #CONT 