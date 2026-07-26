# -------- Step 1: Loading libraries ---------
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# -------- Step 2: Load your dataset ---------
df= pd.read_csv("bhatbhateni_sales.csv")

# -------- Step 3: Inspect your dataset ---------
print(df.head())                  # first 5 rows
print("Rows, Columns:", df.shape) # shape
print("Columns:", df.columns)     # column names

# -------- Step 4: Understand data types and structures ---------
print(df.dtypes)
print(df[["Quantity", "UnitPrice", "TotalAmount"]].describe())

# -------- Step 5: Detect Data Quality Issues ---------

# a: nulls per column
print(df.isnull().sum())
print(df.isnull().mean() * 100)

# b: duplicate rows
print("Duplicate rows:", df.duplicated().sum())

# c: rows sharing a TransactionID (multi-item orders)
same_transaction = df[df.duplicated(subset="TransactionID", keep=False)]
print("Rows sharing a TransactionID:", len(same_transaction))

# d: check TotalAmount vs Quantity * UnitPrice
df["check_total"] = df["Quantity"] * df["UnitPrice"]
wrong_total = df[df["TotalAmount"] != df["check_total"]]
print("Wrong totals:", len(wrong_total))
df = df.drop(columns=["check_total"])

# -------- Step 6: Handle Duplicate Rows ---------
print("Before:", df.shape[0])
df = df.drop_duplicates()

# b
print("After:", df.shape[0])
print("Remaining duplicates:", df.duplicated().sum())

# -------- Step 7: Handle Missing Values ---------

# a - CustomerName
df['CustomerName'] = df['CustomerName'].fillna('Unknown Customer')

# b - ProductCategory (fill using most common category overall)
most_common_category = df['ProductCategory'].mode()[0]
df['ProductCategory'] = df['ProductCategory'].fillna(most_common_category)

# c - UnitPrice (recalculate from TotalAmount and Quantity)
df['UnitPrice'] = df['UnitPrice'].fillna(df['TotalAmount'] / df['Quantity'])

# d - PaymentMethod (flag as Unknown, don't guess)
df['PaymentMethod'] = df['PaymentMethod'].fillna('Unknown')

# e - confirm nothing is missing anymore
print(df.isnull().sum())

# -------- Step 8: Data Cleaning & Feature Engineering ---------

# a: convert Date to datetime and pull out useful parts
df["Date"] = pd.to_datetime(df["Date"])
df["Year"] = df["Date"].dt.year
df["Month"] = df["Date"].dt.month
df["DayOfWeek"] = df["Date"].dt.day_name()
df["IsWeekend"] = df["DayOfWeek"].isin(["Saturday", "Sunday"])

# b: split Branch into City
df["City"] = df["Branch"].str.split(" - ").str[0]

# c: recompute TotalAmount now that UnitPrice is fully filled in
df["TotalAmount"] = df["Quantity"] * df["UnitPrice"]

# -------- Step 9: Univariate Analysis ---------

# a: transactions per product category
print(df["ProductCategory"].value_counts())
df["ProductCategory"].value_counts().plot(kind="bar")
plt.title("Transactions per Category")
plt.show()

# b: transactions per branch
print(df["Branch"].value_counts())
df["Branch"].value_counts().plot(kind="barh")
plt.title("Transactions per Branch")
plt.show()

# c: most common payment method
print(df["PaymentMethod"].value_counts())

# d: distribution of TotalAmount
df["TotalAmount"].plot(kind="hist", bins=50)
plt.title("Distribution of TotalAmount")
plt.show()
print("Skew:", df["TotalAmount"].skew())

# -------- Step 10: Sales Trend Analysis (Time Series) ---------

# a - revenue per month
monthly_sales = df.groupby('Month')['TotalAmount'].sum()
print(monthly_sales)
monthly_sales.plot(kind='line', marker='o')
plt.title('Monthly Revenue')
plt.show()

# b - weekend vs weekday revenue
weekend_sales = df.groupby('IsWeekend')['TotalAmount'].sum()
print(weekend_sales)   # False = weekday, True = weekend

# c - revenue by day of week
day_sales = df.groupby('DayOfWeek')['TotalAmount'].sum()
print(day_sales)
print("Best day:", day_sales.idxmax())

# -------- Step 11: ranch & City Performance Analysis ---------

# a: total revenue per branch
branch_revenue = df.groupby("Branch")["TotalAmount"].sum()
print(branch_revenue.sort_values(ascending=False))

# b: average transaction value per branch
branch_avg = df.groupby("Branch")["TotalAmount"].mean()
print(branch_avg.sort_values(ascending=False))

# c: total revenue per city
city_revenue = df.groupby("City")["TotalAmount"].sum()
print(city_revenue.sort_values(ascending=False))

# -------- Step 12: Product Category & Product Analysis ---------

# a: category revenue vs category transaction count
cat_revenue = df.groupby("ProductCategory")["TotalAmount"].sum()
print(cat_revenue.sort_values(ascending=False))

cat_count = df.groupby("ProductCategory")["TransactionID"].count()
print(cat_count.sort_values(ascending=False))

# b: top 10 products by quantity sold
top_qty = df.groupby("ProductName")["Quantity"].sum()
print(top_qty.sort_values(ascending=False).head(10))

# c: top 10 products by revenue
top_rev = df.groupby("ProductName")["TotalAmount"].sum()
print(top_rev.sort_values(ascending=False).head(10))

# -------- Step 13: Customer Analysis ---------

# a: top 10 customers by total spend
cust_spend = df.groupby(["CustomerID", "CustomerName"])["TotalAmount"].sum()
print(cust_spend.sort_values(ascending=False).head(10))

# b: repeat customers vs one-time customers
orders = df.groupby("CustomerID")["TransactionID"].nunique()
print("Repeat customers:", (orders > 1).sum())
print("One-time customers:", (orders == 1).sum())

# c: average spend per customer
avg_spend = df.groupby("CustomerID")["TotalAmount"].sum().mean()
print("Average spend per customer:", avg_spend)

# -------- Step 14: PAYMENT METHOD ANALYSIS --------
pay_mix = pd.crosstab(df["Branch"], df["PaymentMethod"], normalize="index")
print((pay_mix * 100).round(1))

pay_avg = df.groupby("PaymentMethod")["TotalAmount"].mean()
print(pay_avg.sort_values(ascending=False))

# -------- STEP 15: CORRELATION & OUTLIERS --------
corr = df[["Quantity", "UnitPrice", "TotalAmount"]].corr()
print(corr)
sns.heatmap(corr, annot=True)
plt.show()

Q1 = df["TotalAmount"].quantile(0.25)
Q3 = df["TotalAmount"].quantile(0.75)
IQR = Q3 - Q1
low = Q1 - 1.5 * IQR
high = Q3 + 1.5 * IQR
outliers = df[(df["TotalAmount"] < low) | (df["TotalAmount"] > high)]
print("Outliers:", len(outliers))

# -------- STEP 16: Predictive Modeling (Optional Advanced Step) --------
cols = ["Quantity", "UnitPrice", "Branch", "ProductCategory"]
X = pd.get_dummies(df[cols])
y = df["TotalAmount"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)
print("R2 score:", model.score(X_test, y_test))

importance = pd.Series(model.coef_, index=X.columns)
print(importance.sort_values(key=abs, ascending=False).head(10))