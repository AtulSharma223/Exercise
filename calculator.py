class calculator:
    def add(self,x,y):
        return x+y
    def sub(self,x,y):
        return x-y
    def mul(self,x,y):
        return x*y
    def div(self,x,y):
        return x//y
        
    
a=int(input("Enter a "))
b=int(input("Enter b "))

calculator1=calculator()
print("Addition is",calculator1.add(a,b))
print("substraction is",calculator1.sub(a,b))
print("Multiplication is",calculator1.mul(a,b))
print("Division is",calculator1.div(a,b))