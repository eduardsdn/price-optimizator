import json
import csv

catalog1 = {}
with open('Price_optimizator_M.video.json', 'r', encoding='utf-8') as f:
    data = json.loads(f.read())
    for item in data['M.video']['Games_Soft_&_Entertainment']['Games_for_PS4']:
        catalog1[item['name']] = item['price']


catalog2 = {}
with open('PSStore_sale.json', 'r', encoding='utf-8') as f:
    data = json.loads(f.read())
    for item in data['PlayStationStore']['Games']['PS4']:
        catalog2[item['name']] = item['price']


with open('Pricelist.txt', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    next(reader)
    content1 = {name: price for _, name, price in reader}

with open('Price_optimizator_M.video.json', 'r', encoding='utf-8') as f:
    data = json.loads(f.read())
    content2 = {}
for item in data['M.video']['Games_Soft_&_Entertainment']['Games_for_PS4']:
    content2[item['name']] = item['price']

with open('PSStore_sale.json', 'r', encoding='utf-8') as f:
    data = json.loads(f.read())
    content3 = {}
for item in data['PlayStationStore']['Games']['PS4']:
    content3[item['name']] = item['price']


print('-------------------------------------')
print(*set(content2) - set(content1), sep='\n')
print(*set(content3) - set(content1), sep='\n')    
print('-------------------------------------')


def average_of_2_sites(file_name1, file_name2):
    for name in catalog1:
        avg_price = int((catalog1[name] + catalog2[name]) / 2)
        print(f"Name: {name}   Average price: {avg_price}")


print(average_of_2_sites('Price_optimizator_M.video.json', 'PSStore_sale.json'))




