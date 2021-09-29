print('********************************************************************')
print('(1)')

## classの初期化
class Person(object):
    def __init__(self):
        print('First')

    def say_something(self):
        print('hello')

# objectを作成した際に、最初に__init__が実行される
person = Person()


print('********************************************************************')
print('(2)')

## classの初期化後に値を保持したい場合
## selfに変数を紐づける
class Person(object):
    def __init__(self, name):
        self.name = name
        print(self.name)

    def say_something(self):
        print('hello')

## objectに引数を入れ、nameに入れ込む
## 引数を渡さなければエラーになるのは関数と同じ。"__init__()self, name = "のようにデフォルト引数を持たせるのも一つの手
person = Person('Mike')


print('********************************************************************')
print('(3)')

## 初期化に使用した変数を、メソッドでも呼び出せる
class Person(object):
    def __init__(self, name):
        self.name = name
        # print(self.name)

## say_something(self)の引数にselfがなければ、__init__のselfにアクセスできない。
## そのため、self.namemeメソッドを呼び出せない
    def say_something(self):
        print('I am {}. hello'.format(self.name))


person = Person('Mike')
person.say_something()

print('********************************************************************')
print('(4)')

class Person(object):
    def __init__(self, name):
        self.name = name
        # print(self.name)

    def say_something(self):
        print('I am {}. hello'.format(self.name))
        ## 初期化以外のメソッドも呼び出すことができる
        self.run()

    def run(self):
        print('run')


person = Person('Mike')
person.say_something()


print('********************************************************************')
print('(4)')


class Person(object):
    def __init__(self, name):
        self.name = name
        # print(self.name)

    def say_something(self):
        print('I am {}. hello'.format(self.name))
        ## ↓runの引数はここに記載する
        self.run(10)

    ## 引数を追加することもできる
    def run(self, num):
        print('run' * num)


person = Person('Mike')
person.say_something()
