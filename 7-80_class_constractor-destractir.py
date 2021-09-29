print('********************************************************************')
print('(1)')

class Person(object):
    def __init__(self, name):
        self.name = name


    def say_something(self):
        print('I am {}. hello'.format(self.name))
        self.run(10)

    def run(self, num):
        print('run' * num)


person = Person('Mike')
person.say_something()
