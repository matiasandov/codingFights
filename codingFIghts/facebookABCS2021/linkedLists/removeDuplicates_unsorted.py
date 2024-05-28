# 1 2 2 3
def removeDuplicates(head):
    temp = head
    
    while temp:
        iter = temp.next
        while iter:
            if iter.val == temp.val:
                #importante
                iter.next = iter.next.next
            iter = iter.next
        temp = temp.next