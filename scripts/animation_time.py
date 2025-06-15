import pandas as pd
import numpy as np
import pyvista as pv
from scipy.interpolate import griddata

def create_time_animation(output_file='outputs/time_evolution.gif'):
    df = pd.read_csv('data/processed/bruse_clean.csv')
    xi = np.linspace(df['x'].min(), df['x'].max(), 40)
    yi = np.linspace(df['y'].min(), df['y'].max(), 40)
    zi = np.linspace(df['z'].min(), df['z'].max(), 40)
    X, Y, Z = np.meshgrid(xi, yi, zi)
    time_steps = sorted(df['time'].unique())
    p = pv.Plotter()
    p.open_gif(output_file, fps=2)
    for i, time_val in enumerate(time_steps[:20]):
        p.clear()
        time_df = df[df['time'] <= time_val]
        if len(time_df) > 10:
            time_points = time_df[['x', 'y', 'z']].values
            time_values = time_df['y'].values
            V_time = griddata(time_points, time_values, (X, Y, Z), method='nearest')
            time_grid = pv.StructuredGrid(X, Y, Z)
            time_grid['value'] = V_time.flatten(order='F')
            if not np.all(np.isnan(V_time)):
                time_contours = time_grid.contour(isosurfaces=[np.nanmedian(V_time)])
                p.add_mesh(time_contours, opacity=0.6, cmap='jet')
            p.add_text(f"Time: {time_val:.3f}", position='upper_left', font_size=14)
            p.show_bounds(grid='all', location='all', color='black')
            p.add_axes()
        p.write_frame()
    p.close()
    print(f"Animation saved as '{output_file}'")

if __name__ == "__main__":
    create_time_animation()
