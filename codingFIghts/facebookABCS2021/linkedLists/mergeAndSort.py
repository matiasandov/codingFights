class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

def merge_sorted_lists(first, second):
    res = None
    
    #fslta poner si esta vacia una u otra 
    
    #no necesitas poner while porque es recusrivo
    if first is None:
        return second
    if second is None:
        return first
    
    
    if first.data <= second.data:
        #guardas el mas pequeno
        res = first
        #vas checando a si el siguiente ed mas pequeno que el secone                
        #vas haciendo apend a res 
        res.next = merge_sorted_lists(first.next , second)
    else:
        res = second
        res.next = merge_sorted_lists(first, second.next)
    
    return res