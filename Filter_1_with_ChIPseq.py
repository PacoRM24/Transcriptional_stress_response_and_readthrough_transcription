#This code will check if RNAPII peaks match within any DoG in MCF10A-ER-Src cells in each condition and replicate

dog_file = r"C:\Users\Paco\Desktop\MCF10A_DoGFinder_ensGene\common_dog_annotation_TPL.bed"
chip_file = r"TSS_InPeaks_TT1peaks.bed"
new_dog_file = "DoGFinder_DoGs_TPL_after_f1.bed"

#Iterate through the RNAPII peaks to find which maps to a DoG
with open(dog_file, "r") as dogs, open(chip_file, "r") as peaks, open(new_dog_file, "w") as new_dogs:
    #Save the data from ChIP-seq file in a list for future iteration through it
    peaks_data = [line.strip() for line in peaks]

    for dog in dogs:

        # Establish the variables for DoG coordinates
        dog_coordinates = dog.strip().split("\t")[:3]
        dog_chr = dog_coordinates[0]
        dog_i = int(dog_coordinates[1])
        dog_f = int(dog_coordinates[2])
        it_has_a_peak = False
        for peak in peaks_data:

            #Establish the variables for RNAPII peak coordinates
            coordinates = peak.strip().split("\t")[:3]
            peak_chr = coordinates[0]
            peak_i = int(coordinates[1])
            peak_f = int(coordinates[2])

            #Compare if the peak coordinate maps into the DoG coordinate
            if peak_chr == dog_chr and peak_i < dog_f and peak_f > dog_i:
                it_has_a_peak = True
                break

        #If the DoG has no peak of RNAPII then it has to be written in the new file
        if not it_has_a_peak:
            new_dogs.write(dog)