print('hello')
print("hello")
print("I don't know")
print('I don\'t know')
print('say "I don\'t know"')
print("say \"I don't know\"")

print('hello. \nHow are you?')
print(r'hello. \nHow are you?')
print(r'c:\name:\cname')

print("""
line1
line2
line3
""")

print("########")
print("""
line1
line2
line3
""")
print("########")

print("########")
print("""line1
line2
line3""")
print("########")

print("########")
print("""\
line1
line2
line3\
""")
print("########")

print('Hi.' * 3)
print('Hi.' * 3 + 'Mike.')

print('Hi.' + 'Mike.')
print('Hi.''Mike.')

s = 'aaaaaaaaaaaaa''bbbbbbb'
print(s)

s = ('aaaaaaaaaaaaa'
     'bbbbbbb')
print(s)

s = 'aaaaaaaaaaaaa'\
    'bbbbbbb'
print(s)

word = 'python'
print(word[0])
print(word[1])
print(word[-1])
print(word[0:2])
print(word[2:5])
print(word[:2])
print(word[2:])

word = 'j' + word[2:]
print(word)
print(word[:])

n = len(word)
print(n)
