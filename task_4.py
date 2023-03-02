import pandas as pd

df = pd.read_csv("test_file.csv")
# print(df)

class Orders:
    order_no = 0

    def __init__(self, order_id):
        self.order_id = order_id
        Orders.order_no += 1

    @classmethod
    def get_order_no(cls):
        return Orders.order_no
    
    def display(self):
        return 'order_id = ' + str(self.order_id) 

print(Orders.get_order_no())    
orders_1 = Orders('CA-2017-100111')
print(Orders.get_order_no())    

    
