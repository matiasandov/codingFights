class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1



 
my_linked_list = LinkedList(4)

print('Head:', my_linked_list.head.value)
print('Tail:', my_linked_list.tail.value)
print('Length:', my_linked_list.length)

def print_linked_list(head: Node ):
    #debes tener un iterador 
    iter = head
    
    #mientras no llegues al final
    while iter is not None:
        print(iter.data)
        #iterador pasa al siguiente nodo
        iter = iter.next



"""
    EXPECTED OUTPUT:
    ----------------
    Head: 4
    Tail: 4
    Length: 1
    
"""

                                                                                                                    