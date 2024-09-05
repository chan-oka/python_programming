l = [1, 20, 4, 50, 2, 1, 2]
print(l)
print(l[0])
print(l[1])
print(l[-1])
print(l[-2])
print(len(l))
print(type(l))
print(list('abcdf'))

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(l[::2])
print(l[::-1])

a = ['a', 'b', 'c']
b = [1, 2, 3]
x = [a, b]
print(x)
print(x[0])
print(x[0][0])
print(x[1][0])

s = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(s)
print(s[0])
s[0] = 'x'
print(s[0])
print(s[2:5])
s[2:5] = ['C', 'D', 'E']
print(s[2:5])
s[2:5] = []
print(s)
print(s[:])
s[:] = []
print(s)

n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(n)
n.append(100)
print(n)
n.insert(0, 200)
print(n)
n.insert(1, 300)
print(n)

print(n.pop(0))
print(n.pop(1))

print(n)
del n[0]
print(n)

n.remove(2)
print(n)

a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 10]
x = a + b
print(x)

a += b
print(a)

a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 10]
a.extend(b)
print(a)

r = [1, 2, 3, 4, 5, 1, 2, 3]
print(r)
print(r.index(3))
print(r.index(3, 3))
print(r.count(5))

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

s = 'My name is Mike.'
to_split = s.split('!!!')
print(to_split)
to_split = s.split(' ')
print(to_split)

x = ' '.join(to_split)
print(x)
x = '####'.join(to_split)
print(x)

print(help(list))

i = [1, 2, 3, 4, 5]
j = i
j[0] = 100
print('j = ', j)
print('i = ', i)

x = [1, 2, 3, 4, 5]
y = x.copy()
z = x[:]
y[0] = 100
z[1] = 200
print('x = ', x)
print('y = ', y)
print('z = ', z)

x = 20
y = x
y = 5
print(x)
print(y)
print(id(x))
print(id(y))

x = [1, 2, 3, 4, 5]
y = x
y[0] = 100
print('x = ', x)
print('y = ', y)
print(id(x))
print(id(y))


seat = []
min = 0
max = 5
print(min <= len(seat) < max)

t = (1, 2, 3, 4, 5)
print(t)
print(type(t))
print(t[0])
print(t[-1])
print(t[2:5])
print(t.index(1))
print(t.index(5, 2))
print(t.count(1))

t = ([1, 2, 3], [4, 5, 6])
print(t)
t[0][0] = 100
print(t)

t = 1, 2, 3, 4, 5
print(t)
print(type(t))

t = 1,
print(t)
print(type(t))

t = 1,000
print(t)
print(type(t))

t = ()
print(t)
print(type(t))

t = (1)
print(t)
print(type(t))

t = ('test')
print(t)
print(type(t))

t = ('test',)
print(t)
print(type(t))

t = (1, 2, 3, 4, 5) + (1, 2, 3, 4, 5)
print(t)
t = (1,) + (1, 2, 3, 4, 5)
print(t)

num_tuple = (10, 20)
print(num_tuple)

x, y = num_tuple
print(x, y)

x, y = (10, 20)
print(x, y)

x, y = 10, 20
print(x, y)

i = 10
j = 20
tmp = i
i = j
j = tmp
print('#####')
print(i, j)
print('#####')

a = 100
b = 200
print(a, b)
a, b = b, a
print(a, b)

chose_from_two = ('A', 'B', 'C')
answer = []
answer.append('A')
answer.append('C')
print(answer)

d = {'x': 10, 'y': 30}
print(d)
print(type(d))
print(d['x'])
print(d['y'])
d['x'] = 100
print(d)
d['x'] = 'test'
print(d)
d['z'] = 200
print(d)
d[1] = 200
print(d)

zzz = dict(a=100, b=200)
print(zzz)

zzz = dict([('a', 10), ('b', 20)])
print(zzz)

d = {'x': 20, 'y': 30}
print(d.keys())
print(d.values())

d2 = {'x': 1000, 'j': 500}
d.update(d2)
print(d)

print(d.get('x'))
print(d.get('z'))
print(type(d.get('z')))

print('x' in d2)
print('zz' in d2)

x = {'a': 1}
y = x
y['a'] = 1000
print(x)
print(y)

x = {'a': 1}
y = x.copy()
y['a'] = 1000
print(x)
print(y)

fruits = {
    'apple': 100,
    'banana': 200,
    'orange': 300
}
print(fruits['apple'])

a = {1, 1, 2, 2, 3, 4, 4, 4, 5, 6}
print(a)

b = {2, 3, 3, 6, 7}
print(b)

print(a - b)
print(b - a)
print(a & b)
print(a | b)
print(a ^ b)

s = {1, 2, 3, 4, 5}
s.add(6)
print(s)

s = {1, 2, 3, 4, 5}
s.add(6)
print(s)

s.remove(6)
print(s)
s.clear()
print(s)

my_friends = {'A', 'C', 'D'}
a_friends = {'B', 'D', 'E', 'F'}
print(my_friends & a_friends)

f = {'apple', 'banana', 'apple', 'banana'}
kind = set(f)
print(f)
print(kind)
print(type(f))
print(type(kind))
