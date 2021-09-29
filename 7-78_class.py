## classについて
print('********************************************************************')
print('(1)')

# capitalizeを右クリックし、「定義へ移動」を選択すると、buitins.pyiが表示される。
# メソッドがどんなクラスに所属しているかがわかる
s = 'qwertyu'
print(s.capitalize())


## classについて
print('********************************************************************')
print('(2)')

# classの作成
class Person(object):
    def say_something(self):
        print('hello')

# objectを作成
person = Person()

# personまで打ち込み、'.'を打つと、作成したsay_somethingメソッドが表示される
person.say_something()


print('********************************************************************')
print('(3)')

# Python3なら、 classの表記の際に、"(object)"の記載がなくても問題ない。
# もしくは"()"の未記載してもよい。
# ただし、"(object)"を付けると明示的にclassを作成しているとコードから分かる。そのためつけることが推奨される
class Person:
    def say_something(self):
        print('hello')

# objectを作成
person = Person()

# personまで打ち込み、'.'を打つと、作成したsay_somethingメソッドが表示される
person.say_something()
