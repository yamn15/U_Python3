# 位置引数とキーワード引数とデフォルト引数
print('**********************************************************************')
print('(1)')


def menu(entree):
    print(entree)

menu('beef')

print('**********************************************************************')
print('(2)')

# メニューを複数出力する場合
## 引数を複数定義できる
def menu(entree, drink, dessert):
    print(entree)
    print(drink)
    print(dessert)

# 引数の順番を間違えると、想定通りに出力されないので要注意
# menu('beef', 'ice', 'beer')
menu('beef', 'beer', 'ice')

print('**********************************************************************')
print('(3)')

def menu2(entree, drink, dessert):
    print('entree =', entree)
    print('drink =', drink)
    print('dessert =', dessert)

# 順番を間違わないようにするためには、キーワードアーギュメントを使用する
# キーワードアーギュメント(引数)＝ 引数とキーワードを紐づける
## キーワード引数を使用すれば、順番に左右されずに意図したとおりの出力結果を得られる
menu2(entree='beef', dessert='beer', drink='ice')

print('**********************************************************************')
print('(4)')

def menu3(entree, drink, dessert):
    print('entree =', entree)
    print('drink =', drink)
    print('dessert =', dessert)

# キーワード引数と単純な引き数を共存できる
menu3('beef', dessert='beer', drink='ice')

# ただし位置引数とキーワード引数を混ぜて使用する場合は要注意。位置に気を付けないとエラーが起こる。
## pythonが引数を正しく判断できなくなる
# menu3(dessert='beer','beef', drink='ice')

print('**********************************************************************')
print('(5)')

# デフォルト引数
def menu4(entree='fish', drink='white wine', dessert='gelate'):
    print('entree =', entree)
    print('drink =', drink)
    print('dessert =', dessert)

# 引数の指定なし
## 引数を何も渡さなかった場合は、関数にデフォルトで定義された「デフォルト引数」が出力される
### 引数を渡した場合、デフォルト引数が新たに指定した引数に入れ替わる
#### 引数は複数指定できる
##### 位置引数とキーワード引数と混ぜて使える
# menu4()
# menu4(entree='chiken')
# menu4(entree='chiken', drink='beer')
menu4('chiken', drink='beer')




