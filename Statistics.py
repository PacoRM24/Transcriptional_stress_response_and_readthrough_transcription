# This code will calculate the t statistics and p-values for the DoGs in a file

import numpy as np
import pandas as pd
from scipy import stats

# Load the data from a file with the RPKM values
expression_data = pd.read_csv(r"C:\Users\Paco\Desktop\Pan_ARTDeco_ensGene\analisis_casero_de_expresion_diferencial\MAtriz_de_expresion_THZ1.txt", sep="\t")

# Logarithmic transformation of the data
control_columns = ['DMSOR1', 'DMSOR2']
tpl_columns = ['THZ1R1', 'THZ1R2'] #Write the name columns depending on the data analyzed, TPL or THZ1
expression_data[control_columns] = np.log1p(expression_data[control_columns])
expression_data[tpl_columns] = np.log1p(expression_data[tpl_columns])

# Add a small smoothing constant
sc = 0.001
expression_data[control_columns] += sc
expression_data[tpl_columns] += sc

# Establish lists to p-values and t-statistics
p_values = []
t_statistics = []

# Iterate through the genes
for i in range(len(expression_data)):
    DMSO_values = expression_data.loc[i, control_columns].astype(float)
    TPL_values = expression_data.loc[i, tpl_columns].astype(float)

    t_statistic, p_value = stats.ttest_ind(DMSO_values, TPL_values)

    p_values.append(p_value)
    t_statistics.append(t_statistic)

# Calculate de log2 fold change
conditions = ['DMSO', 'THZ1'] # Change the problem condition according to the file used
data_combined = pd.DataFrame()

for condition in conditions:
    condition_columns = [col for col in expression_data.columns if condition in col]
    data_combined[condition] = expression_data[condition_columns].mean(axis=1)

data_fold_change = np.log2((data_combined["THZ1"] + sc) / (data_combined["DMSO"] + sc)) # Change THZ1 if it is the case

# Add the log2fc, p-values and t statistics to the data frame
expression_data['log2fc'] = data_fold_change
expression_data['t_statistic'] = t_statistics
expression_data['p-value'] = p_values

# Generate a new file with all the data
expression_data.to_csv("ARTDeco_Pan_cells_Tabla_de_expresion_de_THZ1.csv", index= False) #Change the name if necessary
