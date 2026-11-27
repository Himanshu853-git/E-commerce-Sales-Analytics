import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

customers = pd.read_csv("cleaned_data/customers_clean.csv")
products = pd.read_csv("cleaned_data/products_clean.csv")
sales = pd.read_csv("cleaned_data/sales_clean.csv")

df = sales.merge(
    customers,
    on="Customer_ID",
    how="left"
)

df = df.merge(
    products,
    on="Product_ID",
    how="left"
)

print(df.shape)
print(df.head())

df.to_csv("cleaned_data/master_dataset.csv",
          index=False)

print("Total Revenue:",
      df["Total_Amount"].sum())

print("Average Order Value:",
      df["Total_Amount"].mean())

print("Total Orders:",
      df["Order_ID"].nunique())

print("Total Customers:",
      df["Customer_ID"].nunique())


    # order_status_distribution
print(df["Order_Status"].value_counts())
plt.figure(figsize=(8,5))
sns.countplot(
    data=df,
    x="Order_Status")
plt.title("Order Status Distribution")
plt.savefig("images/revenue_trend.png")
plt.show()


     # payment_mode_distrbution
print(df["Payment_Mode"].value_counts())

plt.figure(figsize=(8,5))
df["Payment_Mode"].value_counts().plot(
    kind="bar")
plt.title("Payment Modes")
plt.savefig("images/payment_modes.png")
plt.show()


     # monthly_revenue_trend
df["Order_Date"] = pd.to_datetime(
    df["Order_Date"])

monthly_sales = df.groupby(
    df["Order_Date"].dt.to_period("M")
)["Total_Amount"].sum()

monthly_sales.plot(
    figsize=(10,7))
plt.title("Monthly Revenue Trend")
plt.savefig("images/monthly_revenue_trend.png")
plt.show()
    # top_categories
category_sales = df.groupby(
    "Category")["Total_Amount"].sum() \
.sort_values(
    ascending=False)

category_sales.plot(
    kind="bar",
    figsize=(12,6))
plt.title("Revenue by Category")
plt.savefig("images/revenue_by_category.png")
plt.show()


    # top 10 products
top_products = (
    df.groupby("Product_Name")
      ["Total_Amount"]
      .sum()
      .sort_values(
          ascending=False
      )
      .head(10)
)
print(top_products)

top_products.plot(
    kind="barh",
    figsize=(12,8))
plt.title("Top 10 Products")
plt.savefig("images/top_10_products.png")
plt.show()
   # customer_age_distribution
plt.figure(figsize=(10,5))
sns.histplot(
    df["Age"],
    bins=20)
plt.title("Customer Age Distribution")
plt.savefig("images/customer_age_distribution.png")
plt.show()

