# 位置引数のタプル化
print('**********************************************************************')

# 位置引数を出力する場合、printを複数書かなければならず少し手間
def say_something(word, word2, word3):
    print(word)
    print(word2)
    print(word3)

say_something('Hi!', 'Mike', 'Nance')

print('**********************************************************************')

# pyrhonでは、「*args」を使用すれば、まとめて位置引数を出力できる。なおかつタプル化される
def say_something2(*args):
    print(args)

say_something2('Hi!2', 'Manny', 'Anthony')

print('**********************************************************************')

# 以下の構文はタプル化されないけどどういうこと？
def say_something3(*args):
    print(*args)

say_something3('Hi!3', 'Manny', 'Anthony')

print('**********************************************************************')

# 「*args」をforループで回す
def say_something4(*args):
    for arg in args:
        print(arg)

say_something4('Hi!4', 'Manny', 'Anthony')

print('**********************************************************************')

# sがあるかないかで結果が変わる。なんだろう？しかも3行出力される・・・
def say_something5(*args):
    for arg in args:
        print(args)

say_something5('Hi!5', 'Manny', 'Anthony')

print('**********************************************************************')

# argsと位置引数の混合も可能
## wordに位置引数が入り、残りはargsとして出力される
### 残りの引数の数がわからないときなどに使用される
def say_something6(word, *args):
    print('word =', word)
    for arg in args:
        print(arg)

say_something6('Hi!', 'Manny', 'Anthony')

print('**********************************************************************')

# これはなんだ？
def say_something7(word, *args):
    print('word =', word)
    for arg in args:
        print(args)

say_something7('Hi!', 'Manny', 'Anthony')

print('**********************************************************************')

# 引数にタプルを挿入することもできる
## この表現は今ほとんど使われていない
def say_something8(word, *args):
    print('word =', word)
    for arg in args:
        print(arg)

t = ('Manny', 'Nancy')
say_something8('Hi!', *t)

print('**********************************************************************')
