class queue:
    def __init__(self):
        self.q=[]
    def enqueue(self,value):
        self.q.append(value)
    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            popElement=self.q.pop(0)
            return popElement
    def is_empty(self):
        return len(self.q)==0
    def print(self):
        print("queue is ",self.q)

q1=queue()
print("poped item is ",q1.dequeue())
q1.enqueue(1)
q1.enqueue(2)
q1.enqueue(3)
q1.print()
print("poped item is ",q1.dequeue())
