import matplotlib.pyplot as plt
import pandas as pd

# Data from the PCA table
eigenvalues = [6.72, 3.15, 1.89]
variance_percent = [48.0, 22.5, 13.5]
cumulative_percent = [48.0, 70.5, 84.0]
pc_labels = ['PC1', 'PC2', 'PC3']

# Loadings for biplot
loadings_data = {
    'Variable': ['PH', 'EC', 'Turbidity', 'TDS', 'DO', 'BOD', 'As', 'Ca', 'Fe', 'Mg', 'P', 'Pb', 'Zn', 'Mn'],
    'PC1': [0.91, 0.89, 0.96, -0.49, 0.54, 0.16, -0.61, -0.06, -0.37, 0.75, -0.23, -0.54, -0.01, 0.73],
    'PC2': [0.15, -0.06, 0.02, 0.79, -0.57, -0.70, 0.10, 0.85, 0.52, -0.01, 0.54, -0.45, -0.81, -0.42]
}
loadings_df = pd.DataFrame(loadings_data)

# Create figure with subplots
plt.figure(figsize=(12, 5))

# Scree Plot (a)
plt.subplot(1, 2, 1)
bars = plt.bar(pc_labels, variance_percent, color='blue', alpha=0.6)
plt.ylabel('Percentage of Variance Explained', color='blue')
plt.xlabel('Principal Components')
plt.ylim(0, 100)

# Add cumulative line
plt.twinx()
plt.plot(pc_labels, cumulative_percent, 'r-', marker='o')
plt.ylabel('Cumulative Percentage', color='red')
plt.ylim(0, 100)
plt.title('(a) Scree Plot')

# Biplot (b)
plt.subplot(1, 2, 2)
# Plot variable loadings as arrows
for _, row in loadings_df.iterrows():
    plt.arrow(0, 0, row['PC1'], row['PC2'],
              head_width=0.05, head_length=0.05,
              fc='black', ec='black', alpha=0.6)
    plt.text(row['PC1']*1.1, row['PC2']*1.1, row['Variable'],
             color='blue', fontsize=9)

plt.xlabel(f'PC1 ({variance_percent[0]}%)')
plt.ylabel(f'PC2 ({variance_percent[1]}%)')
plt.title('(b) Biplot')
plt.grid(True, linestyle='--', alpha=0.7)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.xlim(-1.1, 1.1)
plt.ylim(-1.1, 1.1)

plt.tight_layout()
plt.show()