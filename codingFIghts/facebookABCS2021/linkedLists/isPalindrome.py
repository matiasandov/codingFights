def isPalindrome(head):
    temp = head
    stack = ()
    slow = head
    fast = head

    while fast:
        stack.add(slow.val)
        slow = slow.next
        fast = fast.next.next
    
    while slow:
        if slow.val == stack.pop():
            slow = slow.next
        else:
            return False
    
    return True


#pinecone
#github