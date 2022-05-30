from tkinter import N


foods = ['apple', 'bread', 'cheese', 'milk']
count = 4
# This Works
for food in foods:
    if food == 'cheese':
        print(f'you need to buy this {food}')
    else:
        print(food)

# While

while count <= 10:
    print(count)
    count += 1
    
