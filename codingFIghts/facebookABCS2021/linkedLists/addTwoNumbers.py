class Node:
     def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
#class Solution(object):
def addTwoNumbers( l1: Node, l2: Node):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    #puedo irlos recorriendo y añadirlos a un string y al final invertir ese string y convertirlo en int

    s1 = ""
    s2 = ""
    res = []

    #Node iter1 = l1
    #Node iter2 = l2

    #Recorres toda la mientras no exista un node nulo
    while l1 is not None:
        #agregas valor como string
        s1 += str(l1.val)
        #continuas iterando
        l1 = l1.next

    while l2 is not None:
        s2 += str(l2.val)
        l2 = l2.next

    #invertir
    s1 = s1[::-1]

    s2 = s2[::-1]

    #convertir a int y sumar
    s1 = int(s1)
    s2 = int(s2)
    s3= s1+s2

    s3 = str(s3)


    for i in s3:
        res.append(i)

    return res

    #Time: O(N)
    #Space: O(N)

#main
