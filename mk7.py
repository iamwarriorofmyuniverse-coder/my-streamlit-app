import matplotlib.pyplot as plt
import numpy as np

categories = ['Python', 'JavaScript', 'Java', 'C++', 'Go']
values_2023 = [45, 38, 30, 22, 15]
values_2024 = [52, 41, 27, 25, 21]
values_2025 = [58, 43, 24, 28, 26]  

x = np.arange(len(categories))
width = 0.25  

# Create the plot
fig, ax = plt.subplots(figsize=(10, 5))

bars1 = ax.barh(x - width, values_2023, width, label='2023', color='red', edgecolor='black')
bars2 = ax.barh(x, values_2024, width, label='2024', color='gold', edgecolor='black')
bars3 = ax.barh(x + width, values_2025, width, label='2025', color='green', edgecolor='black')


ax.set_title('Programming Language Popularity', fontsize=14, fontweight='bold')
ax.set_xlabel('Languages', fontsize=12)
ax.set_ylabel('Users (in millions)', fontsize=12)
ax.set_xticks(x)
ax.set_xticklabels(categories)
ax.legend()
ax.grid(axis='y', linestyle='--', alpha=0.6)

plt.tight_layout()
plt.show()
