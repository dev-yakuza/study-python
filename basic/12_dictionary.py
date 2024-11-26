d = {'x': 10, 'y': 20}
print(d)
print(type(d))
print(d['x'])
print(d['y'])
d['x'] = 100
print(d)
d['x'] = 'aaaaa'
print(d)
d['z'] = 200
print(d)
d[1] = 10000
print(d)

print('#################')

d = dict(a=10, b=20)
print(d)
d = dict([('a', 10), ('b', 20)])
print(d)