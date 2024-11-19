print('a is {}'.format('a'))
print('a is {}'.format('test'))
print('a is {} {} {}'.format(1, 2, 3))
print('a is {0} {1} {2}'.format(1, 2, 3))
print('a is {2} {1} {0}'.format(1, 2, 3))
print('My name is {name} {family}'.format(name='Deku', family='Dev'))

print('##################')

# f-string
a = 'a'
print(f'a is {a}')
x, y, z = 1, 2, 3
print(f'a is {x} {y} {z}')
name = 'Deku'
family = 'Dev'
print(f'My name is {name} {family}')

print('##################')

print(1)
print('1')
print(str(1))
print(str(3.14))
print(str(True))