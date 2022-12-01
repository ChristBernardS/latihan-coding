# x = int(input('Masukan angka:'))
# for i in range(0,10):
#     print(x)
#     x += 1

menu = {
    'Main Dish':['Crispy Fried Oysters With Cornmeal Batter','Steamed Mussels in White Wine','French Pork Rillettes','Shrimp Ceviche','Beef Wellington'],
    'Side Dish':['Crab Cakes','Cheese and Leek Souffle','Truffled French Fries','Lobster Macaroni and Cheese Casserole'],
    'Desert'   :['Milk Shake','Juice','Dark Chocolate Molten Lava Cake','Lemon Crème Brûlée','Easy Caramel Flan','Apple Galette','Baked Alaska'],
    'Beverage' :['Root Beer','Champagne Cocktail','Vesper Martini','Negroni Cocktail','Paloma Cocktail','The Classic Whiskey Manhattan With Variations']
}
for key, value in menu.items():
    print(f'{key} : {value}')
print('')
milih_maindish = str(input('Pilih Menu Main Dish: '))
milih_sidedish = str(input('Pilih Menu Side Dish: '))
milih_desert = str(input('Pilih Menu Desert: '))
milih_beverage = str(input('Pilih Menu Beverage: '))
if milih_maindish in 'Main Dish' and milih_sidedish in 'Side Dish' and milih_desert in 'Desert' and milih_beverage in 'Beverage':
    print(milih_maindish+',',milih_sidedish+',',milih_desert+' dan',milih_beverage,'Akan disajikan segera, mohon tunggu sebentar')
else:
    print('Pilihan anda tidak terdaftar di dalam menu kami')