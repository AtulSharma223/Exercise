class shoppingCart:
    def __init__(self):
        self.cart=[]
    def add_item(self,item_name,qty):
        item=(item_name,qty)
        self.cart.append(item)
    
    def remove_item(self,item_name):
        for item in self.cart:
            if item[0] == item_name:
                self.cart.remove(item)
                break
    def totalCost(self):
        total=0
        for item in self.cart:
            total+=item[1]
        return total

cart1=shoppingCart()
cart1.add_item("Papaya",350)
cart1.add_item("Apple",250)
cart1.add_item("Mango",100)
print("Current item in cart")
for item in cart1.cart:
    print(item[0],"-",item[1])

print("total cost is",cart1.totalCost())

cart1.remove_item("Mango")
print("Updated cart ")
for item in cart1.cart:
    print(item[0],"-",item[1])



