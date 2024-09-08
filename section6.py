import sys

'''
コマンド：python3 section6.py aaaaa vbvvvv                                                                 (git)-[main]
出力：['section6.py', 'aaaaa', 'vbvvvv']
'''
print(sys.argv)

import lesson_package.tools.utils
from lesson_package.tools import utils, utils as u
from lesson_package.tools.utils import say_twice

r = lesson_package.tools.utils.say_twice('hello')
t = utils.say_twice('smile')
w = say_twice('smile2')
j = u.say_twice('smile3')
print(r)
print(t)
print(w)
print(j)

# from lesson_package.talk import human
# from lesson_package.talk import animal
from lesson_package.talk import *
print(human.sing())
print(human.cry())
print(animal.sing())
print(animal.cry())

try:
    from lesson_package import utils
except ImportError as ext:
    from lesson_package.tools import utils

print(utils.say_twice('ninu'))

print(globals())

import builtins
builtins.print('builtins')

ranking = {
    'a': 100,
    'b': 85,
    'c': 95
}
# 100 = ranking.get('a')
print(sorted(ranking, key=ranking.get, reverse=True))


s = "aoijhouhushiudhaudahdoahojdsojpcjpcaokca"

d = {}
for c in s:
    if c not in d:
        d[c] = 0
    d[c] += 1
print(d)

d = {}
for c in s:
    d.setdefault(c, 0)
    d[c] += 1

print(d)

from collections import defaultdict
d = defaultdict(int)
for c in s:
    d[c] += 1

print(d)

from termcolor import colored

print(colored('test', 'red'))
print(colored('test', 'red'))

# import collections, os, sys 複数のimportをしない
# importはアルファベット順
import collections
import os
import sys

# 標準ライブラリとサードパーティは空白行を一個入れて分ける
import termcolor

# 自分達のライブラリ
import lesson_package

# ローカルファイル
import config

# import順 標準→サードパーティ→自分達のライブラリ→ローカルファイル、各アルファベット順に並べる

print(collections.__file__)
print(termcolor.__file__)
print(lesson_package.__file__)
print(config.__file__)

print(sys.path)

import config

print("section6:", __name__)

import lesson_package.talk.animal

def main():
    lesson_package.talk.animal.sing()

if __name__ == '__main__':
    main()
