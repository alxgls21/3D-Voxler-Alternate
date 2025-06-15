import pandas as pd
import numpy as np
from scipy.interpolate import griddata
from sklearn.model_selection import KFold
from sklearn.metrics import mean_squared_error, r2_score
import warnings
warnings.filterwarnings('ignore')

def spatial_cross_validation(df, method='nearest', n_splits=5):
    kf = KFold(n_splits=n_splits, shuffle=True, random_state=42)
    mse_scores = []
    r2_scores = []
    for train_idx, test_idx in kf.split(df):
        train_data = df.iloc[train_idx]
        test_data = df.iloc[test_idx]
        train_points = train_data[['x', 'y', 'z']].values
        train_values = train_data['y'].values
        test_points = test_data[['x', 'y', 'z']].values
        test_values = test_data['y'].values
        predicted = griddata(train_points, train_values, test_points, method=method)
        valid_mask = ~np.isnan(predicted)
        if np.sum(valid_mask) > 0:
            mse = mean_squared_error(test_values[valid_mask], predicted[valid_mask])
            r2 = r2_score(test_values[valid_mask], predicted[valid_mask])
            mse_scores.append(mse)
            r2_scores.append(r2)
    return {
        'mean_mse': np.mean(mse_scores),
        'std_mse': np.std(mse_scores),
        'mean_r2': np.mean(r2_scores),
        'std_r2': np.std(r2_scores)
    }

def bootstrap_uncertainty(df, n_bootstrap=50):
    xi = np.linspace(df['x'].min(), df['x'].max(), 30)
    yi = np.linspace(df['y'].min(), df['y'].max(), 30)
    zi = np.linspace(df['z'].min(), df['z'].max(), 30)
    X, Y, Z = np.meshgrid(xi, yi, zi)
    n_samples = len(df)
    predictions = []
    for i in range(n_bootstrap):
        bootstrap_idx = np.random.choice(n_samples, n_samples, replace=True)
        bootstrap_df = df.iloc[bootstrap_idx]
        bootstrap_points = bootstrap_df[['x', 'y', 'z']].values
        bootstrap_values = bootstrap_df['y'].values
        V_bootstrap = griddata(bootstrap_points, bootstrap_values, (X, Y, Z), method='nearest')
        predictions.append(V_bootstrap)
    predictions = np.array(predictions)
    uncertainty = np.std(predictions, axis=0)
    return uncertainty

if __name__ == "__main__":
    df = pd.read_csv('data/processed/bruse_clean.csv')
    print("=== MODEL VALIDATION ===")
    validation_results = spatial_cross_validation(df)
    print(f"Cross-Validation Results:")
    print(f"R² Score: {validation_results['mean_r2']:.3f} ± {validation_results['std_r2']:.3f}")
    print(f"MSE: {validation_results['mean_mse']:.3f} ± {validation_results['std_mse']:.3f}")
    if validation_results['mean_r2'] > 0.8:
        print("✓ Υψηλή αξιοπιστία μοντέλου - Τα isosurfaces είναι αξιόπιστα")
    elif validation_results['mean_r2'] > 0.6:
        print("⚠ Μέτρια αξιοπιστία - Χρειάζονται επιπλέον δεδομένα")
    else:
        print("✗ Χαμηλή αξιοπιστία - Το μοντέλο χρειάζεται βελτίωση")
    print("\n=== UNCERTAINTY ANALYSIS ===")
    uncertainty = bootstrap_uncertainty(df)
    print(f"Mean uncertainty: {np.nanmean(uncertainty):.3f}")
    print(f"Max uncertainty: {np.nanmax(uncertainty):.3f}")
