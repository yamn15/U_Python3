print('**********************************************************************')

# pythonでは何も値が入っていないことを「None」と表現する
## help出力結果では「class 'Non type'」と表示される。＝ Null object (中身が何もない)
### 変数を定義するが、何も値を入れたくない場合はNoneを使う

is_empty = None
print(type(is_empty))
print(help(is_empty))

print('**********************************************************************')

if is_empty == None:
    print('None!!!')







