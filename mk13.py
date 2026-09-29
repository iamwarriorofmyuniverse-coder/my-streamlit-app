import matplotlib.pyplot as plt

n = int(input("Enter number of departments: "))
departments = []
males = []
females = []

for i in range(n):
    dept = input(f"Enter department name {i+1}: ")
    m = int(input(f"Enter number of male employees in {dept}: "))
    f = int(input(f"Enter number of female employees in {dept}: "))
    departments.append(dept)
    males.append(m)
    females.append(f)

# Plot stacked bar chart2
plt.figure(figsize=(9, 5))
plt.bar(departments, males, label="Males", color="steelblue")
plt.bar(departments, females, bottom=males, label="Females", color="pink")
plt.title("Department-wise Gender Distribution")
plt.xlabel("Departments")
plt.ylabel("No. of Employees")
plt.legend()
plt.tight_layout()
plt.show()