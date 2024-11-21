i = [1, 2, 3, 4, 5]
j = i
print('i =', i)
print('j =', j)

j[0] = 100
print('i =', i)
print('j =', j)

x = [1, 2, 3, 4, 5]
y = x.copy()
print('x =', x)
print('y =', y)
x[0] = 100
print('x =', x)
print('y =', y)

x = [1, 2, 3, 4, 5]
y = x[:]
print('x =', x)
print('y =', y)
x[0] = 100
print('x =', x)
print('y =', y)

print('##################')

x = 20
y = x
y = 5
print(x)
print(y)
print(id(x))
print(id(y))

x = ['a', 'b']
y = x
y[0] = 'p'
print(x)
print(y)
print(id(x))
print(id(y))