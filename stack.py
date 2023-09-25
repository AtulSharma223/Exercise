class stack:
    def __init__(self):
        self.st=[]

    def push(self,value):
        self.st.append(value)
    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        else:
            return self.st.pop()
    def is_empty(self):
        return len(self.st)==0
    def peek(self):
        if not self.is_empty():
            return self.st[-1]
        else:
            return "Stack is empty"
    def size(self):
        return len(self.st)
    def print(self):
        print("Stack is ",self.st)
    
tempSt=stack()
tempSt.push(12)
tempSt.push(34)
tempSt.push(10)
tempSt.print()
print("stack size:",tempSt.size())
print("Top element:",tempSt.peek())
print("Poped item:",tempSt.pop())

tempSt.print()

