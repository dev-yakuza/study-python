word ='python'
print(word[0])
print(word[1])
print(word[-1])
print(word[0:2])
print(word[2:5])
print('#################')
print(word[0:2])
print(word[:2])
print('#################')
print(word[2:])
# print(word[100]) # Error
print('#################')
# Error
# word[0] = 'j'
# print(word)
word = 'j' + word[1:]
print(word)
print('#################')
print(word[:])

n = len(word)
print(n)