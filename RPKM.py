# This code will calculate the RPKM values for DoGs found by ARTDeco

import re

#The Paths to the bam_summary file and raw counts of DoGs are saved in variables
bam_summary = r"C:\Users\Paco\Desktop\Pan_ARTDeco_ensGene\summary_files\bam_summary.txt" # Write the path to the bam_summary.txt file from ARTDeco directory
dogs_raw_counts = r"C:\Users\Paco\Desktop\Pan_ARTDeco_ensGene\dogs\all_dogs.raw.txt" # Write the path to the all.dogs.raw.txt file from ARTDeco directory

#A new file for the RPKM results is saved in a a variable
RPKM_file = "RPKM_file.txt"

#First is the extraction of the mapped reads in each condition
conditions_wreads = dict()
with open(bam_summary, "r") as file:
    for line in file:
        if "bam" in line:
            condition = ((line.strip().split("."))[1].split("/"))[1]
            reads = int(re.split(r'\s+', ((line.strip().split("."))[2]))[2])
            conditions_wreads[condition] = reads

#Iterate through the file with the raw counts in all DoGs and create another file with the RPKM values
with open(dogs_raw_counts, "r") as raw_counts, open(RPKM_file, "w") as RPKM:

    #Scaling factors for each column (condition) are obtained
    first_line = raw_counts.readline()
    col_tittles = first_line.strip().split("\t")
    i = 0
    pos_conditions = dict()
    for tittle in col_tittles:
        if tittle in conditions_wreads:
            pos_conditions[i] = conditions_wreads[tittle]
        i += 1

    scaling_factors = dict()
    for val in pos_conditions:
        scaling_factors[val] = pos_conditions[val]/1000000

    #Writing the tittles in each file
    RPKM.write(first_line)

    #Read each line and calculate the RPKM value for each condition
    for line in raw_counts:
        #gene_length = None
        line_values = line.strip().split("\t")
        gene_length = int(line_values[1])
        j = 2
        for counts in line_values[j:]:
            counts = float(counts)
            RPKM_value = (counts / scaling_factors[j]) / (gene_length/1000)
            line_values[j] = RPKM_value
            j += 1

        RPMK_line = "\t".join(str(x) for x in line_values)
        RPKM.write(RPMK_line+"\n")
