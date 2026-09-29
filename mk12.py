import matplotlib.pyplot as plt

n = int(input("Enter number of months: "))
months = []
product_a = []
product_b = []
product_c = []

for i in range(n):
    month = input(f"Enter month {i+1}: ")
    a = float(input(f"Enter sales of Product A in {month}: "))
    b = float(input(f"Enter sales of Product B in {month}: "))
    c = float(input(f"Enter sales of Product C in {month}: "))
    months.append(month)
    product_a.append(a)
    product_b.append(b)
    product_c.append(c)

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(months, product_a, label='Product A', marker='o', color='blue')
plt.plot(months, product_b, label='Product B', marker='s', color='green')
plt.plot(months, product_c, label='Product C', marker='x', color='gold')
plt.title("Product Sales Comparison")
plt.xlabel("Months")
plt.ylabel("Sales (in ₹)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()