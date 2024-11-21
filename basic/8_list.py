l = [1, 20, 4, 50, 2, 1, 2]
print(l)
print(l[0])
print(l[1])
print(l[-1])
print(l[-2])
print(l[0:2])
print(l[:2])
print(l[2:5])
print(l[2:])
print(l[:])
print(len(l))
print(type(l))
print(list('abcdefg'))
# print(l(100)) # ERROR

print('##################')

n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(n[::2])
print(n[::-1])

print('##################')

a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
print(x)
print(x[0])
print(x[1])
print(x[0][1])
print(x[1][2])

print('##################')

s = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(s)
print(s[0])

s[0] = 'X'
print(s)

print(s[2:5])
s[2:5] = ['C', 'D', 'E']
print(s)
s[2:5] = []
print(s)
s[:] = []
print(s)

print('##################')

n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(n)
n.append(100)
print(n)
n.insert(0, 200)
print(n)
n.pop()
print(n)
n.pop(0)
print(n)
del n[0]
print(n)
del n
# print(n) # ERROR
n = [1, 2, 2, 2, 3]
n.remove(2)
print(n)
n.remove(2)
n.remove(2)
print(n)
# n.remove(2) # ERROR

print('##################')

a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 10]
print(a)
print(b)
x = a + b
print(x)
a += b
print(a)

a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 10]
x.extend(b)
print(x)

print('##################')

r = [1, 2, 3, 4, 5, 1, 2, 3]
print(r.index(3))
print(r.index(3, 3))
print(r.count(3))
if 5 in r:
    print('exist')
if 100 in r:
    print('exist')

r.sort()
print(r)
r.sort(reverse=True)
print(r)
r.reverse()
print(r)

s = 'My name is Deku'
to_split = s.split(' ')
print(to_split)
to_split = s.split('###')
print(to_split)

to_split = s.split(' ')
print(to_split)
x = ' ' .join(to_split)
print(x)
x = '###' .join(to_split)
print(x)

print(help(list))