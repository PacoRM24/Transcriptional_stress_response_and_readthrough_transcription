import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Cargar el archivo CSV en un DataFrame y especificar que la primera columna es el índice
data = pd.read_csv(r"C:\Users\Paco\Desktop\MCF10A_ARTDeco_ensGene\analisis_casero_de_expresion_diferencial\Matriz_de_expresion_af2.txt", sep="\t", index_col=0)

# Extraer los nombres de las condiciones ('DMSOR' y 'TPLR')
conditions = ['DMSO', 'TPL']

# Crear un DataFrame para almacenar los promedios de cada condición
data_combined = pd.DataFrame()

# Calcular el promedio de las réplicas para cada condición
for condition in conditions:
    condition_columns = [col for col in data.columns if condition in col]
    data_combined[condition] = data[condition_columns].mean(axis=1)

# Calcular el log2 del fold change y agregarlo como una columna tomando en cuenta un valor para ajustar los valores iguales a cero
adj_value = 0.001
data_fold_change = np.log2((data_combined["TPL"] + adj_value) / (data_combined["DMSO"] + adj_value))

# Crear un DataFrame con los valores de log2 fold change para TPL y THZ1
#heatmap_data = data_combined[['TPLvsDMSO', 'THZ1vsDMSO']]
val_max = max(data_fold_change)
val_min = min(data_fold_change)
print(val_max,val_min)

# Crear el heatmap con los datos
sns.set(font_scale=1)
plt.figure(figsize=(10, 6))
heatmap = sns.heatmap(data_fold_change.to_frame(), cmap="coolwarm", cbar=True, xticklabels=False, yticklabels=False, vmax=9, vmin=-9)  # Establecer yticklabels=False para quitar las etiquetas del eje y

# Agregar una leyenda personalizada
cbar = heatmap.collections[0].colorbar
cbar.set_label("Log2 Fold Change", rotation=270, labelpad=15)

# Agregar el número de genes en la parte inferior
num_genes = len(data_combined)
plt.text(0.5, -0.1, f'n={num_genes}', horizontalalignment='center', verticalalignment='center', transform=plt.gca().transAxes)

plt.ylabel("DoGs")
plt.xlabel("TPLvsDMSO")
plt.show()
