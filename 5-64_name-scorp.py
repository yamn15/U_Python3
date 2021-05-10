# 名前空間とスペース
print('********************************************************************')
print('(1)')

# グローバルに定義された変数
animal = 'cat'

# 変数を出力
print(animal)


print('********************************************************************')
print('(2)')

animal2 = 'cat'

def = f():
    print(animal2)

# Function内からグローバル変数の出力を行う
f()


print('********************************************************************')
print('(3)')

animal3 = 'cat'

# 関数内でanimalを定義(Local変数)し、そのanimalに何らかの値を入れてプログラムを実行しようとするとエラーになる
## 関数内にanimalを定義したことにより、一番上のanimal3はグローバル変数(cat)ではなく、ローカル変数(関数内の変数)としてみなされる。
### animal3が何も定義されていないためprintできないというエラーになる
#### 関数内の最初のprintをコメントアウトすると、動くプログラムになる
def = f():
    print(animal3)
    animal3 = 'dog'
    print('after', animal3)

# 関数内のanimal3を出力
f()

# グローバル変数のanimal3を出力
print('global', animal3)


print('********************************************************************')
print('(4)')

# グローバル変数のanimal4を、関数内で書き換えたい場合

animal4 = 'cat'

def = f():
    # 明示的にグローバルの変数を扱うと宣言する
    global animal4
    animal4 = 'dog'
    print('local', animal4)


f()
print('global', animal4)


print('********************************************************************')
print('(5)')

animal5 = 'cat'

def = f():
    # ローカル変数をコメントアウトした場合、locals()には、空のdictが出力される
    animal5 = 'dog'
    print('local:', locals())

# locals()を使用すれば、dict型で、ローカル変数に入っているkey/valueを表示できる
f()

# globals()を使用すれば、dict型で、グローバル変数に入っているkey,valueを表示できる
print('global:', globals())


print('********************************************************************')
print('(6)')

animal6 = 'cat'

def = f():
    # ローカル変数をコメントアウトした場合、locals()には、空のdictが出力される
    animal6 = 'dog'
    print('local:', locals())

# locals()を使用すれば、dict型で、ローカル変数に入っているkey/valueを表示できる
f()

# globals()を使用すれば、dict型で、グローバル変数に入っているkey,valueを表示できる
print('global:', globals())


# globals()を出力すると、pythonがグローバルで定義した変数がすべて出力される。
## 以下は__doc__の例

"""
Test Test ***************************************
"""


print('********************************************************************')
print('(7)')

animal7 = 'cat'

def = f():
    """ Testfunc doc """
    print(f.__name__)
    print(f.__doc__)

f()

print('global:', __name__)

# 変数の中身を知りたい場合は、globals()を使用するといい
print('global:', globals())
