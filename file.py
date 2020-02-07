cook_book ={}
ingredient_book = {}
len_count = 0
with open('recipes.txt', encoding='utf8') as f:
    while True:
        dish_name = f.readline().strip()
        if not dish_name:
            break
        if dish_name not in cook_book.keys():
            cook_book[dish_name] = list()
        ingredient_count = int(f.readline().strip())
        while ingredient_count > 0:
            ingredient = f.readline().strip().split(' | ')
            ingredient_book['ingredient_name'] = ingredient[0]
            ingredient_book['quantity'] = int(ingredient[1])
            ingredient_book['measure'] = ingredient[2]
            cook_book[dish_name].append(ingredient_book)
            ingredient_count -= 1
            ingredient_book = {}
        f.readline()

def ingredients_dict(dishes, ingredient_book):
    for i in cook_book[dishes]:
        if i['ingredient_name'] in ingredient_book.keys():
            new_quantity = ingredient_book[i['ingredient_name']]['quantity'] + i['quantity']
            ingredient_book[i['ingredient_name']] = {'quantity': new_quantity, 'measure': i['measure']}
        else:
            ingredient_book[i['ingredient_name']] = {'quantity': i['quantity'], 'measure': i['measure']}
    return ingredient_book

def get_shop_list_by_dishes(dishes, person_count):
    ingredient_book = {}
    if isinstance(dishes, str):
        ingredients_dict(dishes, ingredient_book)
    else:
        for dish in dishes:
            ingredients_dict(dish, ingredient_book)
    for keys, values in ingredient_book.items():
           values['quantity'] = int(values['quantity'])*person_count
    print('Необходимые продукты:\n')
    for keys, values in ingredient_book.items():
        print(f'{keys}: ', end = '')
        for v in values.values():
            print(f'{v}', end = ' ')
        print()
get_shop_list_by_dishes(['Запеченный картофель','Омлет', 'Фахитос'], 2)








