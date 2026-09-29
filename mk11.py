import matplotlib.pyplot as plt

n = int(input("Enter No.of Friends : "))
Friends = []
budget = []

# Get Department-wise budget allocation
for i in range(n):
    dept = input(f"Enter Friend name {i+1}: ")
    amt = float(input(f"Enter allocated budget for {dept} in ₹: "))
    Friends.append(dept)
    budget.append(amt)

plt.figure(figsize=(7, 7))
plt.pie(budget, labels=Friends, autopct='%1.1f%%', startangle=90,shadow=True)
plt.title("TRIP Budget Allocation")
plt.axis('equal')  # Equal aspect ratio
plt.tight_layout()
plt.show()