class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


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

def numNodes(root):
    if root == None:
        return 0
    leftCount = numNodes(root.left)
    rightCount = numNodes(root.right)
    return 1 + leftCount + rightCount

def largest_data(root):
    if root == None:
        return -1 #ideally return -inf assuming that tree has all +ve num
    leftLargest = largest_data(root.left)
    rightLargest = largest_data(root.right)
    largest = max(leftLargest,rightLargest,root.data)
    return largest

def tree_height(root):
    if root == None:
        return 0

    left_h = tree_height(root.left)
    right_h = tree_height(root.right)

    return max(left_h,right_h)+1

def printDepthK(root,k):
    if root == None:
        return
    if k == 0:
        print(root.data)
        return
    printDepthK(root.left,k-1)
    printDepthK(root.right,k-1)

def numLeafNodes(root):
    if root == None:
        return 0 # for an empety tree there should be no leaf node
    if root.left == None and root.right == None:
            return 1
    numLeafLeft = numLeafNodes(root.left)
    numLeafRight = numLeafNodes(root.right)
    return numLeafLeft + numLeafRight

def removeLeaves(root):
    if root == None:
        return None
    if root.left == None and root.right == None:
        return None
    root.left = removeLeaves(root.left)
    root.right = removeLeaves(root.right)
    return root

def mirror_tranform(root):
    if root == None:
        return 
    l = root.left
    root.left = root.right
    root.right = l
    mirror_tranform(root.left)
    mirror_tranform(root.right)

def balanced(root):
    if root == None:
        return True
    lh = tree_height(root.left)
    rh = tree_height(root.right)
    if (lh - rh) or (rh-lh)> 1:
        return False
    isLeftBalaced =  balanced(root.left)
    isRightBalaced =  balanced(root.right)
    if isLeftBalaced and isRightBalaced:
        return True
    else:
        return False
def getHeightAndCheckBalanced(root): # efficient code to know weather tree is balanced or not
    if root == None:
        return 0,True # as 0 node means balanced and height 0

    lh, isLeftBalanced = getHeightAndCheckBalanced(root.left)
    rh, isRightBalanced = getHeightAndCheckBalanced(root.right)

    h = 1+max(lh,rh)
    if lh-rh > 1 or rh-lh>1:
        return h,False
    if isLeftBalanced and isRightBalanced:
        return h,True
    else:
        return h,False

def get_diameter(root):
    if root == None:
        return 0, 0
    lh,ld = get_diameter(root.left)
    rh, rd = get_diameter(root.right)

    h = 1+max(lh,rh)
    curr_h = lh+rh+1 # current height/curr diameter

    return h, max(curr_h,ld,rd)

import queue
def takeLevelWiseTreeInput():
    q = queue.Queue()
    print("Enter root")
    root_input = int(input())
    if root_input == -1:
        return None
    root = BinaryTreeNode(root_input)
    q.put(root)
    while not q.empty():
        curr_node = q.get()
        print("Enter Left Child of ", curr_node.data)
        leftChildData = int(input())
        print("Enter Right Child of ", curr_node.data)
        rightChildData = int(input())
    
        if leftChildData != -1:
            leftNode = BinaryTreeNode(leftChildData)
            curr_node.left = leftNode
            q.put(leftNode)
        if rightChildData != -1:
            rightNode = BinaryTreeNode(rightChildData)
            curr_node.right = rightNode
            q.put(rightNode)
        
    return root        

def nodeToRootPath(root,s):
    if root == None:
        return None
    if root.data == s:
        l = list()
        l.append(root.data)
        return l
    leftOutput = nodeToRootPath(root.left,s)
    if leftOutput != None:
        leftOutput.append(root.data)
        return leftOutput
    rightOutPut = nodeToRootPath(root.right,s)
    if rightOutPut != None:
        rightOutPut.append(root.data)
        return rightOutPut
    else:
        return None

if __name__ == '__main__':

    # root = treeInput()
    # printTree(root)
    # print(numNodes(root))
    # print(largest_data(root))
    # print(numLeafNodes(root))
    # printDepthK(root,2)
    # root = removeLeaves(root)
    # printTree(root)
    # print(balanced(root))
    # print(getHeightAndCheckBalanced(root))
    root =  takeLevelWiseTreeInput()
    printTree(root)
    print(nodeToRootPath(root,5))
