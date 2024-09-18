def what_your_name():
    return 'こんにちは!私はRobokoです。あなたの名前は何ですか?\n'

def which_restaurant_do_you_like(name: str):
    return f"{name}さん。どこのレストランが好きですか?\n"

def have_a_good_day(name: str):
    return f"{name}さん。。ありがとうございました。\n良い一日を!さようなら。"

name = input(what_your_name())
like_restaurant = input(which_restaurant_do_you_like(name))

import csv
import os

if not os.path.isfile(path_w):

with open('recommend_restaurants.csv', 'w+') as csv_file:
    rows = csv_file.read()
    for row in rows:
        print(row)

    field_name = ['Name', 'Count']
    writer = csv.DictWriter(csv_file, fieldnames=field_name)
    writer.writeheader()
    writer.writerow({'Name': like_restaurant, 'Count': 1})

print(have_a_good_day(name))


