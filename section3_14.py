word = 'a is {}'.format('a')
print(word)
word = 'a is {}'.format('test')
print(word)

word = 'a is {} {} {}'.format(1, 2, 3)
print(word)
word = 'a is {0} {1} {2}'.format(1, 2, 3)
print(word)
word = 'a is {2} {1} {0}'.format(1, 2, 3)
print(word)
word = 'a is {1} {0} {2}'.format(1, 2, 3)
print(word)
word = 'My name is {0} {1}. Watashi ha {1} {0}'.format('okada', 'daisaku')
print(word)
word = 'My name is {name} {family}. Watashi ha {family} {name}'.format(name = 'okada', family = 'daisaku')
print(word)

num=1
print(num)
print(str(num))
print(type(str(num)))
print(str(3.14))
print(str(True))

print('###### Python 3.6よりformatではなく、f-strings ######')

a = 'a'
print(f'a is {a}')

x, y, z = 1, 2, 3
print(f'a is {x}, {y}, {z}')
print(f'a is {z}, {y}, {x}')

name = 'Jun'
family = 'Sakai'
print(f'My name is {name} {family}. Watashi ha {family} {name}')

