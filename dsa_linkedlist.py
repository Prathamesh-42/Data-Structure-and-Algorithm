class Node: 
    def __init__(self,data):
        self.data=data
        self.next=None
class LL:
    def __init__(self):
        self.head=None 

    def create(self):
        n=int(input("Enter no of books: "))
        if n<=0:
            print("Enter valid no of books..")
            return
        for i in range(1,n+1):
            val=input(f"Enter name for {i} book: ")
            self.insert(val)
        print("Linked list created")

    def insert(self,val):
        new_node=Node(val)
        if self.head is None:
            self.head=new_node 
            return
        temp=self.head
        while temp.next is not None:
            temp=temp.next
        temp.next=new_node
        
    def delete(self,val):
        if self.head is None:
            print("Nothing to delete...")
            return
        if self.head.data==val:
            self.head=self.head.next
            print(f"Book {val} is deleted...")
            return
        prev=self.head
        temp=self.head.next
        while temp is not None:
            if temp.data==val:
                prev.next=temp.next
                print(f"book of {val} is deleted...")
                return
            prev=temp
            temp=temp.next
        print(f"Book {val} not found...")

    def display(self):
        if self.head is None:
            print("Nothing to print..")
        temp=self.head
        while temp is not None:
            print(temp.data,end="->")
            temp=temp.next
        print("None")

l=LL()
while True:
    ch=int(input("\n1.Create\n2.Insert\n3.Delete\n4.Display\n5.Exit\nEnter choice: "))
    if ch==1:
        l.create()
    elif ch==2:
        dat=input("Enter some book to add: ")
        l.insert(dat)
    elif ch==3:
        val=input("Enter book to delete: ")
        l.delete(val)
    elif ch==4:
        l.display()
    else:
        break                                                                        