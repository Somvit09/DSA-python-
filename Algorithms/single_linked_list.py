class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SingleLinkedList:
    def __init__(self):
        self.head = None

    # Printing Linked list
    def PrintLinkedList(self):
        n = self.head
        if n is None:
            print([])
        else:
            while n is not None:
                print(n.data, end="-->")
                n = n.next

    # Insertion

    # normal insertion when linked list is empty
    def InsertElementInAEmptyLinkedList(self, data):
        new_node = Node(data)
        self.head = new_node

    # inserting an element at the end position
    def InsertElementAtLast(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            # looping through the values untill it reaches to the last element
            while n.next is not None:
                n = n.next
            n.next = new_node


    # Inserting element from front of a node
    def InsertAtBegining(self, data):
        new_node = Node(data)
        # checks if the head is none or not.if none head is the new element.
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    # inserting a node after a given position
    def InsertElementAfterAPosition(self, data, x):
        n = self.head
        # if head is none
        if n is None:
            print("Singly linkedlist is empty.")
            self.InsertElementInAEmptyLinkedList(data)
            print("added node as a head node as there is no other node.")
        # if data of head is the value x after which we have to insert the element
        if n.data == x:
            self.InsertElementAtLast(data)
        # if the node is somewhere in the linked list
        while n is not None:
            if n.data == x:
                break
            n = n.next
        if n is None:
            print("Node is not present in single linked list.")
        else:
            new_node = Node(data)
            new_node.next = n.next
            n.next = new_node

    # inserting a node before a given position
    def InsertElementBeforeAPosition(self, data, x):
        n = self.head
        # if head is none
        if n is None:
            print("Singly linkedlist is empty.")
            self.InsertElementInAEmptyLinkedList(data)
            print("added node as a head node as there is no other node.")
        # if data of head is the value x before which we have to insert the element
        if n.data == x:
            self.InsertAtBegining(data)
        # if the node is somewhere in the linked list
        while n.next is not None:
            if n.next.data == x:
                break
            n = n.next
        if n.next is None:
            print("Node is not present in this sigle linked list")
        else:
            new_node = Node(data)
            new_node.next = n.next
            n.next = new_node

    # Deletion

    # delete node from begin
    def DeleteBegin(self):
        if self.head is None:
            print("Linked List is empty")
        elif self.head.next is None:
            self.head = None        
        else:
            self.head = self.head.next

    
    def DeleteNodeFromEnd(self):
        # head is not present
        if self.head is None:
            print("Linked List is empty")
        # head has no next node
        elif self.head.next is None:
            self.head = None
        else:
            # loop through the last node  to delete it
            n = self.head
            while n.next.next is not None:
                n = n.next
            n.next = None

    def DeleteNodeByValue(self, x):
        # head is not present
        if self.head is None:
            print("linked list is empty")
            return 
        # head has next node 
        if self.head.next is not None:
            # if x is the data of head node
            if self.head.data == x:
                self.head = self.head.next
                return 
            # if x is other node present in the linked list
            n = self.head
            while n.next is not None:
                if n.next.data == x:
                    break
                n = n.next
            if n.next is None:
                print("Node is not present.")
                return
            else:
                n.next = n.next.next
        # if head has no next node then           
        else:
            if self.head.data == x:
                self.head = None
            else:
                print("Node is not present in the linked list.")


sol = SingleLinkedList()
sol.PrintLinkedList()
sol.InsertElementInAEmptyLinkedList(5)
sol.InsertElementAtLast(7)
sol.InsertElementAtLast(8)
sol.InsertElementAtLast(9)
sol.InsertAtBegining(4)
sol.InsertElementAfterAPosition(6, 5)
sol.InsertElementBeforeAPosition(10, 9)
sol.DeleteBegin()
sol.DeleteBegin()
sol.DeleteNodeFromEnd()
sol.DeleteNodeByValue(10)
sol.DeleteNodeByValue(7)
sol.DeleteNodeByValue(10)
sol.DeleteNodeByValue(8)
sol.DeleteNodeByValue(6)
sol.DeleteNodeByValue(7)
sol.PrintLinkedList()

