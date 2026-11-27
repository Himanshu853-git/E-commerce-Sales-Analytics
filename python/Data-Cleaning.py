import pandas as pd
import numpy as np

customers = pd.read_csv("customers.csv")
products = pd.read_csv("products.csv")
sales= pd.read_csv("sales.csv")

print("CUSTOMERS")
print(customers.info())
print(customers.shape)

print("\nPRODUCTS")
print(products.info())
print(products.shape)

print("\nSALES")
print(sales.info())
print(sales.shape)
print("\nCustomers Missing Values")
print(customers.isnull().sum())

print("\nProducts Missing Values")
print(products.isnull().sum())

print("\nSales Missing Values")
print(sales.isnull().sum())

print("Customer Duplicates:", customers.duplicated().sum())
print("Product Duplicates:", products.duplicated().sum())
print("Sales Duplicates:", sales.duplicated().sum())

print("Duplicate Customer IDs:",
      customers["Customer_ID"].duplicated().sum())

print("Duplicate Product IDs:",
      products["Product_ID"].duplicated().sum())

print("Duplicate Order IDs:",
      sales["Order_ID"].duplicated().sum())

customers["Registration_Date"] = pd.to_datetime(
    customers["Registration_Date"]
)

customers["Date_of_Birth"] = pd.to_datetime(
    customers["Date_of_Birth"]
)

sales["Order_Date"] = pd.to_datetime(
    sales["Order_Date"]
)

sales["Delivery_Date"] = pd.to_datetime(
    sales["Delivery_Date"]
)

print(customers.dtypes)
print(sales.dtypes)
sales["Delivery_Days"] = (
    sales["Delivery_Date"] - sales["Order_Date"]
).dt.days

print(sales["Delivery_Days"].describe())

invalid_delivery = sales[sales["Delivery_Days"] < 0]

print("Invalid Delivery Records:",
      len(invalid_delivery))

sales["Calculated_Order_Value"] = (
    sales["Quantity"] *
    sales["Unit_Price"]
)

difference = sales[
    round(sales["Calculated_Order_Value"],2)
    != round(sales["Order_Value"],2)
]

print("Order Value Mismatch:",
      len(difference))

sales["Coupon_Code"] = sales["Coupon_Code"].fillna("No Coupon")

sales["Review_Text"] = sales["Review_Text"].fillna("No Review")

customers.to_csv(
    "cleaned_data/customers_clean.csv",
    index=False
)

products.to_csv(
    "cleaned_data/products_clean.csv",
    index=False
)

sales.to_csv(
    "cleaned_data/sales_clean.csv",
    index=False
)