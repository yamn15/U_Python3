# クロージャ―
## https://qiita.com/_rdtr/items/d3bc1a8d4b7eb375c368
## https://qiita.com/mtb_beta/items/d257519b018b8cd0cc2e
## https://qiita.com/deaikei/items/07d456c6eafccf986b64
## https://qiita.com/moonwalkerpoday/items/9bd987667a860adf80a2
print('*********************************************')
print('(1)')

# 単純なfunc
def add_num(a, b):
    return a + b

r = add_num(10, 20)

print(r)

print('*********************************************')
print('(2)')

# decolater
# funcの処理の前後にほかの処理を行う
def add_num2(a, b):
    return a + b

print('start')
r2 = add_num2(10, 20)
print('end')

print(r2)

print('*********************************************')
print('(3)')

# funcの前後で何らかの処理を行いたいときや、funcに機能を追加したいときにはデコレータを使う
## print_infoはデコレータのfunc
def print_info(func):
    # wrapperはinner func
    def wrapper(*args, **kwargs):
        print('start')
        # inner funcの中で、デコレータのfuncを実行する
        result = func(*args, **kwargs)
        print('end')
        # resultを処理の結果として返す
        return result
    return wrapper

def add_num3(a, b):
    return a + b

# 以下デコレータの実行
## add_numがprint_infoの引数
f = print_info(add_num3)
r3 = f(10, 20)
print(r3)


# 53 f処理スタート  func 「print_info」の(func)にadd_num3が入る
## 38 wrapper inner funcの処理が始まる
### 46 outer func 「print_info」の返り値として、wrapperが返される。
### 返す際はwrapperをオブジェクトとして返される
#### f にfunc 「print_info」が返ってくる。
#### add_numが入っている状態で返ってくる。
##### 53 r3の処理に移る
###### print infoが返したwrapperがfに入っている。=r3は wrapper(10, 20)という状態になっている
####### inner関数の処理がこのタイミングで始まる。
####### 引数は10, 20はtuple化され、argsに入る
####### 41 resultの処理に移る。resultの中のfuncはadd_numを引数として渡している → 47 add_numの中に10, 20が入る
####### add_numがa + bを行い、値をresultに返す
####### print('end')も処理
######## rにresultが返ってくる
######### r をprintで出力
########## デコレータは上記の通り処理が結構複雑かつコードが読みずらい

print('*********************************************')
print('(4)')
# デコレータの分かりやすい書き方
def print_info2(func2):
    def wrapper2(*args, **kwargs):
        print('start')
        result2 = func2(*args, **kwargs)
        print('end')
        return result2
    return wrapper2

# @xxxでデコレータを指定すれば、デコレータを簡単に実行できる
## 今回は @print_info がデコレータ
@print_info2
def add_num4(a, b):
    return a + b

r4 = add_num4(10, 20)
print(r4)

# 91 r の処理開始
## 次はいきなりプリントインフォのインナー関数が呼び出される
## ファンクションを実行
## add_numが引数としてデコレータに渡されている
## add_numの結果がresultに入る
### rが出力される

print('*********************************************')
print('(5)')

# デコレータ、一度定義すれば何度でも再利用できるので便利
## @xxx でデコレータを書けば、ほかの異なる関数に同じデコレータを適用できる

@print_info2
def substract_num(a, b):
    return a - b

r5 = substract_num(100, 50)
print(r5)

print('*********************************************')
print('(6)')

## 複数のデコレータを定義
def print_more(func6):
    def wrapper6(*args, **kwargs):
        print('func6:', func6.__name__)
        print('args:', args)
        print('kwargs:', kwargs)
        result6 = func6(*args, **kwargs)
        print('result6:', result6)
        return result6
    return wrapper6

def print_info6(func6):
    def wrapper6(*args, **kwargs):
        print('start')
        result6 = func6(*args, **kwargs)
        print('end')
        return result6
    return wrapper6


# 先に@print_infoの処理が始まる
## print('start')の処理が終わり、resultのfunctionが呼び出されたら@print_moreが実行される
### print_moreのresultがreturnされる際に、print_infoに戻る
#### print('end')が処理され、最終的にresultがr6に返る
@print_info6
@print_more
def add_num6(a, b):
    return a + b

r6 = add_num6(10, 20)
print(r6)


## 順序を逆にすると、分かりずらくなる = 意図した順番に出力されないかもしれないので要注意
## print_infoの処理が、print_moreの処理の間に入ってしまう
### 上に書かれているデコレータが先に実行されるので覚えておくこと
# @print_more
# @print_info6

print('*********************************************')

# @xxxを複数書く場合は、下記のような処理をしているイメージ
## デコレータで、デコレータを包み込むイメージ
# f = print_info(print_more(add_num3))
# r3 = f(10, 20)
# print(r3)


