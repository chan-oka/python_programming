# class Person:
# class Person():
class Person(object):
    def __init__(self, name):
        self.name = name
        print('first')

    def say_something(self):
        print(self.name)
        self.run(10)

    def run(self, num):
        print('run' * num)

    def __del__(self):
        print('bye bye')

person = Person('mike')
person.say_something()
del person
print('#########')

class Car(object):
    def run(self):
        print('run')

class ToyotaCar(Car):
    pass

class TeslaCar(Car):
    def auto_run(self):
        print('auto_run')

car = Car()
car.run()

toyota_car = ToyotaCar()
toyota_car.run()

tesla_car = TeslaCar()
tesla_car.run()
tesla_car.auto_run()

class Car(object):
    def __init__(self, model=None):
        self.model = model

    def run(self):
        print('run')

class ToyotaCar(Car):
    def run(self):
        print('fast toyota car')

class TeslaCar(Car):
    def __init__(self, model='Model', enable_auto_run=False):
        # self.model = model
        super().__init__(model)
        self.enable_auto_run = enable_auto_run

    def run(self):
        print('fast tesla car')

    def auto_run(self):
        print('auto_run')

car = Car()
car.run()

toyota_car = ToyotaCar('Lexus')
print(toyota_car.model)
toyota_car.run()

tesla_car = TeslaCar()
tesla_car.run()
tesla_car.auto_run()

class Car(object):
    def __init__(self, model=None):
        self.model = model

    def run(self):
        print('run')

class ToyotaCar(Car):
    def run(self):
        print('fast toyota car')

class TeslaCar(Car):
    def __init__(self, model='Model', enable_auto_run=False, passwd="123"):
        # self.model = model
        super().__init__(model)
        self.__enable_auto_run = enable_auto_run
        self._passwd = passwd

    @property
    def enable_auto_run(self):
        return self._enable_auto_run

    @enable_auto_run.setter
    def enable_auto_run(self, is_enable):
        if self._passwd == 123:
            self._enable_auto_run = is_enable
        else:
            raise ValueError

    def run(self):
        print('__enable_auto_run', self.__enable_auto_run)
        print('fast tesla car')

    def auto_run(self):
        print('auto_run')

tesla_car = TeslaCar('modele_s', passwd='1234')
tesla_car.run()
# tesla_car.enable_auto_run = True
# print(tesla_car.enable_auto_run)

class Person(object):
    def __init__(self, age=1):
        self.age = age

    def drive(self):
        if self.age >= 18:
            print('ok')
        else:
            raise Exception('ng')

class Baby(Person):
    def __init__(self, age=1):
        if age < 18:
            super().__init__(age)
        else:
            raise ValueError('Baby ValueError')

class Adult(Person):
    def __init__(self, age=18):
        if age >= 18:
            super().__init__(age)
        else:
            raise ValueError('Adult ValueError')

    def drive(self):
        if self.age >= 18:
            print('ok')
        else:
            raise Exception('ng')

baby = Baby()
adult = Adult()

class Car(object):
    def __init__(self, model=None):
        self.model = model

    def run(self):
        print('run')

    def ride(self, person):
        person.drive()

car = Car()
car.ride(adult)
#car.ride(baby)

import abc

class Person(metaclass=abc.ABCMeta):
    def __init__(self, age=1):
        self.age = age

    @abc.abstractmethod
    def drive(self):
        pass

class Baby(Person):
    def __init__(self, age=1):
        if age < 18:
            super().__init__(age)
        else:
            raise ValueError('Baby ValueError')

    def drive(self):
        raise ValueError('Ng')

class Adult(Person):
    def __init__(self, age=18):
        if age >= 18:
            super().__init__(age)
        else:
            raise ValueError('Adult ValueError')

    def drive(self):
        print('OK')

baby = Baby()
# baby.drive()
adult = Adult()
adult.drive()

print("###############")

class Person(object):
    def talk(self):
        print('talk')

    def run(self):
        print('Person run')

class Car(object):
    def run(self):
        print('run')

# runは2つのクラスに定義、継承が先が優先
class PersonCarRobot(Person, Car):
    def fly(self):
        print('fly')

person_car_robot = PersonCarRobot()
person_car_robot.talk()
person_car_robot.run()
person_car_robot.fly()

print("###############")

class Person(object):
    kind = 'human'

    def __init__(self, name):
        self.name = name

    def who_are_you(self):
        print(self.kind, self.name)

a = Person('A')
a.who_are_you()

b = Person('B')
b.who_are_you()

class T(object):
    words = []
    def add_word(self, word):
        self.words.append(word)

c = T()
c.add_word('test')
c.add_word('test 2')
d = T()
d.add_word('d test')
d.add_word('d test 2')
print(d.words)

print("###############")

class Person(object):
    kind = 'aa human'

    def __init__(self):
        self.x = 100

    @classmethod
    def what_is_your_kind(cls):
        return cls.kind

    @staticmethod
    def about(year):
        print('about human {}'.format(year))

a = Person()
# ()つけてオブジェクトになっている
print(a)
print(a.x)
print(a.kind)
print(a.what_is_your_kind())
print(a.about(199))
print(Person().kind)
print(Person().what_is_your_kind())
print(Person().about(200))

# ()なし、ただクラスを参照
b = Person
print(b)
print(b.kind)
print(b.what_is_your_kind())
print(b.about(201))
print(Person.kind)
print(Person.what_is_your_kind())
print(Person.about(202))

print("###############")

class Word(object):
    def __init__(self, text):
        self.text = text

    def __str__(self):
        return '__str__'

    def __len__(self):
        return len(self.text)

    def __add__(self, other):
        return self.text.lower() + other.text.lower()

    def __eq__(self, other):
        return self.text.lower() == other.text.lower()

w = Word('test')
print(len(w))

w = Word('test')
w2 = Word('_____test____')
print(w + w2)
print(w2 + w)
print(w + w)
print(w2 + w2)

w = Word('test')
w2 = Word('test')

print(w == w2)