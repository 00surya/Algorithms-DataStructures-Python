class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def printTree(root):
    if root == None:
        return
    print(root.data, end=":")
    if root.left != None:
       print(" L->",root.left.data,end=",")
    if root.right != None:
        print(" R->",root.right.data)
    print()
    printTree(root.left)
    printTree(root.right)


def treeInput():
    rootData = int(input())
    if rootData == -1:
        return None

    root = BinaryTreeNode(rootData)
    leftTree = treeInput()
    rightTree = treeInput()
    root.left = leftTree
    root.right = rightTree

    return root

def numNodes(root):
    if root == None:
        return 0
    leftCount = numNodes(root.left)
    rightCount = numNodes(root.right)
    return 1 + leftCount + rightCount


class Traversal:
    #order => root-left-right
    def preOrder(self, root):
        if root == None:
            return
        print(root.data, end = " ")
        self.preOrder(root.left)
        self.preOrder(root.right)
        return
    
    def postOrder(self, root):
        # order => left-right-root
        if root == None:
            return
        self.postOrder(root.left)
        self.postOrder(root.right)
        print(root.data, end=" ")
        return
    
    def inOrder(self, root):
        # order => left-root-right
        if root == None:
            return
        self.inOrder(root.left)
        print(root.data, end = " ")
        self.inOrder(root.right)


if __name__ == '__main__':

    root = treeInput()
    print()
    printTree(root)
    # print(numNodes(root))
    t = Traversal()
    print("Pre-Order")
    t.preOrder(root)
    print()
    # print("Post-Order")
    # t.postOrder(root)
    # print()/
    print("In-Order")
    t.inOrder(root)


