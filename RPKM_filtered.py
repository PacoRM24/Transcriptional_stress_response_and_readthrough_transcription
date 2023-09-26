# This code will create a new RPKM file using the DoGs that has been filtered

rpkm_file = "RPKM_file.txt"
dogs_file = "ARTDeco_Total_dog_annotation.bed"
new_rpkm = "RPKM_file_af2.txt"

with open(dogs_file, "r") as dogs, open(rpkm_file, "r") as rpkms, open(new_rpkm, "w") as nrpkm:
    dogs_ids = []

    for dog in dogs:
        dog_id = dog.strip().split("\t")[3]
        dogs_ids.append(dog_id)

    nrpkm.write(rpkms.readline())
    for rpkm in rpkms:
        rpkm_id = rpkm.strip().split("\t")[0]
        if rpkm_id in dogs_ids:
            nrpkm.write(rpkm)
