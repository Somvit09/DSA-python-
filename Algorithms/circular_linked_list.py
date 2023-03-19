class Node:

    def __init__(self, data):
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
            if n is self.head:
                print(n.data)
                break
        return
    
    # Insert

    # Insert into an empty list
    def InsertIntoAnEmptyLL(self, data):
        new_node = Node(data)
        # if head is none then head is the new node and its next pointer is pointed to the head node 
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            return


    # Inserting elements at begining
    def InsertANodeAtBegin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            return 
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
    
    # Delete


    # delete node at begin position
    def DeleteNodeBeginPosition(self):
        if self.head is None:
            print("there is no node in this circular linked list")
            return
        # if head is the only node present in the linked list
        if self.head.next is self.head:
            self.head = None
            return
        n = self.head
        # traversing the linked list until the last node
        while n.next is not self.head:
            n = n.next
        n.next = self.head.next
        self.head = self.head.next
        return 
    
    # delete node from end
    def DeleteNodeFromEnd(self):
        if self.head is None:
            print("there is no node in this circular linked list")
            return
        # if head is the only node present in the linked list
        if self.head.next is self.head:
            self.head = None
            return
        n = self.head
        # traversing the linked list until the previous node of the last node
        while n.next.next is not self.head:
            n = n.next
        n.next = self.head
        return 
    
    # delete node by value
    def DeleteNodeByValue(self, x):
        if self.head is None:
            print("there is no node in this circular linked list")
            return
        # if head is the only node present in the linked list
        if self.head.next is self.head:
            if self.head.data == x:
                self.head = None
                return
            print("node is not present")
            return 
        if self.head.next is not None and self.head.data == x:
            n = self.head
            while n.next is not self.head:
                n = n.next
            n.next = self.head.next
            self.head = n.next
            return
        n = self.head
        prev = None
        # traversing the linked list until the last node
        while n:
            if n.data == x:
                break
            prev = n
            n = n.next
            if n is self.head:
                break
        # after coming out of the loop there are 2 possibilities, 1. came out without finding the x node, 2. came out with finding the x node.
        # if not find
        if n.data != x and n == self.head:
            print(f"{x} node is not present in this linked list")
            return
        # if finds
        prev.next = n.next
        return
        
sol = CircularLinkedList()
sol.InsertIntoAnEmptyLL(5)
sol.InsertANodeAtBegin(4)
sol.InsertANodeAtBegin(3)
sol.InsertNodeAtEnd(6)
sol.InsertNodeAtEnd(7)
sol.InsertNodeAtEnd(8)
sol.InsertANodeAtBegin(2)
sol.InsertNodeAfterAGivenNode(9, 8)
sol.InsertNodeAfterAGivenNode(10, 4)
sol.InsertANodeBeforeANode(11, 10)
sol.DeleteNodeBeginPosition()
sol.DeleteNodeFromEnd()
sol.DeleteNodeByValue(11)
sol.DeleteNodeByValue(10)
sol.DeleteNodeByValue(3)
sol.DeleteNodeByValue(4)
sol.PrintCircularList()
        



        