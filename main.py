from pprint import pprint

def get_dict(file_name):

    dish_keys = ('ingredient_name', 'quantity', 'measure')
    stack = []
    number_ingr = 0
    cook_book ={}

    with open (file_name, encoding='utf8') as recipes_file:
    
        for line in recipes_file:

            if line == '\n':
              continue
            
            stack.append(line.strip('\n'))

            if line.strip('\n').isdigit():
                number_ingr = int(stack.pop())
                dish_name = stack.pop()
                
            if len(stack) == number_ingr:
                dish_list = []

                for ingredients in stack:
                    dish = dict(i for i in list(zip(dish_keys, map(lambda x: x.strip(), ingredients.split('|')))))
                    dish_list.append(dish)
                    
                stack.clear()

                cook_book[dish_name] = dish_list

    return cook_book

def get_shop_list_by_dishes(dish_list, person_count):
    
    cook_book = get_dict('recipes.txt')

    shop_list = {}

    for dish in dish_list:
        try:
            for ingredients in cook_book[dish]:            
                if list(ingredients.items())[0][1] in shop_list.keys():
                    repeat_quant = shop_list.pop(list(ingredients.items())[0][1])['quantity']
            
                    ingredient = (int(list(ingredients.items())[1][1]) * person_count) + repeat_quant, list(ingredients.items())[2][1]
                else:
                    ingredient = int(list(ingredients.items())[1][1]) * person_count, list(ingredients.items())[2][1]

                shop_list[list(ingredients.items())[0][1]] = dict(list(zip(('quantity', 'measure'), ingredient)))

        except KeyError:
            print(f'Блюдо {dish} отсутствует в книге рецептов')

    return shop_list

dish_list = ['Яичница-глазунья', 'Омлет', 'Фахитос'] 
person_count = 3

#Задача №1
#pprint(get_dict('recipes.txt'))

#Задача №2
shop_list = get_shop_list_by_dishes(dish_list, person_count)
pprint(shop_list)       


        


