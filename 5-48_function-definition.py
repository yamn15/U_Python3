print('**********************************************************************')

# 関数を定義する前に関数を実行しようとするとエラーが起きる
# pythonは上からスクリプトを読んでいく
# say_something()

# def xxx(): で関数名を定義する。
# 改行し、インデントを整え、関数内の処理を書く
def say_something():
    print('hi')

#xxx() で関数を実行する
# ()パレンティスの丸かっこがなければ実行できないので要注意
## say_something
say_something()

print('**********************************************************************')

# typeはfunction
print(type(say_something))

print('**********************************************************************')

# 違いが判らん
print(type(say_something()))

print('**********************************************************************')

# functionなので、変数に入れて実行することも可能
f = say_something
f()

print('**********************************************************************')

# 返り値
## 関数の中に、変数を定義。関数内にreturnを書けば、関数の返り値として変数を返す処理をする
def say_something2():
    s = 'hi'
    return s

# なぜresultのtypeがtype吐出力される？
result = say_something2()
print(result)

print('**********************************************************************')

print(type(say_something2()))
print(type(say_something2))
print(type, (result))

print('**********************************************************************')

# 引数
## 関数のパレンティスの丸かっこの中に「引数」を定義
def what_is_this(color):
    print(color)

### 関数に引数を入力した状態で実行する
### 引数が関数内に渡されて、処理が実行される
what_is_this('red')

print('**********************************************************************')

# 返り値
## 処理はresultから始まる。変数resultに関数「what_is_this2」を定義。
## what_is_this2の引数にredが入っていることにより、関数what_is_this2(color)の処理が始まる。
## 関数内の、if文に合致した値を、resultに返す
def what_is_this2(color):
    if color == 'red':
        return 'tomato'
    elif color == 'green':
        return 'green pepper'
    else:
        return "I don't know"

result = what_is_this2('red')
# 関数を定義すれば、何度もif文を再利用できる
# result = what_is_this2('green')
# result = what_is_this2('yellow')
print(result)

print('**********************************************************************')

