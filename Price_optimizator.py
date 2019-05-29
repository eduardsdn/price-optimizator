def read_data_store(file_path): #reads pricelist.txt
    data = []
    with open(file_path, "r") as f:
        f.readline()
        for line in f:
            parts = line.split(",")
            row = [parts[0], parts[1],int(parts[2])]

            data.append(row)

    return data

pricelist = read_data_store("Price_optimizator.txt") #matrix with pricelist
