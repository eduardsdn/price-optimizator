import json

catalog1 = {}
with open('Price_optimizator_M.video.json', 'r', encoding='utf-8') as f:
    data = json.loads(f.read())
    for item in data['M.video']['Games_Soft_&_Entertainment']['Games_for_PS4']:
        catalog1[item['name']] = item['price']


print(f"Sales of PS4 games in M.video: {catalog1}")


catalog2 = {}
with open('PSStore_sale.json', 'r', encoding='utf-8') as f:
    data = json.loads(f.read())
    for item in data['PlayStationStore']['Games']['PS4']:
        catalog2[item['name']] = item['price']


print(f"Sales of PS4 games in PS Store: {catalog2}")
