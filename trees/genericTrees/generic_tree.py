
class TreeNode:

    def __init__(self,data):
        self.data = data
        self.children = []


def printTreeDetailed(root):
    if root == None:
        return
    print(root.data, ":", end="")
    for child in root.children:
        print(child.data,",",end="")
    print()
    for child in root.children:
        printTreeDetailed(child)


def takeTreeInput():
    print("Enter root Data")
    rootData = int(input())
    if rootData == -1:
        return None
    
    root = TreeNode(rootData)

    print("Enter number of children for ",rootData)
    childrenCount = int(input())
    for i in range(childrenCount):
        child = takeTreeInput()
        root.children.append(child)
    return root


import queue

def takeTreeInputLevelWise():
    q = queue.Queue()
    print("Enter the root")
    rootData = int(input())
    if rootData == -1:
        return None
    
    root = TreeNode(rootData)
    q.put(root)
    while not q.empty():
        curr_node = q.get()
        print("Enter number of children for",curr_node.data)
        numChildren = int(input())
        for i in range(numChildren):
            print("Enter next child for ", curr_node.data)
            childData = int(input())
            childNode = TreeNode(childData)
            curr_node.children.append(childNode)
            q.put(childNode)

    return root


# Problem: count the number of nodes in generic tree

def numNodes(root):
    if root == None: # edge case; to takse exception
        return 0 # none tree has 0 child
    count = 1
    for child in root.children:
        count += numNodes(child)
    return count

# Problem: sum of all node
def sumUpNodes(root):
    initial_sum = root.data
    for child in root.children:
        initial_sum += sumUpNodes(child)
    return initial_sum


if __name__ == "__main__":
    # root = takeTreeInput()
    root = takeTreeInputLevelWise()
    printTreeDetailed(root)
    print(numNodes(root))