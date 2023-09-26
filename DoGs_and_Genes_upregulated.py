# This code will extract from the DAVID's gene ID conversion tool the Gene Symbols
# and compare them with the genes that are upregulated

conversion_table = r"C:\Users\Paco\Desktop\Pan_ARTDeco_ensGene\analisis_casero_de_expresion_diferencial\ARTDeco_Pan_cells_THZ1_names.txt"
genes_up_file = r"C:\Users\Paco\Desktop\MCF10A_ARTDeco_ensGene\analisis_casero_de_expresion_diferencial\Osmotic_name_genes.txt"

with open(conversion_table, "r") as dogs, open(genes_up_file, "r") as genes_up:

    dogs_names = []
    dogs.readline()
    for dog in dogs:
        dog_name = dog.strip().split("\t")[1]
        dogs_names.append(dog_name)

    c = 0
    for gene in genes_up:
        gene = gene.strip()
        if gene in dogs_names:
            c += 1

    print(c)