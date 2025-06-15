import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

df = pd.read_csv('data/processed/bruse_clean.csv')

fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

p = ax.scatter(df['x'], df['y'], df['z'], c=df['y'], cmap='viridis', s=20)

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
fig.colorbar(p, label='y value')

plt.title('3D Scatter Plot των δεδομένων')
plt.show()
