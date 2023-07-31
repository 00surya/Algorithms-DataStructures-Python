class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None



class BST:

    def __init__(self):
        self.root = None
        self.numNodes = 0
    
    def printTreeHelper(self,root):
        if root == None:
            return
        print(root.data, end=":")
        if root.left!= None:
            print("L",root.left.data, end=":")
        if root.right !=  None:
            print("R",root.right.data,end="")
        print()
        self.printTreeHelper(root.left)
        self.printTreeHelper(root.right)

        return

    def printTree(self):
        self.printTreeHelper(self.root)
        return

    def isPresentHelper(self, root,data):
        if root == None:
            return False
        if root.data == data:
            return True
        if root.data > data:
            # call on left
            return self.isPresentHelper(self, root.left,data)
        else:
            # call right
            return self.isPresentHelper(self, root.right,data)


    def isPresent(self,data):
        return self.isPresentHelper(self,self.root,data)

    def insertHelper(self,root,data):
        if root is None:
            node = BinaryTreeNode(data)
            return node
        if root.data > data:
            root.left = self.insertHelper(root.left,data)
            return root
        else:
            root.right = self.insertHelper(root.right,data)
            return root

    def insert(self,data):
        self.numNodes += 1
        self.root = self.insertHelper(self.root,data)

    def min(self,root):
        if root == None:
            return 1000
        if root.left == None:
            return root.data

        return self.min(root.left)

    def deleteDataHelper(self,root,data):
        if root == None:
            return False, None

        if root.data < data:
            deleted, newRightNode = self.deleteDataHelper(root.right,data)
            root.right = newRightNode
            return deleted, root # as overall root is not going to change

        elif root.data > data:
            deleted, newLeftNode = self.deleteDataHelper(root.left,data)
            root.left = newLeftNode
            return deleted, root 

        else: # if root.data == data

            # root is leaf
            if root.left == None and root.right == None:
                return True, None

            #root has one child
            elif root.left == None:
                return True, root.right

            elif root.right == None:
                return True, root.left
            
            # root has two child
            else:
                min_right = self.min(root.right)
                root.data = min_right
                deleted, newRightNode = self.deleteDataHelper(root.right,root.data)
                root.right = newRightNode
                return True, root


    def deleteData(self,data):
        deleted, newRoot = self.deleteDataHelper(self.root,data)
        if deleted:
            self.numNodes -= 1
        self.root = newRoot
        return deleted

    def count(self):
        return self.numNodes











def min_tree(root):
    if root == None:
        return 10000
    left_min = min_tree(root.left)
    right_min = min_tree(root.right)

    return min(left_min,right_min,root.data)

def max_tree(root):
    if root == None:
        return -10000
    left_max = max_tree(root.left)
    right_max = max_tree(root.right)

    return max(left_max,right_max,root.data)


def isBst(root):
    if root == None:
        return True
    left_max = max_tree(root.left)
    right_min = min_tree(root.right)
    # print(left_max)
    # print(right_min)
    if root.data > right_min:
        return False
    elif root.data <= left_max:
        return False

    isLeftBst = isBst(root.left)
    isRightBst = isBst(root.right)

    return isLeftBst and isRightBst

# improved verison
def isBst2(root): 
    if root == None:
        return 10000,-10000,True

    left_min, left_max, isLeftBst = isBst2(root.left)
    right_min, right_max, isRightBst = isBst2(root.right)

    minimum = min(left_min,right_min,root.data)
    maximum = max(left_max,right_max,root.data)
    
    isTreeBst = True
    if root.data <= left_max or root.data > right_min:
        isTreeBst = False
    if not (isLeftBst) or not (isRightBst):
        isTreeBst = False

    return minimum, maximum, isTreeBst



    

if __name__ == "__main__":
    # bst = BST()
    # bst.insert(10)
    # bst.insert(5)
    # bst.insert(12)
    # bst.printTree()
    # print(bst.count())
    # print(bst.root.data)
    # check_bst = isBst2(bst.root)
    # print(check_bst[2])

    # print(bst.deleteData(12),"find")
    # bst.printTree()
    b = BST()
    q = int(input())
    while (q > 0) :
        li = [int(ele) for ele in input().strip().split()]
        choice = li[0]
        q-=1
        if choice == 1:
            data = li[1]
            b.insert(data)
        elif choice == 2:
            data = li[1]
            b.deleteData(data)
        elif choice == 3:
            data = li[1]
            ans = b.isPresent(data)
            if ans is True:
                print('true')
            else:
                print('false')
        else:
            b.printTree()


