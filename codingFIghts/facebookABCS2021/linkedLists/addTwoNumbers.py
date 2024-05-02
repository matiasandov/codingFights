class Node:
     def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

#usando LL
#tiempo O(N)
#spacio O(1)
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        #1. recorrer las listas obtener el int en orden correcto de ambas listas
        #2. sumar numero
        #3. invertir los digitos en una lista
        #4. regresar la lista

        #si haces (10 elevado a N  * temp.val) te va a dar el valor de la posicion del val
        #ejemplo para 342, 
        #    cuando N = 0 temp.val = 2 si haces  2*(10**0) = 2*(1) = 2 y eso lo acumulas sum = 2
        #    cuando N = 1 temp.val = 4 si haces 4*(10**1) = 40 y eso acumulas sum = 40 + 2

        power1 = 0
        power2 = 0
        sum = 0
        while l1 or l2:
            if l1:
                sum += (l1.val * (10**power1) )
                power1 += 1
                l1 = l1.next
            
            if l2:
                sum += (l2.val * (10**power2) )
                power2 += 1
                l2 = l2.next
            
            
        if sum == 0:
            return ListNode(0)

        res = ListNode(0)
        temp = res
        
        while sum > 0 and temp:
            val = sum % 10
            sum//=10
            temp.next = ListNode(val)
            temp = temp.next

        return res.next

#usando strings        
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
