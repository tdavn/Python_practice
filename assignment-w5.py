# 4.1 Pizzas
favorite_pizzas = ['Hot pepper pizza', 'Chicken pizza', 'Maze pizza']

for pizza in favorite_pizzas:
    print(f'{pizza} is one of my most favorite pizzas.')

print('These ' + str(len(favorite_pizzas)+1) + ' pizzas are so delicieous!')


# 4.2 Animals
pets = ['Hamster', 'Guinea pig', 'Persian cat']

for pet in pets:
    print(f'{pet} would be a great pet.')

print(f'All of them, {pets[0]}, {pets[1]} and {pets[2]} are really cute!')

# 4.3 Counting to twenty
for i in range(1, 21):
    print(i, end='\t')
    
# 4.4 Million
million = list(range(1, 1_000_001))
for number in million:
    print(number)
    
print('The smallest value:')
print(min(million))
print('The largest value:')
print(max(million))
print('Sum of an array from 1 to 1,000,000: ', sum(million))

# 4.6 Odd numbers 
odd_numbers = list(range(1, 20, 2))
print('Odd number in range of 20:')
for number in odd_numbers:
    print(number, end=' ')
    
# 4.13 Buffet
def menu_change(menu, old_items, new_items):
    '''Define menu changing method'''
    menu_list = list(menu)
    for k, v in enumerate(old_items):
        menu_list[menu_list.index(v)] = new_items[k]
    return tuple(menu_list)

menu = ('Salad', 'Chicken fry', 'Beef rib', 'Ice cream', 'Pizza', 'Egg soup')
print('The menu:')
counter = 1
for item in menu:
    print(f'Item {counter}: {item}')
    counter += 1

# Change 2nd and 4th items
old_formula = ['Chicken fry', 'Ice cream']
new_formula = ['Japanes ramen', 'Grape juice']
new_menu = menu_change(menu, old_formula, new_formula)

print('The new menu:')
counting = 1
for item in new_menu:
    print(f'Item {counting}: {item}')
    counting += 1

# 8.3 T-Shirt
def make_shirt(size, text):
    '''Making a T-shirt'''
    print(f'T-shirt size {size} with slogan {text.upper()}')

make_shirt('L', 'heal the world!')

# 8.4 Large Shirts
def make_shirt(size='L', text='I love Python!'):
    '''Making a T-shirt'''
    print(f'T-shirt size {size} with slogan {text.upper()}')

make_shirt()
make_shirt('M')
make_shirt('S', 'I love you more!')

# 8.5 Cities
def describe_city(city_name, country='Canada'):
    print(f'{city_name} city is in {country}')

describe_city('Toronto')
describe_city('Montreal')
describe_city('Chicago', 'USA')

# 8.6 City Name
