# キーワード引数の辞書化
print('**********************************************************************')
print('(1)')

def menu(entree='beef', drink='wine'):
    print(entree, drink)

menu()

print('**********************************************************************')
print('(2)')

def menu2(entree='beef', drink='wine'):
    print(entree, drink)

menu2(entree='beef', drink='coffee')

print('**********************************************************************')
print('(3)')

# 複数のキーワードを引数として使用したい場合は、「**kwargs」を使用する
def menu3(**kwargs):
    print(kwargs)

menu3(entree='fish', drink='coffee')

print('**********************************************************************')
print('(4)')

# forループを使用する
def menu4(**kwargs):
    for k, v in kwargs.items():
        print(k, v)

menu4(entree='fish', drink='coffee')

print('**********************************************************************')
print('(5)')

# 変数dにdictを定義し、それを引数として渡す。
## 定義がわかりやすいのでよく使用される表現
def menu5(**kwargs):
    for k, v in kwargs.items():
        print(k, v)

d = {
    'entree': 'beef',
    'drink': 'ice coffee',
    'dessert': 'ice'
}

menu5(**d)

# ※Pythonの可変長引数（*args, **kwargs）の使い方
## https://note.nkmk.me/python-args-kwargs-usage/
### 関数定義で引数に*と**（1個または2個のアスタリスク）をつけると、任意の数の引数（可変長引数）を指定することができる。
### 慣例として*args, **kwargsという名前が使われることが多いが、*と**が頭についていれば他の名前でも問題ない。以下のサンプルコードでは*args, **kwargsという名前を使う。
### 以下の内容について説明する。
### *args: 複数の引数をタプルとして受け取る
### **kwargs: 複数のキーワード引数を辞書として受け取る

print('**********************************************************************')
print('(6)')

# 位置引数とtuple化とdict化を混在できる
def menu6(food, *args, **kwargs):
## 引数を書く順番を待ちがえるとエラーになるので要注意
## def menu6(food, **kwargs, *args,):
    print(food)
    print(args)
    print(kwargs)

# foodにbananaが入る -> 位置引数
## appleとorangeがargsとして入る -> tuple
### entree,drinkがkwargsとして入る -> dict

menu6('banana', 'apple', 'orange', entree='beef', drink='coffee')

print('**********************************************************************')
print('(7)')

### *(args)と**(kwargs)を混在させるときは、*が先で、**が後ろでなくてはならない
### 以下のコードはエラーになる
# def menu7(food, **kwargs, *args):
#     print(food)
#     print(kwargs)
#     print(args)

# foodにbananaが入る -> 位置引数
## appleとorangeがargsとして入る -> tuple
### entree,drinkがkwargsとして入る -> dict

# menu6('banana', entree='beef', drink='coffee', 'apple', 'orange',)

print('**********************************************************************')
