class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    
    # Time Complexity :  O(n)
    # Space Complexity : O(1)
    def middleNode(self, head):
        temp = head
        #temp.next.next va a ir avanzando 2x lo que head avance
        #lo confuso aqui es temp 
        while temp is not None and temp.next is not None:
            #head contendra el puntero que eventualmente llegara a la mitad cuando el otro llegue al final
            head = head.next
            temp = temp.next.next
            
            
        return head
    
    
    
    
    
    
    
    #O(2n)
    def middleNode_past(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        #es importante si solo hay uno regresar en automatico
        if head.next is None:
            return head

        temp = head
        cont = 0
        new = None

        while temp is not None:
            cont += 1
            temp = temp.next

        mid = cont//2 

        #reiniciar variables
        cont = 0
        temp = head

        while cont < mid:
            if cont == mid-1:
                new = temp.next
                return new 
            else:
                temp = temp.next
                cont+= 1
        
        return new
            

