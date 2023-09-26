# This code will generate a heatmap after calculate the log2 fold change 

# Import necessary libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Load the CSV file into a DataFrame, specifying the first column as the index
data = pd.read_csv(r"C:\Users\Paco\Desktop\MCF10A_ARTDeco_ensGene\analisis_casero_de_expresion_diferencial\Matriz_de_expresion_af2.txt", sep="\t", index_col=0)

# Extract the names of the conditions ('DMSO' and 'TPL') or ('DMSO' and 'THZ1')
conditions = ['DMSO', 'TPL']

# Create a DataFrame to store the averages for each condition
data_combined = pd.DataFrame()

# Calculate the average for replicates of each condition
for condition in conditions:
    condition_columns = [col for col in data.columns if condition in col]
    data_combined[condition] = data[condition_columns].mean(axis=1)

# Calculate the log2 fold change and add it as a column while considering an adjustment value for values equal to zero
adj_value = 0.001
data_fold_change = np.log2((data_combined["TPL"] + adj_value) / (data_combined["DMSO"] + adj_value))

# Create a DataFrame with log2 fold change values for 'TPL' and 'DMSO'
val_max = max(data_fold_change)
val_min = min(data_fold_change)
print(val_max, val_min)

# Create the heatmap with the data
sns.set(font_scale=1)
plt.figure(figsize=(10, 6))
heatmap = sns.heatmap(data_fold_change.to_frame(), cmap="coolwarm", cbar=True, xticklabels=False, yticklabels=False, vmax=9, vmin=-9)  # Set yticklabels=False to remove y-axis labels

# Add a custom legend
cbar = heatmap.collections[0].colorbar
cbar.set_label("Log2 Fold Change", rotation=270, labelpad=15)

# Add the number of genes at the bottom
num_genes = len(data_combined)
plt.text(0.5, -0.1, f'n={num_genes}', horizontalalignment='center', verticalalignment='center', transform=plt.gca().transAxes)

# Add labels to the axis and show the plot
plt.ylabel("DoGs")
plt.xlabel("TPLvsDMSO")
plt.show()
