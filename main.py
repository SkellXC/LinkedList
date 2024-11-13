

class Node:

    def __init__(self, value=None):
        self.next = None
        self.value = value
    


class LinkedList:
    
    def __init__(self):
        self.head = None
        
    def addAtEnd(self,value):
        newNode = Node(value)
        if not self.head:# If we create an empty node, the head
            
            self.head = newNode# now goes to the new empty node
            return

        current = self.head# Start at the head
        while current.next:# Continue until the value is "None"
            current = current.next
        
        current.next = newNode # Add a new node at the end


    
    def printAllNodes(self):
        current = self.head
        while current:# While the node isn't empty
            print(current.value, end="->")
            current = current.next

        print("None")

    def removeFromStart(self,value):
        if not self.head: # Checks if the list is empty
            print("List is empty")
            return
        
        # If the head is the node to remove (best case)
        # Otherwise we have to traverse the list
        if self.head.value == value:
            self.head = self.head.next 
            return
        
    def removeFromEnd(self,value):
        current = self.head
        while current.next and current.next.next:# If there is any value besides 0, None or False, it becomes True
            if current.next.next:
                current = current.next # go to the second last node
                


"""
linked_list = LinkedList()
linked_list.addAtEnd(10)
linked_list.addAtEnd(20)
linked_list.addAtEnd(30)
linked_list.printAllNodes()  # Output: 10 -> 20 -> 30 -> None"""
