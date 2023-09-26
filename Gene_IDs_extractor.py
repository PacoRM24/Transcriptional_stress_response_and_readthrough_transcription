# This code will extract the ensembl gene IDs from the DoG-producing genes

dog_file = r"C:\Users\Paco\Desktop\MCF10A_ARTDeco_ensGene\analisis_casero_de_expresion_diferencial\ARTDeco_DoGs_DMSOR1_after_f1.bed"
gene_ID_list = "ARTDeco_DoGs_gene_IDs_DMSOR1_after_f1.txt"

with open(dog_file, "r") as dogs, open(gene_ID_list, "w") as gene_list:

    # Generate a list with the ensembl gene IDs from the DoG file
    gene_ids = []
    for dog in dogs:
        gene_id = dog.strip().split("\t")[3]
        gene_ids.append(gene_id)

    gene_list.writelines('\n'.join(gene_ids))