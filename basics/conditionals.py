
x = 40
y = 100

if x < 30:
    print("x is less than 30")
else:
    print('x is greater than 30')

#

name = 'Elvis'
lastName = 'Garcia'

if name == 'Elvis':
    print('The Name is Elvis')
    if lastName == 'Garrcia':
        print(' Your name and your lastname are cool')
    else:
        print('idk')
else:
    print('The name is Wrong')


#  Logic Operators && || but here: and, or, not
if x < 60 and x > 30:
    print('Esta estabilizado')
else:
    print('No esta estabilizado')

if x < 100 or x > 20:
    print('Funciona')

if not(x == y):
    print('are not the same')