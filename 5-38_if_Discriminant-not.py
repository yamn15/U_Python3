print('**********************************************************************')

# pythonでは何も値が入っていないことを「None」と表現する
## help出力結果では「class 'Non type'」と表示される。＝ Null object (中身が何もない)
### 変数を定義するが、何も値を入れたくない場合はNoneを使う

is_empty = None
print(type(is_empty))
# print(help(is_empty))

print('**********************************************************************')

# pythonでは等式を使用して変数がNoneであるか否かを判別することは推奨されていない
if is_empty == None:
    print('None!!!')

# pythonでは [is XXX]を使用して変数がNoneであるか否かを判別するほうが好ましい
if is_empty is None:
    print('None!!!')

if is_empty is not None:
    print('None!!!')

print('**********************************************************************')

# isは[is_empty]のような変数に入っているオブジェクトがNoneかどうかを判定する際によく使われる
## 以下簡単な例

## 値を1として、真同士なのでTrueと出力される
print(type(1 == True))
print(1 == True)

## オブジェクト同士が同じものであれば、真。そうでなければ偽
print(type(1 is True))
print(1 is True)
print(True is True)
print(None is None)
