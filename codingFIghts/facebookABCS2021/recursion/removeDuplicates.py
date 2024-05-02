#la lista esta ordenada

def removeDuplicates(head: SinglyLinkedListNode):
    
    #si ya llegaste al kgnal 
    if head is None:
        return head
    
    #aqui es donde tendras que borrar
    
    #mientras el next no sea el final de la lista(porque comparara algo que no existe)
    if head.next is not None:
        #comparas el actual visitado y el siguiente
        if head.data == head.next.data:
            

            #lo pasad apuntando al siguirnte, se salta el que hiciste null 
            head.next = head.next.next
            
            #pasas el nodo actual recursivamente
            #Opcion1.porque si no hay nada que eliminar se saltaria al else y de todos modos avanzaria
            #Opcion2: Pasar head de nuevo recurisvamente porque necesitas comparar de nuevo
            #el visitado actual contra el head.next.next (o sea el sig al que borraro)
            removeDuplicates(head)
        else:
            #si no hay nada que eliminar, avanzas normal al sig nodo
            removeDuplicates(head.next)
        
    return head


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        temp  = head

        while temp and temp.next:
            if temp.val == temp.next.val:
                #1. En uno apuntas
                #te saltas el duplicado
                temp.next = temp.next.next
            else:
                #2. en el otro unes
                #una vez que ya tu next tiene valor diferente, te mueves a ese next 
                temp = temp.next
        return head

        #para 1->1->2->3->3
        """
        loop 1 - apuntas:
        temp = 1
        1->2

        loop2 - unes:
        temp = 2

        loop3 - apuntas :
        temp = 2
        2->3

        loop4 - unes:
        temp = 3

        toop5 
        temp = 3
        3-> None 

        FIN
        """