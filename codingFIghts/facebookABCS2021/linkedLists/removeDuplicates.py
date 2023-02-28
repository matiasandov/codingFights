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