import pandas as pd
import numpy as np
import plotly.graph_objects as go
from scipy.interpolate import griddata

df = pd.read_csv('data/processed/bruse_clean.csv')

xi = np.linspace(df['x'].min(), df['x'].max(), 30)
yi = np.linspace(df['y'].min(), df['y'].max(), 30)
zi = np.linspace(df['z'].min(), df['z'].max(), 30)
X, Y, Z = np.meshgrid(xi, yi, zi)

points = df[['x', 'y', 'z']].values
values = df['y'].values
V = griddata(points, values, (X, Y, Z), method='nearest')

print("Σύνολο τιμών στο V:", V.size)
print("Πόσες είναι NaN:", np.isnan(V).sum())
print("Ελάχιστη/Μέγιστη τιμή (χωρίς NaN):", np.nanmin(V), np.nanmax(V))

fig = go.Figure(data=go.Isosurface(
    x=X.flatten(),
    y=Y.flatten(),
    z=Z.flatten(),
    value=V.flatten(),
    isomin=np.nanmin(V),
    isomax=np.nanmax(V),
    surface_count=4,
    colorscale='Jet',
    caps=dict(x_show=False, y_show=False, z_show=False),
    opacity=0.6,
))

fig.update_layout(
    scene=dict(
        xaxis_title='X',
        yaxis_title='Y',
        zaxis_title='Z',
    ),
    title='3D Isosurface Visualization',
)

fig.show()
