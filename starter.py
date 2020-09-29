#creating the shop
shop = [(x, y) for i in range(20) for x in ['shirt', 'scarf', 'glove', 'hat'] for y in ['S', 'M', 'L', 'XL', 'XXL'] if x != y]
shop.append(['SHIRT', 's'])
print(shop)
print('Total no of articles in the shop is =  ' + str(len(shop)))

# remove last added item ['SHIRT', 's']
shop.pop()
print(shop)
print(' after deleting last element - the size is: ' + str(len(shop)))

# able to remove any item
shop.remove(('scarf', 'M'))
print(' size is: ' + str(len(shop)))

# restock
shop.append(('dress', 'S'))
print('Last item added : ' + str(shop[len(shop)-1]))
print('Articles in the shop after restock = ' + str(len(shop)))

