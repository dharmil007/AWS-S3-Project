class Order(object):
    def __init__(self, number, amount):
        self.number = number
        self.amount = amount
        print (self)
    
    def __str__(self):
        return "Order #%s: amount = %s" % (self.number, self.amount)
        
    @property
    def order_number(self):
        return self.number

    def cancel(self):
        self.amount = 0
        print ("Order is cancelled.")
        print (self)
        
class PizzaHut(object):
    
    def __init__(self, price):
        self.price = price

    def order(self):
        return Order(42, self.price)

pizza = PizzaHut(4.99)
order = pizza.order()
print (order.order_number)
order.cancel()
