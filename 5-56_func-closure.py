# クロージャ―
## https://qiita.com/naomi7325/items/57d141f2e56d644bdf5f
### クロージャ(関数閉方)とは外側の変数を記憶した関数です。
print('**********************************************************************')
print('(1)')

# innerのfuncは実行されない
def outer(a, b):

    def inner():
        return a + b

    return inner

print(outer(1, 2))

print('**********************************************************************')
print('(2)')

# innerのfuncを実行する方法
## 定義したfに指定した引数「1, 2」がfuncのouter「a, b」に入る
### 本来ならinner func「a + b」に「5, 10」が入るところだが、実行はされない→return inner2に実行を意味する「()」がついていないから
#### inner funcはfに渡されて、未実行のまま待機しているイメージ
##### fが実行された際に、innerがようやく実行される→rに15(inner関数の実行結果)が渡されて出力される
def outer2(a, b):

    def inner2():
        return a + b

    return inner2

f = outer2(5, 10)
r = f()
print(r)

print('**********************************************************************')
print('(3)')

# 利用するケース
## 例えば25＋50を後から実行したいとき。(ここでは***を出力するプリントを間に挟んでいる)
### 変数を定義し、その変数の中にfunctと引数を書く。
#### funcの外で、さらに変数を定義し、その中でfuncを実行する
def outer3(a, b):

    def inner3():
        return a + b

    return inner3

f = outer3(25, 50)

print('***********')

r = f()
print(r)

print('**********************************************************************')
print('(4)')


def circle_area_func(pi):
    def circle_area(radius):
        return pi * radius * radius

# cercle_areaを処理をしない
# 返り値としてcircle_area_funcへ関数内関数の結果をca1 or ca2に返す。
#
    return circle_area

# piを3.14として使用したい場合は、ca1を使用
# piを3.141519として使用したい場合は、ca2を使用
ca1 = circle_area_func(3.14)
ca2 = circle_area_func(3.141592)

print(ca1(10))
print(ca2(10))
