# ジェネレータ内包表記
print('*******************************************************************************')
print('(1)')

# range関数をを使用し、数字を10まで出力するgenerator

def g():
    for i in range(10):
        yield i

g = g()
# typeを確認
print(type(g))
# Generatorを実行する際は、nextを使用する
print(next(g))
print(next(g))
print(next(g))
print(next(g))



print('*******************************************************************************')
print('(2)')

# (1)をジェネレータ内包表記を使用して記述

def g2():
    for i in range(10):
        yield i

# タプルではなく、ジェネレータになる
g2 = (i for i in range(10))
print(type(g2))
print(next(g2))


print('*******************************************************************************')
print('(3)')

# ジェネレータではなく、タプルとして記述
def g3():
    for i in range(10):
        yield i

# tupleとしたい場合は宣言が必要
g3 = tuple(i for i in range(10))
print(type(g3))
# tupleとして出力するので、nextは使用しない
print(g3)


print('*******************************************************************************')
print('(4)')

# ジェネレータ内包表記にif文を追加する
def g4():
    for i in range(10):
        yield i

g4 = (i for i in range(10) if i % 2 == 0)
print(type(g4))

## generatorがfor文が適用された状態で出力される。
## print(next(g4))
## print(next(g4))
## print(next(g4))
## print(next(g4))
## print(next(g4))


# ジェネレータ内包表記を、変数xを用いて、forループを使用して出力している
## ジェネレータでyield毎に出力された値に対してif文が適用され、Trueの値のみ、結果が出力される
for x in g4:
    print(x)





