# comment
"""
comment
"""

s = 'aaaaaaaaaa' + 'bbbbbbbbb'
print(s)

s = 'aaaaaaaaaa' \
    + 'bbbbbbbbb'
print(s)

s = ('aaaaaaaaaa'
    + 'bbbbbbbbb')
print(s)

x = 1 + 1 + 1 + 1 + 1 + 1 \
    + 1 + 1 + 1 + 1 + 1 + 1
print(x)

x = (1 + 1 + 1 + 1 + 1 + 1
    + 1 + 1 + 1 + 1 + 1 + 1)
print(x)

x = 10
if x < 0:
    print('negative')
elif x == 0:
    print('zero')
else:
    print('positive')

a = 5
b = 10

if a > 0:
    print('positive')
    if b > 0:
        print('b is positive')

a = 1
b = 2

# 等しい
print(a == b)
# 異なる
print(a != b)
# aがbより小さい
print(a < b)
# aがbより大きい
print(a > b)
# aがb以下
print(a <= b)
# aがb以上
print(a >= b)
# aもbも真であれば真
print(a > 0 and b > 0)
# aまたはbが真であれば真
print(a > 0 or b > 0)

y = [1, 2, 3]
x = 1

if x in y:
    print('in')

if 100 not in y:
    print('not in')

a = 1
b = 2

if not a == b:
    print('aとbは等しくなし')
if a != b:
    print('aとbは等しくなし')

is_ok = True
if not is_ok:
    print('hello')
is_ok = False
if not is_ok:
    print('hello')

is_ok = True
if is_ok:
    print('ok')
else:
    print('no')
is_ok = 0
if is_ok:
    print('ok')
else:
    print('no')
is_ok = 1
if is_ok:
    print('ok')
else:
    print('no')
is_ok = 10001010
if is_ok:
    print('ok')
else:
    print('no')
is_ok = ''
if is_ok:
    print('ok')
else:
    print('no')
is_ok = 'aaaaa'
if is_ok:
    print('ok')
else:
    print('no')
is_ok = []
if is_ok:
    print('ok')
else:
    print('no')
is_ok = [1, 2, 3]
if is_ok:
    print('ok')
else:
    print('no')
is_ok = [1, 2, 3]
if len(is_ok) > 0:
    print('ok')
else:
    print('no')

is_empty = None
print(help(None))
print(type(None))

if is_empty is None:
    print('None')

if is_empty == None:
    print('None')

if is_empty is not None:
    print('None')
else:
    print('not None')


count = 0
while count < 5:
    print(count)
    count += 1

count = 0
while True:
    if count >= 5:
        break
    if count == 2:
        count += 1
        continue
    print(count)
    count += 1

count = 0
while count < 5:
    print(count)
    count += 1
else:
    print('done')

count = 0
while count < 5:
    if count == 1:
        break
    print(count)
    count += 1
else:
    # breakの場合は出力されない。breakはwhile全てから抜ける
    print('done')

# while True:
#     word = input('Enter:')
#     if word == 'ok':
#         break
#     print('next')
# while True:
#     word = input('Enter:')
#     word = int(word)
#     if word == 100:
#         break
#     print('next')

same_list = [1, 2, 3, 4, 5]

i = 0
while i < len(same_list):
    print(same_list[i])
    i += 1

for i in same_list:
    print(i)

for s in 'abcde':
    print(s)

for word in ['My', 'Name', 'is', 'Mike']:
    if word == 'Name':
        break
    print(word)

for word in ['My', 'Name', 'is', 'Mike']:
    if word == 'Name':
        continue
    print(word)

for word in ['My', 'Name', 'is', 'Mike']:
    print(word)
else:
    print('Done')
for word in ['My', 'Name', 'is', 'Mike']:
    if word == 'Name':
        break
    print(word)
else:
    print('Done')
for word in ['My', 'Name', 'is', 'Mike']:
    if word == 'Name':
        continue
    print(word)
else:
    print('Done')

# num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for i in num_list:
#     print(i)

for i in range(10):
    print(i)

for i in range(2, 10):
    print(i)

for i in range(2, 10, 3):
    print(i)

for _ in range(10):
    print('hello')

for fruit in ['apple', 'banana', 'orange']:
    print(fruit)

for i, fruit in enumerate(['apple', 'banana', 'orange']):
    print(i, fruit)

days = ['Mon', 'Tue', 'Wed']
fruits = ['apple', 'banana', 'orange']
drinks = ['coffee', 'tea', 'beer']

for i in range(len(days)):
    print(days[i], fruits[i], drinks[i])

for day, fruit, drink in zip(days, fruits, drinks):
    print(day, fruit, drink)

d = {'x': 100, 'y': 200}
for v in d:
    print(v)

print(d.items())
for k, v in d.items():
    print(k, v)

def say_something():
    print('hi')
    s = 'hi'
    return s
say_something()
print(type(say_something))
f = say_something
f()
result = say_something()
print(result)

def what_is_this(color):
    print(color)
what_is_this('white')

def what_is_this(color):
    if color == 'red':
        return 'tomato'
    elif color == 'green':
        return 'green pepper'
    else:
        return 'I dont know'
