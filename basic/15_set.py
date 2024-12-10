a = {1, 2, 2, 3, 4, 4, 4, 5, 6}
print(a)
print(type(a))
b = {2, 3, 3, 6, 7}
print(b)

print(a - b)
print(b - a)
# print(a + b) # ERROR
print(a & b)
print(a | b)
print(a ^ b)

print("####################")

s = {1, 2, 3, 4, 5}
print(s)
# print(s[0]) # ERROR
s.add(6)
print(s)
s.add(6)
print(s)

s.remove(6)
print(s)
s.clear()
print(s)

a = {}
print(type(a))
print(a)

# help(set)