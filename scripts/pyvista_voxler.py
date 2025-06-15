import pandas as pd
import numpy as np
import pyvista as pv
from scipy.interpolate import griddata

df = pd.read_csv('data/processed/bruse_clean.csv')

xi = np.linspace(df['x'].min(), df['x'].max(), 60)
yi = np.linspace(df['y'].min(), df['y'].max(), 60)
zi = np.linspace(df['z'].min(), df['z'].max(), 60)
X, Y, Z = np.meshgrid(xi, yi, zi)
points = df[['x', 'y', 'z']].values
values = df['y'].values
V = griddata(points, values, (X, Y, Z), method='nearest')

grid = pv.StructuredGrid(X, Y, Z)
grid['value'] = V.flatten(order='F')

p = pv.Plotter()

isos = [0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5]
opacities = [0.15, 0.18, 0.22, 0.28, 0.35, 0.45, 0.6]
for i, iso in enumerate(isos):
    contour = grid.contour(isosurfaces=[iso])
    p.add_mesh(
        contour,
        opacity=opacities[i],
        cmap='jet',
        scalar_bar_args={'title': 'log(1+[C10C50])'} if i == len(isos) - 1 else None,
        show_scalar_bar=(i == len(isos) - 1)
    )

bounds = grid.bounds
slices = grid.slice_orthogonal(
    x=(bounds[0]+bounds[1])/2,
    y=(bounds[2]+bounds[3])/2,
    z=(bounds[4]+bounds[5])/2
)
p.add_mesh(slices, opacity=0.18, color='gray', show_edges=True)

for idx, row in df.groupby('x_coords').first().iterrows():
    center_bh = (row['x'], row['y'], row['z'])
    cylinder = pv.Cylinder(center=center_bh, direction=(0,0,1), radius=0.11, height=4)
    p.add_mesh(cylinder, color='#7A1FA2', opacity=0.85)
    p.add_point_labels([center_bh], [f"PE{int(idx)}"], font_size=24, point_color='black', point_size=20, bold=True, shape_opacity=0.5)

max_row = df.loc[df['y'].idxmax()]
max_point = (max_row['x'], max_row['y'], max_row['z'])
p.add_point_labels([max_point], ["Max y"], font_size=18, point_color='red', point_size=15, bold=True, shape_opacity=0.8)

p.show_bounds(grid='all', location='all', color='black', font_size=18, use_2d=True)
p.add_axes(line_width=5, color='black')

arrow_length = max(df['x'].max(), df['y'].max(), df['z'].max()) * 1.1
arrows = [
    pv.Arrow(start=(0, 0, 0), direction=(1, 0, 0), tip_length=0.3, tip_radius=0.07, shaft_radius=0.03, scale=arrow_length),
    pv.Arrow(start=(0, 0, 0), direction=(0, 1, 0), tip_length=0.3, tip_radius=0.07, shaft_radius=0.03, scale=arrow_length),
    pv.Arrow(start=(0, 0, 0), direction=(0, 0, 1), tip_length=0.3, tip_radius=0.07, shaft_radius=0.03, scale=arrow_length)
]
p.add_mesh(arrows[0], color='red')
p.add_mesh(arrows[1], color='green')
p.add_mesh(arrows[2], color='blue')

p.add_point_labels([(arrow_length, 0, 0)], ["X [m]"], font_size=24, point_color='red', point_size=0, bold=True)
p.add_point_labels([(0, arrow_length, 0)], ["Y [m]"], font_size=24, point_color='green', point_size=0, bold=True)
p.add_point_labels([(0, 0, arrow_length)], ["Z [m]"], font_size=24, point_color='blue', point_size=0, bold=True)

# Προαιρετικά: αποθήκευση εικόνας
# p.screenshot('outputs/3d_voxler_style.png', window_size=[1920, 1080], transparent_background=False)

p.show()
