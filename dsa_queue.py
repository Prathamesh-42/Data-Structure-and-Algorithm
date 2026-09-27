class queue: 
    def __init__(self):
        self.F=-1
        self.R=-1
        self.qt=[0]*5

    def insert(self,x):
        if self.R==4:
            print("Queue overflow....")
            return
        self.R=self.R+1
        self.qt[self.R]=x
        if self.F==-1:  
            self.F=0

    def delete(self):
        if self.F==-1:
            print("Nothing to delete...empty queue")
        x=self.qt[self.F]

        if self.F==self.R:
            self.F=self.R=-1
        else:
            self.F=self.F+1 
        return x

    def display(self):
        if self.F==-1:
            print("Queue underflow") 
        for i in range(self.F,self.R+1):
            print(self.qt[i]," ")

q=queue()
while True:
    ch=int(input("1.Insert\n2.Delete\n3.Display\nEnter choice: "))
    if ch==1:
        data=input("Enter data to insert: ")
        q.insert(data)
    elif ch==2:
        de=q.delete()
        print(f"The deleted node is {de}")
    elif ch==3:
        q.display()
    else:
        break                                                 
    
 