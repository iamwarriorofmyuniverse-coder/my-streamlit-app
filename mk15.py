import pandas as pd
import matplotlib.pyplot as plt

# Load data
sales = pd.read_csv('sales_data.csv')

# Basic EDA
print("First 5 rows:")
print(sales.head(5))

print("Last 5 rows:")
print(sales.tail(3))
print(sales.sample(3))

print("\nData Info:")
print(sales.info())

print("\nDescriptive Stats:")
print(sales.describe())

print("\nCategory Counts:")
print(sales['Category'].value_counts())

# Visualization
plt.figure(figsize=(12, 8))

# Plot 1: Total Revenue by Category
plt.subplot(2, 2, 1)
sales.groupby('Category')['Revenue'].sum().plot(kind='bar', color=['blue', 'orange'])
plt.title('Total Revenue by Category')
plt.ylabel('Revenue')

# Plot 2: Units Sold Trend
plt.subplot(2, 2, 2)
sales['Date'] = pd.to_datetime(sales['Date'])
sales.set_index('Date')['Units_sold'].plot()
plt.title('Daily Units Sold')
plt.ylabel('Units')

# Plot 3: Region Distribution
plt.subplot(2, 2, 3)
sales['Region'].value_counts().plot(kind='pie', autopct='%1.1f%%')
plt.title('Sales by Region')

# Plot 4: Revenue vs Units
plt.subplot(2, 2, 4)
plt.scatter(sales['Units_sold'], sales['Revenue'])
plt.title('Revenue vs Units Sold')
plt.xlabel('Units Sold')
plt.ylabel('Revenue')

plt.tight_layout()
plt.show()