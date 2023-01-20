with open('recipes.txt', 'rt', encoding='utf-8') as file:
    cook_book = {}
    for line in file:
        dish_name = line.strip()
        ingredient_count = int(file.readline())
        ingredients = []
        for i in range(ingredient_count):
            ing = file.readline().strip()
            ingredient_name, quantity, measure = ing.split(' | ')
            ingredients.append({
                'ingredient_name': ingredient_name,
                'quantity': quantity,
                'measure': measure
            })
        file.readline()
        cook_book[dish_name] = ingredients

def get_shop_list_by_dishes(dishes, person_count):
    dict_by_dishes = {}
    for dish in dishes:
        if dish in cook_book:
            for ingr in cook_book[dish]:
                ingr["quantity"] *= person_count
                happy_dict = ingr.pop('ingredient_name')
                dict_by_dishes[happy_dict] = ingr
    return dict_by_dishes

res = get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
print(res)