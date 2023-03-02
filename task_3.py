import pandas as pd

df = pd.read_csv("test_file.csv")
# print(df)

class Orders:
    def __init__(self, order_id, df):
        self.order_id = order_id
        self.df = df

    def calculate_total(self):
        df_1 = self.df[self.df['order.order_id'] == self.order_id]
        df_2 = df_1[['id', 'sales_amt', 'discount']]
        df_2['final_amt'] = df_2['sales_amt'] - df_2['discount']

        return df_2
    
class Discount(Orders):
    def __init__(self, order_id, df):
        super().__init__(order_id, df)
        

    def calculate_final_amt(self):
        df = Orders.calculate_total(self)
        total_amt = 0

        for i, j in df.iterrows():
            total_amt += j['final_amt']

        return total_amt
      

# CA-2017-100111 = 339.798
discount_1 = Discount('CA-2017-100111', df)
print(discount_1.calculate_final_amt())





