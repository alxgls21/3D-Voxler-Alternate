import pandas as pd
import numpy as np
import pyvista as pv
from scipy.interpolate import griddata
from datetime import datetime

def export_high_quality_images():
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
    p = pv.Plotter(off_screen=True)
    contours = grid.contour(isosurfaces=[0.5, 1.5, 2.5, 3.5])
    p.add_mesh(contours, opacity=0.5, cmap='jet')
    for idx, row in df.groupby('x_coords').first().iterrows():
        center_bh = (row['x'], row['y'], row['z'])
        cylinder = pv.Cylinder(center=center_bh, direction=(0,0,1), radius=0.1, height=4)
        p.add_mesh(cylinder, color='purple')
    p.show_bounds(grid='all', location='all', color='black')
    p.add_axes()
    views = [
        ('front', 'outputs/front_view.png'),
        ('back', 'outputs/back_view.png'), 
        ('left', 'outputs/left_view.png'),
        ('right', 'outputs/right_view.png'),
        ('top', 'outputs/top_view.png')
    ]
    for view_name, filename in views:
        p.view_vector(view_name)
        p.screenshot(filename, window_size=[1920, 1080])
        print(f"Saved {filename}")

def create_validation_report():
    df = pd.read_csv('data/processed/bruse_clean.csv')
    stats_html = df.describe().to_html()
    html_content = f"""
    <html>
    <head>
        <title>3D Model Validation Report</title>
        <style>
            body {{ font-family: Arial, sans-serif; margin: 40px; }}
            h1 {{ color: #2E86AB; }}
            h2 {{ color: #A23B72; }}
            table {{ border-collapse: collapse; width: 100%; }}
            th, td {{ border: 1px solid #ddd; padding: 8px; text-align: left; }}
            th {{ background-color: #f2f2f2; }}
        </style>
    </head>
    <body>
        <h1>3D Geological Model Validation Report</h1>
        <p><strong>Generated:</strong> {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
        <h2>Data Summary</h2>
        <p><strong>Total data points:</strong> {len(df)}</p>
        <p><strong>Value range:</strong> {df['y'].min():.3f} - {df['y'].max():.3f}</p>
        <p><strong>Spatial extent:</strong></p>
        <ul>
            <li>X: {df['x'].min():.3f} - {df['x'].max():.3f}</li>
            <li>Y: {df['y'].min():.3f} - {df['y'].max():.3f}</li>
            <li>Z: {df['z'].min():.3f} - {df['z'].max():.3f}</li>
            <li>Time: {df['time'].min():.3f} - {df['time'].max():.3f}</li>
        </ul>
        <h2>Statistical Summary</h2>
        {stats_html}
        <h2>Recommendations</h2>
        <p>Run validation.py για επιστημονικό έλεγχο αξιοπιστίας του μοντέλου.</p>
        <p>Χρησιμοποίησε interactive_widgets.py για διαδραστική εξερεύνηση.</p>
        <p>Δημιούργησε animation με animation_time.py για χρονική ανάλυση.</p>
    </body>
    </html>
    """
    with open('outputs/validation_report.html', 'w', encoding='utf-8') as f:
        f.write(html_content)
    print("Validation report saved as 'outputs/validation_report.html'")

if __name__ == "__main__":
    export_high_quality_images()
    create_validation_report()
