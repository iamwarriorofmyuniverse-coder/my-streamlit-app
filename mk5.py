import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(0, 10, 20)
y1 = np.sin(x)
y2 = np.cos(x)

# Create the plot
plt.figure(figsize=(8, 5))
 

plt.plot(x, y1, color='magenta', marker='o', linestyle='-',
         linewidth=2, markersize=6, label='sin(x)')
plt.plot(x, y2, color='gold', marker='s', linestyle='--',
         linewidth=2, markersize=6, label='cos(x)')


plt.title('Sine and Cosine Waves', fontsize=14, fontweight='bold')
plt.xlabel('X-axis', fontsize=12)
plt.ylabel('Y-axis', fontsize=12)
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend(loc='upper right', fontsize=10)

plt.tight_layout()
plt.show()