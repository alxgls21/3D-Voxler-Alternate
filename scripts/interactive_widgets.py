import pandas as pd
import numpy as np
import pyvista as pv
from scipy.interpolate import griddata

def create_interactive_visualization():
    df = pd.read_csv('data/processed/bruse_clean.csv')
    xi = np.linspace(df['x'].min(), df['x'].max(), 50)
    yi = np.linspace(df['y'].min(), df['y'].max(), 50)
    zi = np.linspace(df['z'].min(), df['z'].max(), 50)
    X, Y, Z = np.meshgrid(xi, yi, zi)
    points = df[['x', 'y', 'z']].values
    values = df['y'].values
    V = griddata(points, values, (X, Y, Z), method='nearest')
    grid = pv.StructuredGrid(X, Y, Z)
    grid['value'] = V.flatten(order='F')
    p = pv.Plotter()
    initial_contours = grid.contour(isosurfaces=[1.5])
    contour_actor = p.add_mesh(initial_contours, opacity=0.5, cmap='jet', name='contours')
    def update_isosurface(value):
        p.remove_actor('contours')
        new_contours = grid.contour(isosurfaces=[value])
        p.add_mesh(new_contours, opacity=0.5, cmap='jet', name='contours')
    p.add_slider_widget(
        update_isosurface,
        [df['y'].min(), df['y'].max()],
        value=df['y'].median(),
        title="Isosurface Level",
        pointa=(0.02, 0.9),
        pointb=(0.35, 0.9)
    )
    for idx, row in df.groupby('x_coords').first().iterrows():
        center_bh = (row['x'], row['y'], row['z'])
        cylinder = pv.Cylinder(center=center_bh, direction=(0,0,1), radius=0.1, height=4)
        p.add_mesh(cylinder, color='purple')
        p.add_point_labels([center_bh], [f"PE{int(idx)}"], font_size=20)
    p.show_bounds(grid='all', location='all', color='black')
    p.add_axes()
    return p

if __name__ == "__main__":
    plotter = create_interactive_visualization()
    plotter.show()
