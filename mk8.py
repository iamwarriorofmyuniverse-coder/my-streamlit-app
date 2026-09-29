import matplotlib.pyplot as plt

labels = ['Python', 'JavaScript', 'Java', 'C++', 'Go']
sizes = [35, 25, 20, 12, 8]
colors = ['violet', 'orange', 'gold', 'black', 'red']
explode = (0.1, 0, 0, 0, 0)  # highlight Python
fig, ax = plt.subplots(figsize=(8, 6))

# Draw the pie chart
wedges, texts, autotexts = ax.pie(
    sizes,
    labels=labels,
    colors=colors,
    explode=explode,
    autopct='%1.1f%%',
    startangle=90,
    shadow=True,
    textprops={'fontsize': 10}
)

for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontweight('bold')

ax.set_title('Programming Language Usage', fontsize=14, fontweight='bold')
ax.legend(wedges, labels, loc='center left', bbox_to_anchor=(1, 0.5))
plt.tight_layout()
plt.show()