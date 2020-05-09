# ---------------------------------------
#                  DAY 20
#         Coding Interview Question
#
#           REMOVE DUPLICATES
#  Write code to remove duplicates from
#  an unsorted linked list.
#  FOLLOW UP
#  How would you solve this problem if a
#  temporary buffer is not allowed?
#  
#  Question 2.1 | ctci 6th edition
#
#  by: @estalvgs1999
# ---------------------------------------

class Node:
    
    def __init__(self,data):
        self.data = data
        self.next = None

    def set_next(self,next_node):
        self.next = next_node
        
    

# Linked_List
class Linked_List():


    # List constructor
    def __init__(self):
        self.head = None
        self.length = 0


    # Add a new element to the list
    def add(self,data):

        if not self.head:
            self.head = Node(data)
        else:
            tmp = self.head
        
            while tmp.next:
                tmp = tmp.next
        
            tmp.next = Node(data)
        
        self.length += 1


    # Add an element at the front of the list
    def add_first(self,data):
        tmp = Node(data)


    # Returns the data stored on certain index
    def get(self,index):
        c_node = self.head
        c_index = 0
        if index >= self.length:
            print('IndexError: list index out of range')
            return

        while c_index != index:
            c_node = c_node.next
            c_index+=1
        
        return c_node.data
        

    # Shows the list
    def show(self):
        
        c_node = self.head

        while c_node:
            print('[{}]->'.format(c_node.data),end="")
            c_node = c_node.next
        
        print('\n')




