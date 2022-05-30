

from turtle import color


demo_List = [1, 'Hola Mundo', 1.43, False, [1,2,3]]
colors = ['res', 'blue', 'blue']
number_list = list({1,2,3,4,5})

# a way to return number from 1 to 10 or how u want
ok = list(range(1,10))


# a way to change a value of a List
colors[1] = 'Elvis'
#print(colors)

# Array or List methods

# Add a new value in an Array at the final
colors.append('violet')
#print(colors)

# Add a new value at the beginning of the Array 
colors.insert(0, 'Magali')
#print(colors)

# Remove last  element
colors.pop()
print(colors)

# We can eliminate basing of one index using the pop method
colors.pop(1)

#Delete all the elements of an Array
# colors.clear()

# Sort an array by abcdefg alphabetic
colors.sort()
print(colors)