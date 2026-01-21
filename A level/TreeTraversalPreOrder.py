#Mark Reed - 15th Jan 2025
#Tree traversal pre order
#Root -> Left -> Right

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Function to perform preorder traversal
def preorderTraversal(root):
  
    # Base case
    if root is None:
        return
      
    # Visit the current node
    print(root.data, end=' ')
    
    # Recur on the left subtree
    preorderTraversal(root.left)
    
    # Recur on the right subtree
    preorderTraversal(root.right)


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.right = Node(6)
    preorderTraversal(root)

