# This code extracts the RPKMs from the DoGs corresponding to a DoG file from pancreatic cancer cells.

# Define the paths into variables
dogs_file = # Specify the path to the DoG file, which contains information about pancreatic cancer cells.
rpkms_file = # Specify the path to the RPKMs file obtained using RPKM.py.
new_rpkms_file = # Specify the name and path for the output RPKMs file.

# Open the DoG file, RPKMs file, and the new RPKMs file for reading and writing, respectively.
with open(dogs_file, "r") as dog_file, open(rpkms_file, "r") as rpkm_file, open(new_rpkms_file, "w") as new_rpkms:

    # Initialize an empty list to store DoG IDs.
    dogs_id = []
    
    # Iterate through each line in the DoG file.
    for dog in dog_file:
        # Extract the DoG ID from the fourth tab-separated field in the line.
        ids = dog.strip().split("\t")[3]
        id = ids.split("&")[0]
        # Add the extracted DoG ID to the list.
        dogs_id.append(id)

    # Write the header from the RPKMs file to the new RPKMs file.
    new_rpkms.write(rpkm_file.readline())
    
    # Iterate through each line in the RPKMs file.
    for rpkm in rpkm_file:
        # Extract the RPKM ID from the first tab-separated field in the line.
        rpkm_id = rpkm.strip().split("\t")[0]
        # Check if the RPKM ID exists in the list of DoG IDs.
        if rpkm_id in dogs_id:
            # If it exists, write the RPKM line to the new RPKMs file.
            new_rpkms.write(rpkm)
