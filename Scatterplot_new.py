import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.patches as mpatches
from scipy.stats import pearsonr

# Cargar los datos de los archivos como DataFrames de Pandas
dogs_df = pd.read_csv(r"C:\Users\Paco\Desktop\Pan_ARTDeco_ensGene\analisis_casero_de_expresion_diferencial\Resultados_con_DESeq2\ARTDeco_Pan_DoGs_Complete_THZ1.cvs", sep='\t')
genome_df = pd.read_csv(r"C:\Users\Paco\Desktop\Pan_ARTDeco_ensGene\analisis_casero_de_expresion_diferencial\Resultados_con_DESeq2\ARTDeco_Pan_GenesExp_THZ1_complete_with_maxisoforms.txt", sep='\t')

# Filtrar los datos de genes con p-value <= 0.05
filtered_genes_df = genome_df[genome_df['padj'].notna() & (genome_df['padj'] <= 0.05)]

# Combinar los datos de genes y DoGs en un único DataFrame usando 'gene_id' como clave
merged_df = pd.merge(filtered_genes_df, dogs_df, on='Gene_ID', suffixes=('_gene', '_dog'))
print(len(merged_df))

# Calcular el coeficiente de correlación de Pearson y el valor p
correlation_coefficient, p_value = pearsonr(merged_df['log2FoldChange_gene'], merged_df['log2FoldChange_dog'])

# Calcular las categorías "Upregulated", "Downregulated" y "No change"
merged_df['category'] = pd.cut(merged_df['log2FoldChange_gene'], bins=[-float('inf'), -1.2, 1.2, float('inf')], labels=["Downregulated", "No change", "Upregulated"])

# Crear un diccionario que mapee las categorías a sus colores correspondientes
category_colors = {"Upregulated": "purple", "No change": "gray", "Downregulated": "blue"}

# Calcular los porcentajes de cada categoría para la leyenda
category_percentages = {category: (merged_df['category'] == category).mean() for category in category_colors.keys()}

# Crear parches para las categorías
legend_patches = [mpatches.Patch(color=color, label=f"{category} ({category_percentages[category] * 100:.1f}%)") for category, color in category_colors.items()]

# Crear el scatterplot utilizando Seaborn
plt.figure(figsize=(12, 6))
sns.scatterplot(data=merged_df, x='log2FoldChange_gene', y='log2FoldChange_dog', hue='category', palette=category_colors)

# Etiquetar los ejes y agregar un título
plt.xlabel('Gene body log2 fold change')
plt.ylabel('DoG region log2 fold change')
plt.title('Gene expression vs DoG expression in pancreatic cancer cells with THZ1')

# Mostrar la leyenda con los parches personalizados
plt.legend(handles=legend_patches, bbox_to_anchor=(0.242, 1))
plt.text(-0.5, -7.7, f'n = {len(merged_df)}')

# Imprimir los resultados
plt.text(1.2, -7.7, f"r = {correlation_coefficient:.3}")
plt.text(3, -7.7, f"p-value = {p_value:.3e}")

# Mostrar el gráfico sin la rejilla
plt.grid(True)

# Ajustar el límite de la figura para eliminar las barras negras
plt.xlim(merged_df['log2FoldChange_gene'].min() - 0.5, merged_df['log2FoldChange_gene'].max() + 0.5)
plt.ylim(merged_df['log2FoldChange_dog'].min() - 0.5, merged_df['log2FoldChange_dog'].max() + 0.5)

# Mostrar el gráfico
plt.show()
