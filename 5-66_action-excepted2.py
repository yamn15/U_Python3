# 独自例外の作成
print('********************************************************************')
print('(1)')

# 以下の場合はIndexErrorが出力される
# raise IndexError('test error')


print('********************************************************************')
print('(2)')

# クラスを使用して独自の例外処理を行う
class UppercaseError(Exception):
    pass

def check():
    words = ['apple', 'orange', 'banana']
    for word in words:
        if word.isupper():
            raise UppercaseError(word)

# 大文字がないかを確認する関数。wordsはすべて小文字なので、エラーは出ない
check()


print('********************************************************************')
print('(3)')

class UppercaseError(Exception):
    pass

# raiseを使用して、エラーを設定できる
def check():
# apple を APPLEに変えると、エラーが発生する
    words3 = ['apple', 'orange', 'banana']
    for word3 in words3:
        if word3.isupper():
            raise UppercaseError(word3)

check()


print('********************************************************************')
print('(4)')

class UppercaseError4(Exception):
    pass

def check4():
    words4 = ['APPLE', 'orange', 'banana']
    for word4 in words4:
        if word4.isupper():
            raise UppercaseError4(word4)

# 独自の例外処理を設定できる
try:
    check4()
except UppercaseError4 as exc:
    print('This is my fault. Go next')

## pythonの既存のエラーと同じエラー(例えばValueなど)を独自エラーとして記述するとほかのプログラマが混乱するので要注意




