import numpy as np
import pandas as pd

# Define variables and Spearman correlation matrix
variables = ['PH', 'EC', 'Turbidity', 'TDS', 'DO', 'BOD', 'As', 'Ca', 'Fe', 'Mg', 'P', 'Pb', 'Zn', 'Mn']
corr_data = [
    [1.00, 0.88, 0.94, -0.45, 0.45, 0.15, -0.56, -0.04, -0.31, 0.61, -0.20, -0.49, -0.01, 0.61],
    [0.88, 1.00, 0.79, -0.43, 0.54, 0.16, -0.16, 0.00, -0.39, 0.41, 0.04, -0.42, 0.25, 0.77],
    [0.94, 0.79, 1.00, -0.36, 0.57, 0.25, -0.58, -0.18, -0.32, 0.74, -0.29, -0.44, -0.09, 0.69],
    [-0.45, -0.43, -0.36, 1.00, 0.25, 0.52, 0.32, -0.82, 0.82, -0.11, 0.71, -0.49, -0.72, -0.07],
    [0.45, 0.54, 0.57, 0.25, 1.00, 0.88, -0.16, -0.61, 0.11, 0.59, 0.21, -0.40, -0.36, 0.92],
    [0.15, 0.16, 0.25, 0.52, 0.88, 1.00, -0.21, -0.68, 0.47, 0.50, 0.29, -0.36, -0.65, 0.65],
    [-0.56, -0.16, -0.58, 0.32, -0.16, -0.21, 1.00, -0.05, 0.02, -0.63, 0.59, 0.08, 0.41, -0.10],
    [-0.04, 0.00, -0.18, -0.82, -0.61, -0.68, -0.05, 1.00, -0.54, -0.16, -0.64, 0.69, 0.72, -0.32],
    [-0.31, -0.39, -0.32, 0.82, 0.11, 0.47, 0.02, -0.54, 1.00, 0.13, 0.46, -0.51, -0.83, -0.17],
    [0.61, 0.41, 0.74, -0.11, 0.59, 0.50, -0.63, -0.16, 0.13, 1.00, -0.45, -0.29, -0.41, 0.62],
    [-0.20, 0.04, -0.29, 0.71, 0.21, 0.29, 0.59, -0.64, 0.46, -0.45, 1.00, -0.58, -0.25, 0.06],
    [-0.49, -0.42, -0.44, -0.49, -0.40, -0.36, 0.08, 0.69, -0.51, -0.29, -0.58, 1.00, 0.58, -0.30],
    [-0.01, 0.25, -0.09, -0.72, -0.36, -0.65, 0.41, 0.72, -0.83, -0.41, -0.25, 0.58, 1.00, -0.03],
    [0.61, 0.77, 0.69, -0.07, 0.92, 0.65, -0.10, -0.32, -0.17, 0.62, 0.06, -0.30, -0.03, 1.00]
]

corr_matrix = np.array(corr_data)

# Compute eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eigh(corr_matrix)
sorted_indices = np.argsort(eigenvalues)[::-1]
eigenvalues = eigenvalues[sorted_indices]
eigenvectors = eigenvectors[:, sorted_indices]

# Select top 3 components
top3_eigenvalues = eigenvalues[:3]
top3_eigenvectors = eigenvectors[:, :3]

# Compute loadings and communalities
loadings = top3_eigenvectors * np.sqrt(top3_eigenvalues)
communalities = np.sum(loadings**2, axis=1)

# Explained variance and cumulative %
total_variance = len(variables)  # 14 for correlation matrix
explained_variance = (top3_eigenvalues / total_variance) * 100
cumulative_explained = np.cumsum(explained_variance)

# Create DataFrame
pca_table = pd.DataFrame({
    'Parameters (R-mode)': variables,
    'PC1': loadings[:, 0].round(2),
    'PC2': loadings[:, 1].round(2),
    'PC3': loadings[:, 2].round(2),
    'Communalities': communalities.round(2)
})

# Add Eigenvalues, % variance, and cumulative rows
rows = [
    ['Eigenvalues', *top3_eigenvalues.round(2), ''],
    ['% of variance', *explained_variance.round(2), ''],
    ['Cumulative %', *cumulative_explained.round(2), '']
]
for row in rows:
    pca_table.loc[len(pca_table)] = row

print(pca_table.to_string(index=False))