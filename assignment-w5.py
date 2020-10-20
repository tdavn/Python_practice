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
    for items in old_items:
        menu_list[menu_list.index(old_val)] = new_val
    return tuple(menu_list)
menu = ('Salad', 'Chicken fry', 'Beef rib', 'Ice cream', 'Pizza', 'Egg soup')
new_menu = menu_change(menu, 'Beef rib', 'Lamb rib')
print(new_menu)