class Node:
    def __init__(self, roll_no, name):
        self.roll_no = roll_no
        self.name = name
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    # Insert student record
    def insert(self, roll_no, name):
        new_node = Node(roll_no, name)

        if self.root is None:
            self.root = new_node
            return

        current = self.root

        while True:
            if roll_no < current.roll_no:
                if current.left is None:
                    current.left = new_node
                    return
                current = current.left

            else:
                if current.right is None:
                    current.right = new_node
                    return
                current = current.right

    # Non-recursive Inorder Traversal
    def inorder(self):
        stack = []
        current = self.root

        while stack or current:
            while current:
                stack.append(current)
                current = current.left

            current = stack.pop()
            print(current.roll_no, current.name)

            current = current.right

    # Non-recursive Preorder Traversal
    def preorder(self):
        if self.root is None:
            return

        stack = [self.root]

        while stack:
            current = stack.pop()
            print(current.roll_no, current.name)

            if current.right:
                stack.append(current.right)

            if current.left:
                stack.append(current.left)

# Main program
bst = BST()

n = int(input("Enter number of students: "))

for i in range(n):
    roll_no = int(input("Enter Roll No: "))
    name = input("Enter Student Name: ")
    bst.insert(roll_no, name)

print("\nInorder Traversal:")
bst.inorder()

print("\nPreorder Traversal:")
bst.preorder()