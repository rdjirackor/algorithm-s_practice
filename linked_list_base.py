class Node:
    data=None
    next_node=None

    def __init__(self,data):
        self.data=data
    def __repr__(self):
        return "<Node is:%s>"%self.data
    
class LinkedList:
    def __init__(self):
        self.head=None
    def isEmpty(self):
        return self.head==None
    def size(self):
        current=self.head
        count=0
        while current !=None:
            count+=1
            current=current.next_node
        return count

