# ジェネレーター
## イテレータ(反復処理)の要素
### ジェネレータでは、反復処理を行う際に、1要素を取り出し生成していく
print('*******************************************************************************')
print('(1)')

# forループを使用した単純な反復処理
l = ['Good morning', 'Good afternoon', 'Good night']

for i in l:
    print(i)


print('*******************************************************************************')
print('(2)')

# ジェネレータを使用した反復処理
def greeting():
    yield 'Good morning'
    yield 'Good afternoon'
    yield 'Good night'

for g in greeting():
    print(g)


print('*******************************************************************************')
print('(3)')

# ジェネレータを使用した反復処理2
def greeting():
    yield 'Good morning'
    yield 'Good afternoon'
    yield 'Good night'

g = greeting()
# 一番上のGoodmorningのみ生成される
print(next(g))

## 間に何かしらの処理を差し込むことができる
print('-------------------------')

# 二番目のGoodafternoonが生成される
print(next(g))

## 間に何かしらの処理を差し込むことができる
print('-------------------------')

# 三番目のGoodnightが生成される
print(next(g))

### forループの場合は、要素をすべて一連の流れで処理をする。
### ジェネレータは、nextというコマンドを使用し、yieldを出力して、処理を抜ける。
### ジェネレータは、反復処理の合間にほかの処理を差し込むことができる

print('*******************************************************************************')
print('(4)')

# ジェネレータを使用した反復処理3

## runを10回返すジェネレータ
### ジェネレータにはreturnはない
### pyrhonはyieldというコマンドを確認したら、funcをジェネレータとして認識する
### 処理を小分けにする際にジェネレータは使用されることが多い
def counter(num=10):
    for _ in range(num):
        yield 'run'

def greeting2():
    yield 'Good morning'
    yield 'Good afternoon'
    yield 'Good night'

g2 = greeting2()
c = counter()

print(next(g2))

# ジェネレータを入れ子にできる
print(next(c))
print(next(c))
print(next(c))




print(next(g2))

print(next(c))
print(next(c))
print(next(c))


print(next(g2))

print(next(c))
print(next(c))
print(next(c))
