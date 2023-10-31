# This code will extract Gene Symbols from the DAVID gene ID conversion tool
# and compare them with the DoG-producing genes from osmotic stress

# Define the paths to the conversion table and the file containing upregulated genes.
conversion_table = # Write the path to the conversion table given by DAVIDs conversion tool
osmotic_file = # Write the path to the list of DoG-producing genes from osmotic stress

# Open the conversion table and osmotic genes file for reading
with open(conversion_table, "r") as dogs, open(osmotic_file, "r") as osmotic:

    # Initialize an empty list to store Gene Symbols from the conversion table
    dogs_names = []

    # Skip the first line in the conversion table
    dogs.readline()

    # Extract Gene Symbols from the conversion table and store them in dogs_names list
    for dog in dogs:
        dog_name = dog.strip().split("\t")[1]
        dogs_names.append(dog_name)

    # Initialize a counter variable to keep track of matching genes
    c = 0

    # Compare genes from the osmotic genes file with those in dogs_names
    for gene in osmotic:
        gene = gene.strip()
        if gene in dogs_names:
            c += 1

    # Print the count of matching genes.
    print(c)
