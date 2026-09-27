#Library Catalog Navigation
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def create():
    x=input("Enter data to create node (0 to stop): ")
    if x=="0":
        return None
    root=Node(x) #object creation
    print(f"Enter left of {x}:")
    root.left=create()
    print(f"Enter right of {x}:")
    root.right=create()
    return root
root=create()

def preorder(root):
    if root is not None:
        print(root.data)
        preorder(root.left)
        preorder(root.right)

def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.data)
        inorder(root.right)

def postorder(root):
    if root is not None:
        postorder(root.left)
        postorder(root.right)
        print(root.data)

while True:
    ch=int((input("1.Preorder\n2.Inorder\n3.Postorder\nEnter choice: ")))
    if ch==1:
        preorder(root)
    elif ch==2:
        inorder(root)
    elif ch==3:
        postorder(root)
    else:
        print("Invalid..")
        break            