def findMergeNode(head1,head2):
   
  #tamano de linked list1
    c1=getCount(head1)
   
  #tamano de ll2
    c2=getCount(head2)
   
    #recorres la lista mas grande hasta posicion D que es donde ya coincide con la lista chica y las recorres en paralelo
  
    if c1 > c2:
        d=c1-c2
        return _getIntersectionNode(d,head1,head2)
    else:
        d=c2-c1
        return _getIntersectionNode(d,head2,head1)
   
   
def _getIntersectionNode(d,head1,head2):
     
     
    current1=head1
    current2=head2
     
    #avanzar en la lista mas larga hasta el elemento D
    for i in range(d):
        if current1 is None:
            return -1
        current1=current1.next
     
    #mientras no llegues al final
    while current1 is not None and current2 is not None:
     
    # checas que tengan la misma direccion con IS, porque tener el mismo data no indica que sean iguales
        if current1 is current2:
            return current1.data # or current2.data ( the value would be same)
     
     #sigues buscando donde la direccion del nodo sea la misma
        current1=current1.next
        current2=current2.next
   
  # Incase, we are not able to find our intersecting point.
    return -1
   
#Function to get the count of a LinkedList
def getCount(node):
    cur=node
    count=0
    while cur is not None:
        count+=1
        cur=cur.next
    return count

#Space O(n)
#Time O(n)