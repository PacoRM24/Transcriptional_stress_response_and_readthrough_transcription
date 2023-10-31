# This code will extract the log2 Fold Change from a file and create a heatmap

import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv(dog_file, sep="\t") #change 'dog_file' for the actual path were the file with the log2FC is storage

# Filter the data by p-value <= 0.05
filtered_data = data[data['padj'] <= 0.05]

# Create a Dataframe with the values for log2 fold change
data_fold_change = filtered_data['log2FoldChange']

# Extract the max and min values of log2fc
val_max = data_fold_change.max()
val_min = data_fold_change.min()
print(val_max,val_min)

# Create heatmap
sns.set(font_scale=1)
plt.figure(figsize=(10, 6))
heatmap = sns.heatmap(data_fold_change.to_frame('Log2FC'), cmap="coolwarm", cbar=True, xticklabels=False, yticklabels=False, vmax=5, vmin=-9)  # Establecer yticklabels=False para quitar las etiquetas del eje y

# Add the color bar and a label
cbar = heatmap.collections[0].colorbar
cbar.set_label("Log2 Fold Change", rotation=270, labelpad=15)

# Add the number of DoGs and show the plot
num_genes = len(data_fold_change)
plt.text(0.5, -0.1, f'n={num_genes}', horizontalalignment='center', verticalalignment='center', transform=plt.gca().transAxes)
plt.ylabel("DoGs")
plt.xlabel("THZ1vsDMSO")
plt.show()
