

dogs_file = r"C:\Users\Paco\Desktop\Pan_ARTDeco_ensGene\analisis_casero_de_expresion_diferencial\ARTDeco_Pan_cells_THZ1yDMSO_union_dogs.bed"
rpkms_file = r"C:\Users\Paco\Desktop\Pan_ARTDeco_ensGene\analisis_casero_de_expresion_diferencial\RPKM_file.txt"
new_rpkms_file = r"C:\Users\Paco\Desktop\Pan_ARTDeco_ensGene\analisis_casero_de_expresion_diferencial\RPKM_THZ1yDMSO.txt"

with open(dogs_file, "r") as dog_file, open(rpkms_file, "r") as rpkm_file, open(new_rpkms_file, "w") as new_rpkms:

    dogs_id = []
    for dog in dog_file:
        ids = dog.strip().split("\t")[3]
        id = ids.split("&")[0]
        dogs_id.append(id)

    new_rpkms.write(rpkm_file.readline())
    for rpkm in rpkm_file:
        rpkm_id = rpkm.strip().split("\t")[0]
        if rpkm_id in dogs_id:
            new_rpkms.write(rpkm)
