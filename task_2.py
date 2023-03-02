import pandas as pd

df = pd.read_csv("test_file.csv")
# print(df)

class Orders:
    def __init__(self, order_id, df):
        self.order_id = order_id
        self.df = df

    def calculate_total(self):
        df_1 = self.df[self.df['order.order_id'] == self.order_id]
        df_2 = df_1[['id', 'sales_amt']]
        total_amt = 0

        for i, j in df_2.iterrows():
            total_amt += j['sales_amt']
        
        return total_amt
    

# US-2014-106992 = 65.872
orders_1 = Orders('US-2014-106992', df)
print(orders_1.calculate_total())





