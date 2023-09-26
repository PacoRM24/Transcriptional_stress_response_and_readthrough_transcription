# This code will compare the IDs from two bed files and write the DoGs in common

dog_file1 = r"C:\Users\Paco\Desktop\Pan_ARTDeco_ensGene\analisis_casero_de_expresion_diferencial\ARTDeco_Pan_cells_TPL_unic_dogs.bed"
dog_file2 = r"C:\Users\Paco\Desktop\Pan_ARTDeco_ensGene\analisis_casero_de_expresion_diferencial\ARTDeco_Pan_cells_THZ1_unic_dogs.bed"
common_dogs = r"C:\Users\Paco\Desktop\Pan_ARTDeco_ensGene\analisis_casero_de_expresion_diferencial\ARTDeco_Pan_cells_TPLyTHZ1_unic_common_dogs.bed"

# Open the files and iterate through them
with open(dog_file1, "r") as file1, open(dog_file2, "r") as file2, open(common_dogs, "w") as common:
    
    # Save a DoGs file in a list
    dog2_data = [line.strip() for line in file2]

    # Save the IDs from one DoGs file
    for dog1 in file1:
        dog1_id = dog1.strip().split("\t")[3]

        # Iterate through the second file to find the IDs that match between files
        for dog2 in dog2_data:
            dog2_id = dog2.strip().split("\t")[3]

            if dog1_id == dog2_id:
                common.write(dog1) # Write the DoG that match in the two files
