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
