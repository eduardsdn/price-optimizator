.read().split('\n')

catalog3 = {}
def read_data_store(file_name): #reads pricelist.txt
    data = []
    with open(file_name, 'r', encoding='utf-8') as f:
        for line in f.read().split('\n'):
            parts = line.split(",")
            catalog3[parts[1]] = int(parts[3])

    return parts

pricelist = read_data_store("Pricelist.txt") #matrix with pricelist
print(pricelist)


codeforces