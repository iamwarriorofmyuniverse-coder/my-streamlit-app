import matplotlib.pyplot as plt

n = int(input("Enter number of departments: "))
departments = []
budget = []

# Get Department-wise budget allocation
for i in range(n):
    dept = input(f"Enter department name {i+1}: ")
    amt = float(input(f"Enter allocated budget for {dept} in ₹: "))
    departments.append(dept)
    budget.append(amt)

plt.figure(figsize=(7, 7))
plt.pie(budget, labels=departments, autopct='%1.1f%%', startangle=90,shadow=True)
plt.title("Departmental Budget Allocation")
plt.axis('equal')  # Equal aspect ratio
plt.tight_layout()
plt.show()