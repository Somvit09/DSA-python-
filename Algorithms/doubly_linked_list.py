class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # Print

    # printing the linked list
    def PrintLinkedList(self):
        if self.head is None:
            print("Linked list is empty")
            return
        n = self.head
        while n is not None:
            print(n.data, end="<-->")
            n = n.next

    # printing linked list from backwords
    def PrintLinkedListBackwords(self):
        n = self.head
        if n is None:
            print("linked list is empty.")
            return 
        while n.next is not None:
            n = n.next
        while n is not None:
            print(n.data, end="<-->")
            n = n.prev
        return 
    
    # Inserting
    
    # inserting node into an empty linkedlist
    def InsertIntoEmptyLL(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
            return
    

    # Insert a node at the begin position of a ll
    def InsertAtBegin(self, data):
        self.InsertIntoEmptyLL(data)
        new_node = Node(data)
        self.head.prev = new_node
        new_node.next = self.head
        self.head = new_node
        return 
    
    # Insert a node from the end
    def InsertFromEnd(self, data):
        self.InsertIntoEmptyLL(data)
        n = self.head
        while n.next is not None:
            n = n.next
        new_node = Node(data)
        new_node.prev = n
        n.next = new_node
        return 
    
    # add node after a node
    def InsertAfterANode(self, data, x):
        self.InsertIntoEmptyLL(data)
        n = self.head
        while n is not None:
            if n.data == x:
                break
            n = n.next
        if n.next is None:
            print(f"could not find the {x} node")
            return
        new_node = Node(data)
        new_node.prev = n
        new_node.next = n.next
        # if x node is the last value then it is necessary to check that the next node of it is none or not.
        if n.next is not None:
            n.next.prev = new_node
        n.next = new_node
        return 
    

    def InsertBeforeANode(self, data, x):
        self.InsertIntoEmptyLL(data)
        n = self.head
        while n is not None:
            if n.data == x:
                break
            n = n.next
        if n.next is None:
            print(f"the node {x} is not present in the linked list")
            return
        new_node = Node(data)
        new_node.prev = n.prev
        new_node.next = n
        # in case if the x node is the head of the linked list then we have to make the new node as a head node otherwise as the below operation
        if n.prev is not None:
            n.prev.next = new_node
        else:
            # n.prev is None means there is no node infront of the hed node. so the head node will be new node
            self.head = new_node
        n.prev = new_node
        return 
    
    # Deleting

    # delete from begin
    def DeleteFromBegin(self):
        if self.head is None:
            print("linked list is empty")
            return
        if self.head.next is None:
            self.head = None
            print("after deleting the one and only or first node")
        else:
            self.head = self.head.next
            self.head.prev = None
        return
    
    # delete from end
    def DeleteFromEnd(self):
        if self.head is None:
            print("linked list is epmty")
            return 
        if self.head.next is None:
            self.head = None
            print("after deleting the one and only or first node")
        else:
            n = self.head
            while n.next is not None:
                n = n.next
            n.prev.next = None
        return
    
    # delete by a specific value
    def DeleteByValue(self, x):
        if self.head is None:
            print("linked list is empty")
            return
        # if head is the only node present in the linked list then
        if self.head.next is None:
            if self.head.data == x:
                self.head = None
            else:
                print(f"node {x} is not present")
            return
        # if there are other nodes except head node then
        else:
            # if x is the head node to be deleted 
            if self.head.data == x:
                self.head = self.head.next
                self.head.prev = None
                print("node deleted")
                return
            # if the x node is somewhere present in the linked list
            n = self.head
            while n.next is not None:
                if n.data == x:
                    break
                n = n.next
            # if the x node is the last node 
            if n.next is None:
                if n.data == x:
                    n.prev.next = None
                else:
                    print(f"node {x} is not present in the linked list.")
                return
            # if it niether the last node or the first node. except it it present at n position then
            n.prev.next = n.next
            n.next.prev = n.prev
        return
            






sol = DoublyLinkedList()
sol.InsertIntoEmptyLL(1)
sol.InsertAtBegin(5)
sol.InsertFromEnd(6)
sol.InsertAfterANode(2, 1)
sol.InsertBeforeANode(4, 1)
sol.DeleteFromBegin()
sol.DeleteFromEnd()
sol.DeleteByValue(1)
sol.PrintLinkedList()