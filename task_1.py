import pandas as pd

df = pd.read_csv("test_file.csv")
print(df)

def calculate_total_active_time(df, state):
    state_df = df[df["order.customer.address.state"] == state].copy()
    state_df["order.order_purchase_date"] = pd.to_datetime(state_df["order.order_purchase_date"])
    state_df = state_df.sort_values("order.order_purchase_date")
    state_df["next_purchase_date"] = state_df["order.order_purchase_date"].shift(-1)
    state_df["total_active_time"] = (state_df["next_purchase_date"] - state_df["order.order_purchase_date"]) / pd.Timedelta(days=1)
    state_df = state_df[state_df["total_active_time"] != 0]

    # state_df.to_csv("demo_file_cal.csv",index=False)
    return round(state_df["total_active_time"].mean(),2)

# Call the function to avg calculate the total active time for each order placed in a particular state
total_active_time_df = calculate_total_active_time(df, "new york")
print(total_active_time_df)