import matplotlib.pyplot as plt

# Inputs number of months
n = int(input("Enter the number of months for sales data: "))
months = []
sales = []

# Input monthly sales data
for i in range(n):
    month = input(f"Enter name of month {i+1}: ")
    amount = float(input(f"Enter sales in ₹ for {month}: "))
    months.append(month)
    sales.append(amount)

# Plot line chart
plt.figure(figsize=(10, 5))
plt.plot(months, sales, marker='o', linestyle='-', color='orange')
plt.title("Monthly Sales Report")
plt.xlabel("Month")
plt.ylabel("Sales (in ₹)")
plt.grid(True)
plt.tight_layout()
plt.show()
