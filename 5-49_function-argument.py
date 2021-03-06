# 関数の引数と、返り値の宣言
print('**********************************************************************')
print('(1)')

def add_num(a, b):
    return a + b

r = add_num(10, 20)
print(r)

print('**********************************************************************')
print('(2)')

# 型を指定して、関数を定義できる
## ただしpythonではほとんど使用されていない構文

def add_num(a: int, b: int) -> int:
    return a + b

r = add_num(10, 20)
print(r)

print('**********************************************************************')
print('(3)')

# stringの型指定
# def add_num(a: int, b: int) ->int:
## pythonはintで指定しても下記のプログラミングは動いてしまうので要注意
def add_num(a: str, b: str) ->str:
    return a + b

r = add_num('a', 'b')
print(r)