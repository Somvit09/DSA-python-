class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SingleLinkedList:
    def __init__(self):
        self.head = None

    # Printing Linked list
    def PrintLinkedList(self):
        n: Node = self.head
        if n is None:
            print([])
        else:
            while n is not None:
                print(n.data, end="-->")
                n = n.next

    def insertInEmptyLL(self, data):
        self.head = Node(data=data)

    def insertElementAtLastLL(self, data):
        if self.head is None:
            self.insertInEmptyLL(data=data)
        else:
            n: Node = self.head
            while n.next is not None:
                n = n.next
            n.next = Node(data=data)

    def insertAtBeginningLL(self, data):
        if self.head is None:
            self.insertInEmptyLL(data=data)
        else:
            new_node = Node(data=data)
            new_node.next = self.head
            self.head = new_node

    def insertElementAfterAtXPosition(self, data, x):
        if self.head is None:
            self.insertInEmptyLL(data=data)
        else:
            n = self.head
            while n is not None:
                if n.data == x:
                    break
                n = n.next
            next_ele = n.next
            curr = n
            curr.next = Node(data=data)
            curr.next.next = next_ele

    def insertElementBeforeXPosition(self, data, x):
        if self.head is None:
            self.insertInEmptyLL(data=data)
        else:
            n = self.head
            while n.next is not None:
                if n.next.data == x:
                    break
                n = n.next
            prev_ele = n
            next_ele = n.next
            prev_ele.next = Node(data=data)
            prev_ele.next.next = next_ele

    def deleteHead(self):
        if self.head is None:
            return []
        else:
            self.head = self.head.next

    def deleteNodeFromEnd(self):
        if self.head is None:
            return []
        else:
            n: Node = self.head
            while n.next.next is not None:
                n = n.next
            n.next = None

    def deleteNodeInXPosition(self, x):
        if self.head is None:
            return []
        else:
            n = self.head
            while n.next is not None:
                if n.next.data == x:
                    break
                n = n.next
            n.next = n.next.next

    #Function to rotate a linked list.
    def rotate(self, k):
        i = 0
        while i < k:
            self.sendHeadToLastNode()
            i += 1

    def sendHeadToLastNode(self):
        n = self.head.data
        self.head = self.head.next
        node = self.head
        while node.next is not None:
            node = node.next
        node.next = Node(n)
    #Function to rotate a linked list.

    def createLLUsingAList(self, arr: list):
        self.insertInEmptyLL(data=arr[0])
        for i in range(1, len(arr)):
            self.insertElementAtLastLL(data=arr[i])



n = SingleLinkedList()
n.insertInEmptyLL(data=1)
n.insertElementAtLastLL(data=2)
n.insertElementAtLastLL(data=3)
n.insertElementAtLastLL(data=4)
n.insertElementAtLastLL(data=5)
n.insertAtBeginningLL(data=6)
n.insertElementAfterAtXPosition(data=7, x=1)
n.insertElementAfterAtXPosition(data=8, x=7)
n.insertElementAfterAtXPosition(data=10, x=6)
n.insertElementBeforeXPosition(data=9, x=10)
n.deleteHead()
n.deleteHead()
n.deleteNodeFromEnd()
n.deleteNodeInXPosition(x=1)
n.deleteNodeInXPosition(x=3)
n.PrintLinkedList()
print("\n")
n.rotate(k=3)
n.PrintLinkedList()


### testing
# arr = [10, 20, 30, 40]
# n.createLLUsingAList(arr=arr)
# print("\n")
# n.rotate(k=6)
# n.PrintLinkedList()