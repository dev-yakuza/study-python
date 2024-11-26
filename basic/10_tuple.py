t = (1, 2, 3, 4, 1, 2)
print(type(t))
# t[0] = 100 # ERROR
print(t[0])
print(t[-1])
print(t[2:5])
print(t)
print(t.index(1))
print(t.index(1, 1))
print(t.count(1))
print(help(tuple))

print('##################')

t = ([1, 2, 3], [4, 5, 6])
# t[0] = [1] # ERROR
print(t[0][0])
t[0][0] = 100
print(t)

print('##################')

t = 1, 2, 3
print(t)
print(type(t))

t = 1,
print(type(t))

t = 1
print(type(t))
t = ()
print(type(t))
t = (1)
print(type(t))
t = ('test')
print(type(t))
t = ('test',)
print(type(t))

print('##################')
t = (1, 2, 3) + (4, 5, 6)
print(t)
# t = (1) + (2, 3, 4) # ERROR
t = (1,) + (2, 3, 4)
print(t)
