shop = [(x, y) for i in range(100) for x in ['shirt', 'scarf', 'glove', 'hat'] for y in ['S', 'M', 'L', 'XL', 'XXL']]
shop.append(['SHIRT', 's'])
print(shop)
print('Total no of articles in the shop is =  ' + str(len(shop)))
shop.pop()
print(shop)
print(' after deleting last element - the size is: ' + str(len(shop)))

shop.clear()
# restock

shop = [(x, y) for i in range(200) for x in ['dress', 'pyjamas', 'skirt'] for y in ['S', 'M', 'L']]
print(shop)
print('Articles in the shop after restock = ' + str(len(shop)))

