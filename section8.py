f = open('text.txt', 'w')
f.write('Test\n')
print('print', file=f)
f.close()

# withを使うとcloseが不要
with open('text.txt', 'w') as f:
    f.write('Testaaa\n')

s = """
aaa
bbb
ccc
ddd
"""

with open('text.txt', 'w') as f:
    f.write(s)

# with open('text.txt', 'r') as f:
#     print(f.read())

with open('text.txt', 'r') as f:
    while True:
        line = f.readline()
        print(line)
        if not line:
            break

import csv

with open('test.csv', 'w') as csv_file:
    field_name = ['Name', 'Count']
    writer = csv.DictWriter(csv_file, fieldnames=field_name)
    writer.writeheader()
    writer.writerow({'Name': 'test', 'Count': 2})

import tempfile

with tempfile.TemporaryFile(mode='w+') as t:
    t.write('TemporaryFile')
    t.seek(0)
    print(t.read())


import subprocess

subprocess.run(['ls', '-la'])
subprocess.run('ls -la', shell=True)

print('############')

import datetime

now = datetime.datetime.now()
print(now)
print(now.isoformat())
print(now.strftime('%Y-%m-%d %H:%M:%S.%f'))

today = datetime.date.today()
print(today)

time = datetime.time(hour=1, minute=10, second=10, microsecond=10)
print(time)
print(time.isoformat())

print('############')

print(now)
d = datetime.timedelta(weeks=1)
print(now + d)
d = datetime.timedelta(weeks=-1)
print(now + d)

import time
time.sleep(1)
