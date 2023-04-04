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

    def _find_min(self, node):
        while node.left:
            node = node.left
        return node

    # Deletion

    def Delete(self, data):
        return self._Delete(self.root, data)
    
    def _Delete(self, node, data):
        # if node is none
        if node is None:
            print('there is no node in bst')
        # if data is lesser than node data then search the node in left subtree
        if data < node.data:
            if node.left:
                # recursive
                node.left = self._Delete(node.left, data)
            else:
                print('node is not present')
        # if data is greater than node data then search the node in right subtree
        elif data > node.data:
            if node.right:
                node.right = self._Delete(node.right, data)
            else:
                print('node is not present')
        # recursion will not continue for 2 conditions. 1. if the element is not to be found then. 
        # 2. until the data matches the root data in either left subtree or right subtree
        else:# if the root data matches the key or data to be deleted
            # if node has no children
            if not node.left and not node.right:
                node = None
            # if node has left child only
            elif not node.right:
                node = node.left
            # if node has right child only
            elif not node.left:
                node = node.left
            # if node has both childs
            else:
                # then we need to find the smallest node in the right subtree
                successor = self._find_min(node.right)
                # replace the nodes value with the succesors value
                node.data = successor.data
                # recursively delete the successor from the right subtree
                node.right = self._Delete(node.right, successor.data)
        # return the updated node
        return node
    
    # count nodes
    def count_nodes(self, node):
        if not node:
            return 0
        else:
            return 1 + self.count_nodes(node.left) + self.count_nodes(node.right)
        
    # get maximum node
    def maximum_node(self, node):
        if not node:
            return None
        else:
            while node.right:
                node = node.right
            return node.data
        
    # minimum node
    def minimum_node(self, node):
        if not node:
            return None
        else:
            while node.left:
                node = node.left
            return node.data
        
                



        
bst = BinarySearchTree()
bst.PrintBST()
bst.Insert(4)
bst.Insert(2)
bst.Insert(1)
bst.Insert(3)
bst.Insert(5)
bst.Insert(6)
bst.Search(4)
#bst.InOrderTraversal(bst.root)
#bst.PreOrderTraversal(bst.root)
#bst.PostOrderTraversal(bst.root)
bst.Delete(2)
print(bst.count_nodes(bst.root))
print(bst.maximum_node(bst.root))
print(bst.minimum_node(bst.root))
bst.PrintBST()
    