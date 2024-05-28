class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        #usas un fakeHead para iniciar un nodo en lugar de iniciar uno en none 
        #asi te ahorras problemas de si es none y tus dos listas son None
        fakeHead = tail = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            #apunta al ultimo l1 o l2, es decir recorre la tail al ultimo elemento
            tail = tail.next
        
        #apendeas el resto de la lista que aun tenga elementos que no sea None
        tail.next = l1 or l2
        
        #pasas lo siguiente al fakeHead
        # sin next -> [0,1,1,2,3,4,4]
        # con next -> [1,1,2,3,4,4]
        return fakeHead.next