result = what_is_this('red')
print(result)

def add_num(a: int, b: int) -> int:
    return a + b
result = add_num(10, 20)
print(result)
result = add_num('a', 'b')
print(result)

def menu(entree):
    print(entree)
menu('beef')

def menu(entree, drink, dessert):
    print(entree)
    print(drink)
    print(dessert)

menu('beef', 'beer', 'ice')
menu(entree='beef', drink='beer', dessert='ice')
menu('beef', drink='beer', dessert='ice')

def menu(entree='beef', drink='wine', dessert='ice'):
    print(entree)
    print(drink)
    print(dessert)
menu()
menu(entree='chicken', dessert='cake')
menu('chicken', dessert='cake')

def test_func(x, l=[]):
    l.append(x)
    return l

y = [1, 2, 3]
r = test_func(100, y)
print(r)

y = [1, 2, 3]
r = test_func(200, y)
print(r)

r = test_func(100)
print(r)

r = test_func(100)
print(r)

def test_func(x, l=None):
    if l is None:
        l = []
    l.append(x)
    return l
r = test_func(100)
print(r)

r = test_func(100)
print(r)

def say_something(*args):
    print(args)
    for arg in args:
        print(arg)
say_something('aaa', 'bbbb', 'cccc')

def say_something(word, *args):
    print(word)
    for arg in args:
        print(arg)
say_something('aaa', 'arg', 'arg')
t = ('Mike', 'Nancy')
say_something('aaa', *t)
say_something('aaa', *('Mike', 'Nancy'))

def menu(**kwargs):
    print(kwargs)
menu(entree='beef', drink='coffee')

def menu(**kwargs):
    for k, v in kwargs.items():
        print(k, v)
d = {
    'entree': 'beef',
    'drink': 'ice coffe',
    'dessert': 'ice'
}
menu(**d)

def menu(food, *args, **kwargs):
    print(food)
    print(args)
    print(kwargs)

menu('banana', 'apple', 'orange', entree='beef', drink='coffe')

def outer(a, b):
    def plus(c, b):
        return c + b
    r1 = plus(a, b)
    r2 = plus(b, a)
    return r1 + r2
print(outer(1, 2))

def outer(a, b):
    def inner():
        return a + b
    return inner

f = outer(3, 3)
print(f)
print(f())

def circle_area_func(pi):
    def circle_area(radius):
        return pi * radius * radius
    return circle_area

cal1 = circle_area_func(3.14)
cal2 = circle_area_func(3.141592)

print(cal1(10))
print(cal2(10))

def print_inf(func):
    def wrapper(*args, **kwargs):
        print('start')
        result = func(*args, **kwargs)
        print('end')
        return result
    return wrapper

def add_num(a, b):
    return a + b

f = print_inf(add_num)
r = f(10, 20)
print(r)

def print_more(func):
    def wrapper(*args, **kwargs):
        print('func:', func.__name__)
        print('args:', args)
        print('kwargs:', kwargs)
        result = func(*args, **kwargs)
        print('result:', result)
        return result
    return wrapper

def print_info(func):
    def wrapper(*args, **kwargs):
        print('start')
        result = func(*args, **kwargs)
        print('end')
        return result
    return wrapper

@print_info
@print_more
def add_num(a, b):
    return a + b

r = add_num(10, 20)
print(r)

l = ['Mon', 'tue', 'Wed', 'Thu', 'fri', 'sat', 'Sun']
def change_words(words, func):
    for word in words:
        print(func(word))

def sample_func(word):
    return word.capitalize()

change_words(l, sample_func)


def change_words(words, func):
    for word in words:
        print(func(word))

sample_func = lambda word:word.capitalize()
# def sample_func(word):
#     return word.capitalize()

change_words(l, sample_func)
change_words(l, lambda word:word.capitalize())
change_words(l, lambda word:word.lower())

l = ['Good morning', 'Goog afternoon', 'Good night']

for i in l:
    print(i)

def greeting():
    yield 'Good morning'
    yield 'Goog afternoon'
    yield 'Good night'

for i in greeting():
    print(i)

g = greeting()
print(next(g))
print(next(g))

def counter(num=1):
    for _ in range(num):
        yield 'run'

c = counter()

print(next(c))

t = (1, 2, 3, 4)

r = []
for i in t:
    if i % 2 == 0:
        r.append(i)
print(r)

r = []
r = [i for i in t if i % 2 == 0]
print(r)

t2 = (5, 6, 7, 8)
r = []
for i in t:
    for j in t2:
        r.append(i * j)
print(r)

r = [i * j for i in t for j in t2]
print(r)

w = ['1', '2', '3']
f = ['4', '5', '6']

d = {}
for x, y in zip(w, f):
    d[x] = y

print(d)

d = {x: y for x, y in zip(w, f)}
print(d)

s = set()

for i in range(10):
    if i % 2 == 0:
        s.add(i)
print(s)

s = {i for i in range(10) if i % 2 == 0}
print(s)

def g():
    for i in range(10):
        yield i
g = g()

g = {i for i in range(10) if i % 2 == 0}

for x in g:
    print(x)
