class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoubleLinkedLL:
    def __init__(self):
        self.head: Node = None

    def PrintLL(self):
        if self.head is None:
            return []
        n = self.head
        while n is not None:
            print(n.data, end="<-->")
            n = n.next
        print("\n")

    def PrintLLBackwards(self):
        if self.head is None:
            return []
        n = self.head
        while n.next is not None:
            n = n.next
        while n is not None:
            print(n.data, end="<-->")
            n = n.prev

    def InsertIntoEmptyDLL(self, data):
        self.head = Node(data=data)

    def InsertAtBeginDLL(self, data):
        if self.head is None:
            self.InsertIntoEmptyDLL(data=data)
        new_node = Node(data=data)
        self.head.prev = new_node
        new_node.next = self.head
        self.head = new_node

    def InsertAtEndDLL(self, data):
        if self.head is None:
            self.InsertIntoEmptyDLL(data=data)
        n = self.head
        while n.next is not None:
            n = n.next
        new_node = Node(data=data)
        n.next = new_node
        new_node.prev = n

    def InsertAfterANode(self, data, x):
        if self.head is None:
            self.InsertIntoEmptyDLL(data=data)

        n = self.head
        while n is not None:
            if n.data == x:
                break
            n = n.next
        new_node = Node(data=data)
        if n.next is None:
            n.next = new_node
            new_node.prev = n
        else:
            nn = n.next
            curr = n
            curr.next = new_node
            new_node.prev = curr
            new_node.next = nn
            nn.prev = new_node


    def InsertBeforeANode(self, data, x):
        if self.head is None:
            self.InsertIntoEmptyDLL(data=data)

        n = self.head
        while n is not None:
            if n.data == x:
                break
            n = n.next
        curr = n
        prev = n.prev
        new_node = Node(data=data)
        curr.prev = new_node
        new_node.next = curr
        if prev is not None:
            new_node.prev = prev
            prev.next = new_node
        else:
            self.head = new_node

    def DeleteFrontNode(self):
        if self.head is None:
            return []
        if self.head.next is None:
            self.head = None

        curr = self.head
        nn = curr.next
        self.head = nn
        curr.next = None

    def DeleteLastNode(self):
        if self.head is None:
            return []
        if self.head.next is None:
            self.head = None

        n = self.head
        while n.next is not None:
            n = n.next
        n.prev.next = None

    def DeleteNodeByData(self, data):
        if self.head is None:
            return []
        if self.head.next is None:
            self.head = None

        n = self.head
        if n.data == data:
            self.head = self.head.next
            self.head.prev = None
            return
        while n is not None:
            if n.data == data:
                break
            n = n.next

        if n.next is None:
            n.prev.next = None
        else:
            n.prev.next = n.next
            n.next.prev = n.prev








dll = DoubleLinkedLL()
dll.InsertIntoEmptyDLL(1)
dll.InsertAtBeginDLL(2)
dll.InsertAtBeginDLL(3)
dll.PrintLL()
dll.InsertAtEndDLL(4)
dll.InsertAtEndDLL(5)
dll.PrintLL()
dll.InsertAfterANode(6, 5)
dll.InsertAfterANode(7, 6)
dll.InsertAfterANode(8, 1)
dll.PrintLL()
dll.InsertBeforeANode(9, 3)
dll.InsertBeforeANode(11, 9)
dll.InsertBeforeANode(12, 1)
dll.PrintLL()
dll.DeleteFrontNode()
dll.PrintLL()
dll.DeleteFrontNode()
dll.PrintLL()
dll.DeleteLastNode()
dll.PrintLL()
dll.DeleteNodeByData(1)
dll.PrintLL()
dll.DeleteNodeByData(6)
dll.PrintLL()
dll.DeleteNodeByData(3)
dll.PrintLL()