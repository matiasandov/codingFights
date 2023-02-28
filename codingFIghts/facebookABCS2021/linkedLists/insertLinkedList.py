#!/bin/python3

import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

#
# Complete the 'insert_at_position' function below.
#
# The function is expected to return an INTEGER_SINGLY_LINKED_LIST.
# The function accepts following parameters:
#  1. INTEGER_SINGLY_LINKED_LIST head
#  2. INTEGER val
#  3. INTEGER pos
#

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#

#la pos es en formato index 0
def insert_at_position(head: SinglyLinkedListNode, val, pos):
    cont = 0
    iter = head
    # Write your code here
    
    while iter is not None:
        #si llegas a la posicion deseada
        #le haces -1 porque debes de ponerselo antes de llegar a la posicion deseada, no ya que el cont va en la posicion deaseada
        
        #si se quiere poner en head
        if pos == 0:
            #nuevo nodo
            newNode = SinglyLinkedListNode(val)
            #guardas head inicial
            lastHead = iter
            #pones el nuevo nodo(que ahora esta en la cabeza) apuntando a la head pasada 
            newNode.next = lastHead
            #ahora el iterador empieza en el nuevo nodo
            iter = newNode
            
            
            
        if cont == pos-1:
            #creas el nuevo nodo
            newNode = SinglyLinkedListNode(val)
            
            #guardas el que sigue
            oldNext = iter.next 
            
            #agregas el nuevo como nuevo next del iter actual
            iter.next = newNode
            
            #juntas el nuevo nodo insertado con el antiguo next que le seguia
            newNode.next = oldNext
            
            #maybe aqui hacer iter = newNode aunque siento que ya se perderia
            #iter.next = oldNext
        
        iter = iter.next

        cont = cont + 1
    return head
