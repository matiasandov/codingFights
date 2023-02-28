#solo tienes acceso a la mitad del elemento

#remove the middle element list
#paremeters : only head

#need: lenght of the list

def size(head: Node):
    cont= 0
    #get size 
    while head is not None:
        cont = cont +1
        head = head.next
        
    return cont

def removeMiddle(head: Node):
    
    size = size(head)
    
    #if getting the mid i got a gloat number, should I round to the bigger the number or the smaller?
    #round up, to the floor number
    mid = floor(size/2) 
    
    cont = 0
    while head is not None :
        #head = head.next
        
        #prev element from the middle
        if cont == mid:
            #copying the info of the next elment from the middle, in the middle node
            head.data = head.next.data
            #skipping de next node sicne i already copied the data 
            head = head.next.next
        else:
            head = head.next
            
    return head