## Binary Search Tree Algorithm

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:

    def __init__(self):
        self.root = None


    # printing a BST
    def PrintBST(self):
        return self._PrintBST(self.root)
    
    def _PrintBST(self, root):
        if root:
            print(root.data, end=' ')
            self._PrintBST(root.left)
            self._PrintBST(root.right)
    

    # inserting an node to the left child or right child
    def Insert(self, data):
        # if root is none the inserted node is the root  
        if self.root is None:
            new_node = Node(data)
            self.root = new_node
        elif data == self.root.data:
            return "Node already present"
        else:
            # there is root present , we need to insert node either left subtree or right subtree
            self._Insert(self.root, data)

    def _Insert(self, node, data):
        # if data is lesser than root data then it is in left subtree
        if data < node.data:
            if node.left:
                self._Insert(node.left, data)
            else:
                node.left = Node(data)
        # otherwise it is in right subtree
        else:
            if node.right:
                self._Insert(node.right, data)
            else:
                node.right = Node(data)

    # searching for a node 
    def Search(self, key):
        return self._Search(self.root, key)
    
    def _Search(self, node, key):
        # if got a match in recursive methods then return the print statement
        if node.data == key:
            print("Key is present")
            return
        if key < node.data:
            # if data is lesser than root data then it is in left subtree
            if node.left:
                self._Search(node.left, key)
            else:
                print("node is not present")
        else:
            # otherwise it is in right subtree
            if node.right:
                self._Search(node.right, key)
            else:
                print("node is not present")

    # Traversing the BST

    def InOrderTraversal(self, root):
        if root:
            self.InOrderTraversal(root.left)
            print(root.data, end=' ')
            self.InOrderTraversal(root.right)

    def PreOrderTraversal(self, root):
        if root:
            print(root.data, end=' ')
            self.PreOrderTraversal(root.left)
            self.PreOrderTraversal(root.right)

    def PostOrderTraversal(self, root):
        if root:
            self.PreOrderTraversal(root.left)
            self.PreOrderTraversal(root.right)
            print(root.data, end=' ')

        
bst = BinarySearchTree()
bst.PrintBST()
bst.Insert(4)
bst.Insert(2)
bst.Insert(1)
bst.Insert(3)
bst.Insert(5)
bst.Insert(6)
bst.Search(4)
bst.PrintBST()
bst.InOrderTraversal(bst.root)
bst.PreOrderTraversal(bst.root)
bst.PostOrderTraversal(bst.root)
    