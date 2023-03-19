class Node:

    def __inti__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:

    def __init__(self):
        self.head = None
    

    # printing all the nodes 
    def PrintCircularList(self):
        if self.head is None:
            print("Circular Linked List is empty.")
            return
        n = self.head
        # traversing the linked list until the next occurance of self.head 
        while n:
            print(n.data, end="<-->")
            n = n.next
            if n.next == self.head:
                break
        return
    
    # Insert

    # Insert into an empty list
    def InsertIntoAnEmptyLL(self, new_node):
        # if head is none then head is the new node and its next pointer is pointed to the head node 
        if self.head is None:
            new_node.next = self.head
            self.head = new_node
            return


    # Inserting elements at begining
    def InsertANodeAtBegin(self, data):
        new_node = Node(data)
        self.InsertIntoAnEmptyLL(new_node)
        n = self.head
        # traversing the list until the head to be found
        while n.next is not self.head:
            n = n.next
        n.next = new_node
        new_node.next = self.head
        self.head = new_node
        return


    # Inserting a node to the end 
    def InsertNodeAtEnd(self, data):
        new_node = Node(data)
        self.InsertIntoAnEmptyLL(new_node)
        n = self.head
        while n.next is not self.head:
            n = n.next
        n.next = new_node
        new_node.next = self.head
        return 
    
    # insert node after a node given
    def InsertNodeAfterAGivenNode(self, data, x):
        new_node = Node(data)
        self.InsertIntoAnEmptyLL(data)
        n = self.head
        # traversing the list until find the x th node or next occurance of the head node
        while n:
            if n.data == x:
                break
            n = n.next
            if n is self.head:
                break
        # after coming out of the loop there is 2 possibilities, 1. came out without finding the x node, 2. came out with finding the x node.
        if n is self.head and n.data != x:
            print("node is not present in this circular linked list")
            return 
        # afte finding
        new_node.next = n.next
        n.next = new_node
        return
    
    # Insert a node before a node given
    def InsertANodeBeforeANode(self, data, x):
        new_node = Node(data)
        prev = None
        self.InsertIntoAnEmptyLL(data)
        n = self.head
        # traversing the list until find the x th node or next occurance of the head node
        while n:
            if n.data == x:
                break
            prev = n
            n = n.next
            if n is self.head:
                break
        # after coming out of the loop there is 2 possibilities, 1. came out without finding the x node, 2. came out with finding the x node.
        if n is self.head and n.data != x:
            print(f"the {x} node is not present in the linked list.")
            return
        new_node.next = n
        prev.next = new_node
        return



        