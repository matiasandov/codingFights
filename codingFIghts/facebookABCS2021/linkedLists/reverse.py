# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseList(self, head):
        #recibes head->node->node->node
        
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        #empiezas desde el inicio
        iter = head

        #almacenar prev e igual servira como head al regresarlo prev->prev->prev->head que ahora es tail
        prev = None
        
        while iter is not None:
            #en cada ciclo apuntas al siguiente
            after = iter.next
            #----aqui es donde se invierte la flecha
            iter.next = prev
            #update prev
            prev = iter
            #avanzas temp Y SI - ahora temp y after apuntan al mismo nodo pero cambiara en el siguiente ciclo
            # iter = after es igual a hacer iter = iter.next
            iter = after
        
        return prev
        
            
            