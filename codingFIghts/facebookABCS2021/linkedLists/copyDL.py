class DoublyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None
        #apuntador a anterior
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        #tienes la cola
        self.tail = None

    def insert_node(self, node_data):
        node = DoublyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            #el nuevo sera el siguiente de la cola
            self.tail.next = node
            #al insertar el prev sera la cola de la lista
            node.prev = self.tail

        self.tail = node

def print_doubly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

#
# Complete the 'copy_dll' function below.
#
# The function is expected to return an INTEGER_DOUBLY_LINKED_LIST.
# The function accepts INTEGER_DOUBLY_LINKED_LIST dll as parameter.
#

#
# For your reference:
#
# DoublyLinkedListNode:
#     int data
#     DoublyLinkedListNode next
#     DoublyLinkedListNode prev
#
#

def copy_dll(head: DoublyLinkedListNode):
    #iterador para ir avanzando 
    iter =  head

    #nodo head de la copia
    copy = None

    #iterador de la copia que ira haciendo append
    copyIter = None
    
    #mientras no llegues al final
    while iter is not None:

        #creas nodo temporal con los datos que se pasaron 
        #este nodo se actualiza con  iter = iter.next
        visited = DoublyLinkedListNode(iter.data)
        
        #si es el head, copias tal cual el head en copy (solo una vez estara nulo
        # o sea la primera vez que checas el head)
        if copy is None:
            #copy tendra la head de la copia
            copy = visited
        #si es cualquier otro nodo diferente al head
        else:
            #ccopyIter va haciendo apend con .next
            #copia el visitado actual que es diferente al head
            copyIter.next = visited
            #lo ligas al anterior supongo
            copyIter.prev = visited.prev
        #se copia a lista copiada con visisted
        copyIter = visited
        #iteras sobre la lsita 
        iter = iter.next
    return copy
            