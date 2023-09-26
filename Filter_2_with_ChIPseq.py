# This code will check if there are peaks of RNAPII in the promoters of each DoG-producing gene

# Define the paths to the DoG file after filter 1, the same peaks file used in filter 1, the annotation file that could be found in the ARTDeco directory
# in the preprocess_files
dog_file = # path to DoG file
chip_file = # path to peaks file
annotation_file = # path to annotation file
new_dog_file = # path and name for the output

# Iterate through the RNAPII peaks to find which maps to a DoG-producing gene promoter
with open(dog_file, "r") as dogs, open(chip_file, "r") as peaks, open(annotation_file, "r") as genome, open(new_dog_file, "w") as new_dogs:
    # Save the data from ChIP-seq file and the annotation file in lists for future iteration through them
    peaks_data = [pline.strip() for pline in peaks]
    genome_data = [gline.strip() for gline in genome]
    for dog in dogs:

        # Establish the variables for DoG-producing gene
        dog_gene = dog.strip().split("\t")
        gene_chr = dog_gene[0]
        gene_ID = dog_gene[3]
        gene_strand = dog_gene[5]

        for gene in genome_data:
            gene_info = gene.strip().split("\t")
            if gene_ID == gene_info[3]:
                if gene_strand == "+":
                    gene_i = int(gene_info[1])
                else:
                    gene_i = int(gene_info[2])
                break

        # Establish the coordinates for gene promoter
        promoter_f = gene_i - 200
        promoter_s = gene_i + 200

        it_has_a_peak = False
        for peak in peaks_data:

            # Establish the variables for RNAPII peak coordinates
            coordinates = peak.strip().split("\t")[:3]
            peak_chr = coordinates[0]
            peak_i = int(coordinates[1])
            peak_f = int(coordinates[2])

            # Compare if the peak coordinate maps into the DoG-producing gene promoter
            if peak_chr == gene_chr:
                if promoter_f < peak_f and promoter_f > peak_i:
                    it_has_a_peak = True
                    break
                elif promoter_s > peak_i and promoter_s < peak_f:
                    it_has_a_peak = True
                    break
                elif promoter_f < peak_i and promoter_s > peak_f:
                    it_has_a_peak = True
                    break

        # If the DoG has no peak of RNAPII then it has to be written in the new file
        if it_has_a_peak:
            new_dogs.write(dog)
