# This code will extract the unic DoGs from a file

dog_file1 = r"C:\Users\Paco\Desktop\Pan_ARTDeco_ensGene\analisis_casero_de_expresion_diferencial\ARTDeco_Pan_cells_DMSO_common_dogs.bed"
dog_file2 = r"C:\Users\Paco\Desktop\Pan_ARTDeco_ensGene\analisis_casero_de_expresion_diferencial\ARTDeco_Pan_cells_TPL_common_dogs.bed"
dog_file3 = r"C:\Users\Paco\Desktop\Pan_ARTDeco_ensGene\analisis_casero_de_expresion_diferencial\ARTDeco_Pan_cells_THZ1_common_dogs.bed"
unic_dogs = r"C:\Users\Paco\Desktop\Pan_ARTDeco_ensGene\analisis_casero_de_expresion_diferencial\ARTDeco_Pan_cells_DMSO_unic_dogs.bed"

with open(dog_file1, "r") as file1, open(dog_file2, "r") as file2, open(dog_file3, "r") as file3, open(unic_dogs, "w") as unic:
    dog2_data = [line.strip() for line in file2]
    dog3_data = [line2.strip() for line2 in file3]
    c = 0
    for dog1 in file1:
        dog1_id = dog1.strip().split("\t")[3]

        for dog2 in dog2_data:
            dog2_id = dog2.strip().split("\t")[3]

            if dog1_id == dog2_id:
                c += 1
        for dog3 in dog3_data:
            dog3_id = dog3.strip().split("\t")[3]

            if dog1_id == dog3_id:
                c += 1
        if c == 0:
            unic.write(dog1)
        c = 0
