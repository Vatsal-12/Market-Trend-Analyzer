import pandas as pd
import matplotlib.pyplot as plt

# 1. Load dataset
df = pd.read_csv("retail_sales_dataset.csv")

# 2. Preprocessing
df['Date'] = pd.to_datetime(df['Date'])  # convert date column
df['Month'] = df['Date'].dt.month
df['DayOfWeek'] = df['Date'].dt.day_name()

# 3. Exploratory Analysis

## a) Monthly Sales Trend
monthly_sales = df.groupby('Month')['Total Amount'].sum()
plt.figure(figsize=(8,5))
monthly_sales.plot(kind='bar', color='skyblue')
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.show()

## b) Weekly Sales Trend
weekly_sales = df.groupby('DayOfWeek')['Total Amount'].mean().reindex(
    ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
)
plt.figure(figsize=(8,5))
weekly_sales.plot(kind='bar', color='orange')
plt.title("Average Sales by Day of Week")
plt.xlabel("Day")
plt.ylabel("Average Sales")
plt.show()

## c) Product Category Sales
product_sales = df.groupby('Product Category')['Total Amount'].sum()
plt.figure(figsize=(6,6))
product_sales.plot(kind='pie', autopct='%1.1f%%', startangle=90)
plt.title("Sales by Product Category")
plt.ylabel("")
plt.show()

## d) Gender-based Analysis
gender_sales = df.groupby('Gender')['Total Amount'].sum()
plt.figure(figsize=(6,5))
gender_sales.plot(kind='bar', color=['green', 'blue'])
plt.title("Sales by Gender")
plt.xlabel("Gender")
plt.ylabel("Total Sales")
plt.show()

## e) Age Group Analysis
age_bins = [0, 18, 30, 45, 60, 100]
age_labels = ['<18', '18-30', '31-45', '46-60', '60+']
df['Age Group'] = pd.cut(df['Age'], bins=age_bins, labels=age_labels)

age_group_sales = df.groupby('Age Group')['Total Amount'].sum()
plt.figure(figsize=(8,5))
age_group_sales.plot(kind='bar', color='purple')
plt.title("Sales by Age Group")
plt.xlabel("Age Group")
plt.ylabel("Total Sales")
plt.show()

# 4. Actionable Insights
print("\n📊 Insights:")

# Best performing month
best_month = monthly_sales.idxmax()
print(f"- Highest sales occurred in month {best_month}.")

# Best day of week
best_day = weekly_sales.idxmax()
print(f"- Customers spend most on {best_day}, consider promotions then.")

# Top product category
best_product = product_sales.idxmax()
print(f"- {best_product} generates maximum revenue, prioritize placement.")

# Gender insights
best_gender = gender_sales.idxmax()
print(f"- {best_gender} customers contribute the most to sales.")

# Age group insights
best_age_group = age_group_sales.idxmax()
print(f"- Customers in age group {best_age_group} are the top spenders.")
